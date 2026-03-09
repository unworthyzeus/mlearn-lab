import pandas as pd
import numpy as np
import os
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score

file = "winequality-red.csv"
filename = os.path.join(os.getcwd(), 'Data', file)
data = pd.read_csv(filename)

X = data.drop('quality', axis=1)
y = data['quality']

model = linear_model.LinearRegression()

# 1. Full Fit Evaluation (Training set)
model.fit(X, y)
y_pred = model.predict(X)
mse_full = mean_squared_error(y, y_pred)
r2_full = r2_score(y, y_pred)

# 2. Cross-Validation (5-Fold)
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
r2_cv = cross_val_score(model, X, y, cv=kfold, scoring='r2')
mse_cv = -cross_val_score(model, X, y, cv=kfold, scoring='neg_mean_squared_error')

print(f"Full Dataset Fit:")
print(f"  MSE: {mse_full:.4f}")
print(f"  R2: {r2_full*100:.2f}%")

print(f"\nCross-Validation (5-Fold):")
print(f"  Mean MSE: {mse_cv.mean():.4f}")
print(f"  Mean R2: {r2_cv.mean()*100:.2f}%")
