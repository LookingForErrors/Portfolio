
from data_manipulating import cleaned_train_test_split

import matplotlib.pyplot as plt

import pandas as pd

from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.metrics import fbeta_score, make_scorer
from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold
from sklearn.model_selection import cross_validate

from xgboost import XGBClassifier


scoring = {
        'roc_auc': 'roc_auc',
        'recall': 'recall',
        'precision': 'precision',
        'f2': make_scorer(fbeta_score, beta=2)
        }


def print_metrics(prediction_model, X_test, y_test):
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_validate(prediction_model, X_test, y_test,
                            scoring=scoring,
                            cv=cv,
                            n_jobs=-1,
                            return_train_score=True
                            )

    print("ROC AUC: ", scores['test_roc_auc'].mean().round(4))
    print("Recall: ", scores['test_recall'].mean().round(4))
    print("Precision: ", scores['test_precision'].mean().round(4))
    print("F2-Score: ", scores['test_f2'].mean().round(4))


def model_training(data_frame, undersampling=False,
                   cross_train=False):
    (X_train, y_train, X_validation, y_validation,
     X_test, y_test) = cleaned_train_test_split(data_frame,
                                                undersampling=undersampling)

    X_train = pd.concat([X_train, X_validation])
    y_train = pd.concat([y_train, y_validation])

    if cross_train:

        param_grid = {
            'max_depth': [3, 4, 5],
            'learning_rate': [0.05, 0.1, 0.2, 0.3],
            'scale_pos_weight': [1, 5, 10, 100, 500]
        }

        grid_search = GridSearchCV(
            estimator=XGBClassifier(objective='binary:logistic',
                                    n_estimators=300),
            param_grid=param_grid,
            scoring=scoring,
            refit='recall',
            cv=3,
            verbose=1
        )

        grid_search.fit(X_train, y_train, verbose=0)
        model = grid_search.best_estimator_

        params_xgb = model.get_xgb_params()
        print('Model parameters:')
        print('max_depth: {}'.format(params_xgb['max_depth']))
        print('learning_rate: {}'.format(params_xgb['learning_rate']))
        print('scale_pos_weight: {}'.format(params_xgb['scale_pos_weight']))

    else:
        model = XGBClassifier(
            objective='binary:logistic',
            learning_rate=0.3,
            max_depth=3,
            n_estimators=300,
            eval_metric='aucpr',
            )

        model.fit(X_train, y_train, eval_set=[(X_validation, y_validation)],
                  verbose=0)

    print_metrics(model, X_test=X_test, y_test=y_test)

    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)

    if undersampling:
        plt.title('undersampling Confusion Matrix')
        plt.savefig('undersampling.png')
    else:
        plt.title('Confusion Matrix')
        plt.savefig('base.png')

    return model
