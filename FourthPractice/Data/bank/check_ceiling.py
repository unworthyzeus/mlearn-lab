import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

Data = pd.read_csv('c:/mlearn-lab/FourthPractice/Data/bank/bank.csv', sep=';')

for col in ['default', 'housing', 'loan']:
    Data[col] = Data[col].map({'no': -1, 'yes': 1}).fillna(0)
Data['y'] = Data['y'].map({'no': 0, 'yes': 1})

# Powerful feature engineering
Data['contacted_before'] = (Data['pdays'] != -1).astype(float)
Data['pdays'] = Data['pdays'].apply(lambda x: 0 if x == -1 else x)
Data['balance_log'] = np.log(np.abs(Data['balance'])+1)*np.sign(Data['balance'])
Data['duration_log'] = np.log(Data['duration']+1)
Data['campaign_intensity'] = Data['campaign'] * Data['duration_log']

nominal_cols = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
Data = pd.get_dummies(Data, columns=nominal_cols, drop_first=True)
Data = Data.astype(float)

y = Data['y']
X = Data.drop('y', axis=1)

scaler = StandardScaler()
X_s = pd.DataFrame(scaler.fit_transform(X), columns=X.columns, index=X.index)

# Check Logistic Regression CV
lr = LogisticRegression(solver='lbfgs', penalty='l2', C=1, max_iter=2000)
cv_lr = cross_val_score(lr, X_s, y, cv=5, scoring='accuracy')
print(f"LR CV Accuracy: {cv_lr.mean():.4f}")

# Check Light/Gradient Boosting CV
gbc = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
cv_gbc = cross_val_score(gbc, X_s, y, cv=5, scoring='accuracy')
print(f"GBC CV Accuracy: {cv_gbc.mean():.4f}")
