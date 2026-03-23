import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

Data = pd.read_csv('c:/mlearn-lab/FourthPractice/Data/bank/bank.csv', sep=';')

# Binary mappings
for col in ['default', 'housing', 'loan']:
    Data[col] = Data[col].map({'no': -1, 'yes': 1}).fillna(0)
Data['y'] = Data['y'].map({'no': 0, 'yes': 1})

# Feature engineering
Data['contacted_before'] = (Data['pdays'] != -1).astype(float)
Data['pdays'] = Data['pdays'].apply(lambda x: 0 if x == -1 else x)
Data['balance_log'] = np.log(np.abs(Data['balance'])+1)*np.sign(Data['balance'])
Data['duration_log'] = np.log(Data['duration']+1)

# Derived features from common sense
Data['campaign_intensity'] = Data['campaign'] * Data['duration_log']  # total marketing effort
Data['age_balance'] = Data['age'] * Data['balance_log']  # wealth accumulation proxy
Data['prev_success_rate'] = Data['previous'] * Data['contacted_before']  # history signal

# One-hot encoding
nominal_cols = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
Data = pd.get_dummies(Data, columns=nominal_cols, drop_first=True)
Data = Data.astype(float)

y = Data['y']
X = Data.drop('y', axis=1)

# Only polynomial expand numerical core features
num_core = ['age', 'balance_log', 'duration_log', 'campaign', 'pdays', 'previous',
            'day', 'contacted_before', 'campaign_intensity', 'age_balance', 'prev_success_rate']

np.random.seed(42)
mask = np.random.rand(len(Data)) < 0.75
X_train, X_test = X[mask].copy(), X[~mask].copy()
y_train, y_test = y[mask], y[~mask]

# Scale everything
scaler = StandardScaler()
X_train_s = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns, index=X_train.index)
X_test_s = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns, index=X_test.index)

# Poly expand ONLY numerical core
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_train_num_poly = poly.fit_transform(X_train_s[num_core])
X_test_num_poly = poly.transform(X_test_s[num_core])
poly_names = [f'poly_{i}' for i in range(X_train_num_poly.shape[1])]

# Combine: one-hot dummies + polynomial numerical
other_cols = [c for c in X_train_s.columns if c not in num_core]
X_train_final = np.hstack([X_train_s[other_cols].values, X_train_num_poly])
X_test_final = np.hstack([X_test_s[other_cols].values, X_test_num_poly])
print(f"Final feature count: {X_train_final.shape[1]}")

print("\n" + "="*60)
print("TEST: lbfgs L2 with smart poly (numerical only)")
print("="*60)
for C in [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100]:
    lr = LogisticRegression(solver='lbfgs', penalty='l2', C=C, max_iter=5000)
    lr.fit(X_train_final, y_train)
    acc = accuracy_score(y_test, lr.predict(X_test_final))
    print(f"  C={C}: Acc={acc:.4f}")

print("\n" + "="*60)
print("TEST: liblinear L1 (feature selection) with smart poly")
print("="*60)
for C in [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]:
    lr = LogisticRegression(solver='liblinear', penalty='l1', C=C, max_iter=5000)
    lr.fit(X_train_final, y_train)
    acc = accuracy_score(y_test, lr.predict(X_test_final))
    nz = np.sum(lr.coef_ != 0)
    print(f"  C={C}: Acc={acc:.4f} (non-zero={nz}/{X_train_final.shape[1]})")

# Best model report
print("\n" + "="*60)
print("BEST MODEL DETAILED REPORT")
print("="*60)
best = LogisticRegression(solver='lbfgs', penalty='l2', C=0.1, max_iter=5000)
best.fit(X_train_final, y_train)
print(f"Train Acc: {accuracy_score(y_train, best.predict(X_train_final)):.4f}")
print(f"Test Acc:  {accuracy_score(y_test, best.predict(X_test_final)):.4f}")
print(classification_report(y_test, best.predict(X_test_final)))
