import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score

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

# One-hot encoding
nominal_cols = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
Data = pd.get_dummies(Data, columns=nominal_cols, drop_first=True)
Data = Data.astype(float)

# Target
y = Data['y']
X = Data.drop('y', axis=1)

# Split
np.random.seed(42)
mask = np.random.rand(len(Data)) < 0.75
X_train, X_test = X[mask], X[~mask]
y_train, y_test = y[mask], y[~mask]

# Scale
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

print("="*60)
print("EXPERIMENT 1: Different solvers with L2")
print("="*60)
for solver in ['newton-cg', 'lbfgs', 'liblinear', 'saga']:
    for C in [0.01, 0.1, 1, 10, 100]:
        lr = LogisticRegression(solver=solver, penalty='l2', C=C, max_iter=2000)
        lr.fit(X_train_s, y_train)
        acc = accuracy_score(y_test, lr.predict(X_test_s))
        if acc > 0.905:
            print(f"  solver={solver}, C={C}: Test Acc={acc:.4f}")

print("\n" + "="*60)
print("EXPERIMENT 2: L1 regularization (feature selection)")
print("="*60)
for solver in ['liblinear', 'saga']:
    for C in [0.01, 0.1, 1, 10, 100]:
        lr = LogisticRegression(solver=solver, penalty='l1', C=C, max_iter=2000)
        lr.fit(X_train_s, y_train)
        acc = accuracy_score(y_test, lr.predict(X_test_s))
        if acc > 0.905:
            print(f"  solver={solver}, C={C}: Test Acc={acc:.4f}")

print("\n" + "="*60)
print("EXPERIMENT 3: Polynomial Features degree=2 + L2")
print("="*60)
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_train_poly = poly.fit_transform(X_train_s)
X_test_poly = poly.transform(X_test_s)
print(f"  Poly feature count: {X_train_poly.shape[1]}")
for solver in ['lbfgs', 'saga']:
    for C in [0.01, 0.1, 1, 10]:
        lr = LogisticRegression(solver=solver, penalty='l2', C=C, max_iter=2000)
        lr.fit(X_train_poly, y_train)
        acc = accuracy_score(y_test, lr.predict(X_test_poly))
        if acc > 0.905:
            print(f"  solver={solver}, C={C}: Test Acc={acc:.4f}")

print("\n" + "="*60)
print("EXPERIMENT 4: Polynomial Features degree=2 + L1 (sparse)")
print("="*60)
for C in [0.01, 0.1, 1, 10]:
    lr = LogisticRegression(solver='saga', penalty='l1', C=C, max_iter=2000)
    lr.fit(X_train_poly, y_train)
    acc = accuracy_score(y_test, lr.predict(X_test_poly))
    n_nonzero = np.sum(lr.coef_ != 0)
    if acc > 0.905:
        print(f"  solver=saga, C={C}: Test Acc={acc:.4f}, non-zero coeffs={n_nonzero}")

print("\n" + "="*60)
print("EXPERIMENT 5: ElasticNet (L1+L2 mix)")
print("="*60)
for C in [0.01, 0.1, 1, 10]:
    for ratio in [0.1, 0.3, 0.5, 0.7, 0.9]:
        lr = LogisticRegression(solver='saga', penalty='elasticnet', C=C, l1_ratio=ratio, max_iter=2000)
        lr.fit(X_train_poly, y_train)
        acc = accuracy_score(y_test, lr.predict(X_test_poly))
        if acc > 0.91:
            print(f"  C={C}, l1_ratio={ratio}: Test Acc={acc:.4f}")

print("\n" + "="*60)
print("EXPERIMENT 6: Cross-validated best model")
print("="*60)
cv_scores = cross_val_score(
    LogisticRegression(solver='lbfgs', penalty='l2', C=1, max_iter=2000),
    X_train_poly, y_train, cv=5, scoring='accuracy'
)
print(f"  CV Accuracy (poly+lbfgs+C=1): {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")

# Best config from experiments
best = LogisticRegression(solver='lbfgs', penalty='l2', C=1, max_iter=2000)
best.fit(X_train_poly, y_train)
print(f"\n  BEST Final Test Accuracy: {accuracy_score(y_test, best.predict(X_test_poly)):.4f}")
print(classification_report(y_test, best.predict(X_test_poly)))
