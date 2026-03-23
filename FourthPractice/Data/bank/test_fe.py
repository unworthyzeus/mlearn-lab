import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load data
Data = pd.read_csv('bank.csv', sep=';')

# Baseline model (Linear scale, mapped as integers)
# This simulates the "initial model in linear scale"
Data_lin = Data.copy()
for col in ['default', 'housing', 'loan', 'y']:
    Data_lin[col] = Data_lin[col].map({'no': -1, 'yes': 1, 'unknown': 0}).fillna(0)
for col in ['job', 'marital', 'education', 'contact', 'month', 'poutcome']:
    Data_lin[col] = pd.factorize(Data_lin[col])[0] + 1

X_lin = Data_lin.drop('y', axis=1).astype(float)
y_lin = Data_lin['y'].astype(float)

# Simple split
np.random.seed(42)
mask = np.random.rand(len(Data)) < 0.75
X_train_lin, X_test_lin = X_lin[mask], X_lin[~mask]
y_train_lin, y_test_lin = y_lin[mask], y_lin[~mask]

lr = LogisticRegression(solver='newton-cg', max_iter=1000)
lr.fit(X_train_lin, y_train_lin)
print("Accuracy (Linear, Ordinal Mapped):", accuracy_score(y_test_lin, lr.predict(X_test_lin)))

# Advanced Feature Engineered Model
Data_fe = Data.copy()
# Map binary
for col in ['default', 'housing', 'loan', 'y']:
    Data_fe[col] = Data_fe[col].map({'no': -1, 'yes': 1, 'unknown': 0}).fillna(0)

# PDAYS indicator
Data_fe['contacted_before'] = (Data_fe['pdays'] != -1).astype(float)
Data_fe['pdays'] = Data_fe['pdays'].apply(lambda x: 0 if x == -1 else x)

# Log transforms
Data_fe['balance'] = np.log(np.abs(Data_fe['balance'])+1)*np.sign(Data_fe['balance'])
Data_fe['duration'] = np.log(Data_fe['duration']+1)

# One-hot encoding
nominal_cols = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
Data_fe = pd.get_dummies(Data_fe, columns=nominal_cols, drop_first=True)

X_fe = Data_fe.drop('y', axis=1).astype(float)
y_fe = Data_fe['y'].astype(float)

X_train_fe, X_test_fe = X_fe[mask], X_fe[~mask]
y_train_fe, y_test_fe = y_fe[mask], y_fe[~mask]

# Scale
scaler = StandardScaler()
X_train_fe = scaler.fit_transform(X_train_fe)
X_test_fe = scaler.transform(X_test_fe)

lr_fe = LogisticRegression(solver='newton-cg', max_iter=1000)
lr_fe.fit(X_train_fe, y_train_fe)
print("Accuracy (Feature Engineeered):", accuracy_score(y_test_fe, lr_fe.predict(X_test_fe)))

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_fe, y_train_fe)
print("Accuracy (Random Forest on FE):", accuracy_score(y_test_fe, rf.predict(X_test_fe)))
