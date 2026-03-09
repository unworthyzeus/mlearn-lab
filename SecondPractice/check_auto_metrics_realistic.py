import pandas as pd
import numpy as np
import os
from sklearn import linear_model
from sklearn.model_selection import KFold, cross_val_score

file = "Bdcars.csv"
filename = os.path.join(os.getcwd(),'Data',file)
data =pd.read_csv(filename)

# Cleaning logic as per notebook
data = data[data[' price'] != '?']
data[' price'] = data[' price'].astype('float')

# Emulate categorical mapping for ' make' or similar if it's in the NB
# For now, let's just use numeric + simple factorize for all object columns
for col in data.columns:
    if data[col].dtype == 'object':
        # Simple factorize as per common notebook practices
        data[col] = pd.factorize(data[col])[0]

data = data.fillna(data.mean(numeric_only=True))

X = data.drop(' price', axis=1)
y = data[' price']

# Simple LR
model = linear_model.LinearRegression()
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

r2_scores = cross_val_score(model, X, y, cv=kfold, scoring='r2')

print(f"Mean R2: {r2_scores.mean()*100:.2f}%")
print(f"R2 Std: {r2_scores.std()*100:.2f}%")
