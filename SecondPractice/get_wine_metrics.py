import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import cross_val_score, KFold
import os

# 1. Load Wine Data
file = "winequality-red.csv"
filename = os.path.join(os.getcwd(), 'Data', file)
data = pd.read_csv(filename)

# 2. Check info / basic numeric columns
X = data.drop('quality', axis=1)
y = data['quality']

# 3. Correlation check (usually done in the car section)
# We can just simulate the model training part
model = linear_model.LinearRegression()
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
r2_scores = cross_val_score(model, X, y, cv=kfold, scoring='r2')

print(f"Mean R2: {r2_scores.mean():.4f}")
print(f"R2 Std: {r2_scores.std():.4f}")
print(f"Head:\n{data.head(2).to_string()}")
print(f"Stats:\n{data.describe().to_string()}")
