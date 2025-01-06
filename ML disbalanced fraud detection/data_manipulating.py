import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler


def cleaned_train_test_split(data, undersampling=False):
    X = data.drop('Class', axis=1)
    y = data['Class']

    X_start, X_test, y_start, y_test = train_test_split(X, y, test_size=0.2,
                                                        stratify=y)

    start_df = pd.concat([X_start, y_start], axis=1)
    fraud_df = start_df.loc[start_df['Class'] == 1]
    if undersampling:
        non_fraud_df = start_df.loc[start_df['Class'] == 0][:100000]
    else:
        non_fraud_df = start_df.loc[start_df['Class'] == 0]

    start = pd.concat([non_fraud_df, fraud_df])
    start = start.sample(frac=1, random_state=42)

    train, validation = train_test_split(start, test_size=0.2, shuffle=True)

    X_train = train.drop('Class', axis=1)
    y_train = train['Class']

    X_validation = validation.drop('Class', axis=1)
    y_validation = validation['Class']

    rob = RobustScaler()

    for column in data.columns[:-1]:

        X_train[column] = rob.fit_transform(X_train[column].
                                            values.reshape(-1, 1))
        X_validation[column] = rob.transform(X_validation[column].
                                             values.reshape(-1, 1))
        X_test[column] = rob.transform(X_test[column].
                                       values.reshape(-1, 1))

    return [X_train, y_train,
            X_validation, y_validation,
            X_test, y_test]
