import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score, KFold
import os

# Emulate the notebook steps for Automobile
file = "Bdcars.csv"
filename = os.path.join(os.getcwd(), 'Data', file)
data = pd.read_csv(filename)

# Cleaning
data = data[data[' price'] != '?']
data[' price'] = data[' price'].astype('float')

# Prepare inputs (simplified version of what's in the NB)
# Usually they select numeric columns or encoded ones
numeric_cols = data.select_dtypes(include=[np.number]).columns
if ' price' in numeric_cols:
    numeric_cols = numeric_cols.drop(' price')

X = data[numeric_cols].fillna(0) # Basic fill for simulation
y = data[' price']

model = linear_model.LinearRegression()
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
r2_scores = cross_val_score(model, X, y, cv=kfold, scoring='r2')

print(f"Mean R2: {r2_scores.mean():.4f}")
print(f"R2 Std: {r2_scores.std():.4f}")
