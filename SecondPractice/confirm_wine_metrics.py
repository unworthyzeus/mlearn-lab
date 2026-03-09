import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score, KFold
import os

file = "winequality-red.csv"
filename = os.path.join(os.getcwd(), 'Data', file)
data = pd.read_csv(filename)

X = data.drop('quality', axis=1)
y = data['quality']

model = linear_model.LinearRegression()
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# R2
r2_scores = cross_val_score(model, X, y, cv=kfold, scoring='r2')

# MSE
mse_scores = -cross_val_score(model, X, y, cv=kfold, scoring='neg_mean_squared_error')

print(f"Mean R2: {r2_scores.mean()*100:.2f}%")
print(f"R2 Std: {r2_scores.std()*100:.2f}%")
print(f"Mean MSE: {mse_scores.mean():.6f}")
print(f"MSE Std: {mse_scores.std():.6f}")
