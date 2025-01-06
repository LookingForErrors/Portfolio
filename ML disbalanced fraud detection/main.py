import model as md

import pandas as pd

path = '/home/workspaces/machine_learning/data/creditcard.csv'

fraud_data = pd.read_csv(path)

print('No undersampling model metrics:')

model = md.model_training(fraud_data, undersampling=False, cross_train=False)

print('-'*60)

print('Model metrics with undersampling:')

model = md.model_training(fraud_data, undersampling=True, cross_train=False)

# No undersampling model metrics:
# ROC AUC:  0.9789
# Recall:  0.7022
# Precision:  0.8944
# F2-Score:  0.7286
# ------------------------------------------------------------
# Model metrics with undersampling:
# ROC AUC:  0.9829
# Recall:  0.8204
# Precision:  0.9182
# F2-Score:  0.8347
