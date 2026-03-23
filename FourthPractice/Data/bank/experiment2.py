import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# Load data
Data = pd.read_csv('c:/mlearn-lab/FourthPractice/Data/bank/bank.csv', sep=';')

# Map binary
for col in ['default', 'housing', 'loan']:
    Data[col] = Data[col].map({'no': -1, 'yes': 1}).fillna(0)
Data['y'] = Data['y'].map({'no': 0, 'yes': 1})

# pdays indicator
Data['contacted_before'] = (Data['pdays'] != -1).astype(float)
Data['pdays'] = Data['pdays'].apply(lambda x: 0 if x == -1 else x)

# Log transforms
Data['balance_log'] = np.log(np.abs(Data['balance'])+1)*np.sign(Data['balance'])
Data['duration_log'] = np.log(Data['duration']+1)

# One-hot encoding ALL nominal
nominal_cols = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
Data = pd.get_dummies(Data, columns=nominal_cols, drop_first=False)  # keep ALL dummies
Data = Data.astype(float)

y = Data['y']
X = Data.drop('y', axis=1)

np.random.seed(42)
mask = np.random.rand(len(Data)) < 0.75
X_train, X_test = X[mask], X[~mask]
y_train, y_test = y[mask], y[~mask]

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

print("="*60)
print("TEST A: No poly, lbfgs, varying C")
print("="*60)
for C in [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100]:
    lr = LogisticRegression(solver='lbfgs', penalty='l2', C=C, max_iter=5000)
    lr.fit(X_train_s, y_train)
    acc = accuracy_score(y_test, lr.predict(X_test_s))
    print(f"  C={C}: Acc={acc:.4f}")

print("\n" + "="*60)
print("TEST B: Poly degree=2 interaction_only, lbfgs, key C values")
print("="*60)
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_train_p = poly.fit_transform(X_train_s)
X_test_p = poly.transform(X_test_s)
print(f"  Feature count: {X_train_p.shape[1]}")
for C in [0.01, 0.1, 1, 10]:
    lr = LogisticRegression(solver='lbfgs', penalty='l2', C=C, max_iter=5000)
    lr.fit(X_train_p, y_train)
    acc = accuracy_score(y_test, lr.predict(X_test_p))
    print(f"  C={C}: Acc={acc:.4f}")

print("\n" + "="*60)
print("TEST C: L1 with liblinear on poly features")
print("="*60)
for C in [0.01, 0.1, 1, 10]:
    lr = LogisticRegression(solver='liblinear', penalty='l1', C=C, max_iter=5000)
    lr.fit(X_train_p, y_train)
    acc = accuracy_score(y_test, lr.predict(X_test_p))
    nz = np.sum(lr.coef_ != 0)
    print(f"  C={C}: Acc={acc:.4f} (non-zero={nz})")

print("\n" + "="*60)
print("TEST D: Poly degree=2 ALL features (not interaction_only)")
print("="*60)
poly2 = PolynomialFeatures(degree=2, interaction_only=False, include_bias=False)
X_train_p2 = poly2.fit_transform(X_train_s)
X_test_p2 = poly2.transform(X_test_s)
print(f"  Feature count: {X_train_p2.shape[1]}")
for C in [0.01, 0.1, 1]:
    lr = LogisticRegression(solver='lbfgs', penalty='l2', C=C, max_iter=5000)
    lr.fit(X_train_p2, y_train)
    acc = accuracy_score(y_test, lr.predict(X_test_p2))
    print(f"  C={C}: Acc={acc:.4f}")

print("\nDone!")
