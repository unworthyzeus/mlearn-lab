import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score
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

# Domain-specific interactions
Data['campaign_intensity'] = Data['campaign'] * Data['duration_log']
Data['age_balance'] = Data['age'] * Data['balance_log']
Data['prev_success'] = Data['previous'] * Data['contacted_before']
Data['duration_sq'] = Data['duration_log']**2
Data['balance_sq'] = Data['balance_log']**2
Data['age_sq'] = (Data['age'] / 10.0)**2
Data['campaign_sq'] = Data['campaign']**2

# One-hot encoding
nominal_cols = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
Data = pd.get_dummies(Data, columns=nominal_cols, drop_first=True)
Data = Data.astype(float)

y = Data['y']
X = Data.drop('y', axis=1)

# Core numerical features for polynomial expansion
num_core = ['age', 'balance_log', 'duration_log', 'campaign', 'pdays', 'previous',
            'day', 'contacted_before', 'campaign_intensity', 'age_balance',
            'prev_success', 'duration_sq', 'balance_sq', 'age_sq', 'campaign_sq']

np.random.seed(42)
mask = np.random.rand(len(Data)) < 0.75
X_train, X_test = X[mask].copy(), X[~mask].copy()
y_train, y_test = y[mask], y[~mask]

scaler = StandardScaler()
X_train_s = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns, index=X_train.index)
X_test_s = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns, index=X_test.index)

# Poly expand ONLY numerical core
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_train_num_poly = poly.fit_transform(X_train_s[num_core])
X_test_num_poly = poly.transform(X_test_s[num_core])

other_cols = [c for c in X_train_s.columns if c not in num_core]
X_train_final = np.hstack([X_train_s[other_cols].values, X_train_num_poly])
X_test_final = np.hstack([X_test_s[other_cols].values, X_test_num_poly])
print(f"Final feature count: {X_train_final.shape[1]}")

# Finer C grid around the sweet spot
print("\n" + "="*60)
print("FINE-GRAINED lbfgs L2")
print("="*60)
for C in [0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0]:
    lr = LogisticRegression(solver='lbfgs', penalty='l2', C=C, max_iter=5000)
    lr.fit(X_train_final, y_train)
    acc = accuracy_score(y_test, lr.predict(X_test_final))
    print(f"  C={C}: Acc={acc:.4f}")

print("\n" + "="*60)
print("FINE-GRAINED liblinear L1")
print("="*60)
for C in [0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 7.0, 10.0]:
    lr = LogisticRegression(solver='liblinear', penalty='l1', C=C, max_iter=5000)
    lr.fit(X_train_final, y_train)
    acc = accuracy_score(y_test, lr.predict(X_test_final))
    nz = np.sum(lr.coef_ != 0)
    print(f"  C={C}: Acc={acc:.4f} (non-zero={nz}/{X_train_final.shape[1]})")

# Cross-validation on best candidates
print("\n" + "="*60)
print("CROSS-VALIDATION (5-fold) on best candidates")
print("="*60)
X_all = np.vstack([X_train_final, X_test_final])
y_all = np.concatenate([y_train, y_test])

for name, model in [
    ("lbfgs L2 C=1", LogisticRegression(solver='lbfgs', penalty='l2', C=1, max_iter=5000)),
    ("lbfgs L2 C=5", LogisticRegression(solver='lbfgs', penalty='l2', C=5, max_iter=5000)),
    ("liblinear L1 C=1", LogisticRegression(solver='liblinear', penalty='l1', C=1, max_iter=5000)),
    ("liblinear L1 C=5", LogisticRegression(solver='liblinear', penalty='l1', C=5, max_iter=5000)),
]:
    scores = cross_val_score(model, X_all, y_all, cv=5, scoring='accuracy')
    print(f"  {name}: CV Acc={scores.mean():.4f} +/- {scores.std():.4f}")

print("\nDone!")
