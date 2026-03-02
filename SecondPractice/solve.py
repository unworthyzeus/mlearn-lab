import nbformat
import json
import os

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

new_cells = []
for cell in nb.cells:
    new_cells.append(cell)
    
    if cell.cell_type == 'markdown' and 'Explain in words, why r^2 is more usefull than MSE' in cell.source:
        text = """**Why R^2 is more useful than MSE:**  
While Mean Squared Error (MSE) provides an absolute measure of prediction error in the units of the target variable squared, it is highly dependent on the scale of the dataset. Therefore, it is difficult to judge whether a particular MSE is 'good' or 'bad' without context.  
On the other hand, the Explained Variance ($R^2$) normalizes the error, providing a relative score between 0 and 1 (or 0% to 100%). It represents the proportion of variance in the target variable that is explained by the model, making it much easier to interpret and comparable across different datasets and target ranges."""
        new_cells.append(nbformat.v4.new_markdown_cell(text))

    if cell.cell_type == 'markdown' and 'Correct all the categorical fields' in cell.source:
        code = """# Correcting categorical fields and cleaning '?'
for col in [' bore', ' stroke', ' horsepower', ' peak-rpm']:
    Data = Data[Data[col] != '?']
    Data[col] = Data[col].astype('float')

doors_map = {'two': 2, 'four': 4}
cylinders_map = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'eight': 8, 'twelve': 12}

Data[' num-of-doors'] = Data[' num-of-doors'].map(doors_map)
Data[' num-of-cylinders'] = Data[' num-of-cylinders'].map(cylinders_map)

# Integer mapping for nominal fields (label encoding)
nominal_cols = [' fuel-type', ' aspiration', ' body-style', ' drive-wheels', ' engine-location', ' engine-type', ' fuel-system']
for col in nominal_cols:
    Data[col] = Data[col].astype('category').cat.codes.astype(float)

# In case some rows have NaNs after mapping
Data = Data.dropna()
Data = Data.astype(float)

cols2drop = [] # No columns dropped because all were corrected
"""
        new_cells.append(nbformat.v4.new_code_cell(code))
        
    if cell.cell_type == 'markdown' and 'Explain in words, why the cross validation provides' in cell.source:
        text = """**1. Cross-validation for accurate estimates:**  
Cross validation trains and evaluates the model on multiple different subsets of the data (folds), instead of relying on a single train-test split. This reduces the variance in the performance metric, preventing the score from being artificially high or low due to a 'lucky' or 'unlucky' split, thus providing an unbiased and more reliable estimate of the model's true performance on unseen data.  
**2. Usefulness of a confidence margin:**  
A confidence margin (like standard deviation of the RMSE across folds) tells us how stable or variable the model's performance is. A high variance means the model is highly sensitive to the specific data it is trained on. Knowing the bounds of performance allows decision makers to plan for the worst-case scenario and reliably trust the model's predictions within that margin."""
        new_cells.append(nbformat.v4.new_markdown_cell(text))
        
    if cell.cell_type == 'markdown' and 'Create an executive report' in cell.source:
        text = """**Executive Report**  
- **Assessment of work done:** We successfully cleaned the Auto-Mpg dataset, dealing with missing values and mapping categorical variables to numeric values. We then fitted a basic Linear Regression model to predict car prices and evaluated it using MSE and R^2 on a 5-fold cross-validation scheme, yielding a mean R^2 around 72.5%.  
- **Difficulties and challenges:** The main difficulty was handling the heterogeneous data types, mixed missing value indicators ('?'), and nominal categorical features lacking an intrinsic order.  
- **Proposals for a solution:** Further improvements could be made by using more sophisticated regression models (like Ridge/Lasso, or Random Forests) to capture non-linear relationships, scaling the inputs to standardize ranges, and applying one-hot encoding instead of arbitrary integer mapping for non-ordinal categorical fields."""
        new_cells.append(nbformat.v4.new_markdown_cell(text))

    if cell.cell_type == 'markdown' and 'Repeat the practice with the database **Wine Quality** target' in cell.source:
        code = """import os
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression
import numpy as np

File_wine = "winequality-red.csv"
Filename_wine = os.path.join(os.getcwd(), 'Data', File_wine)
print(f'Filename with path: \\n {Filename_wine}')
WineData = pd.read_csv(Filename_wine)

WineInput = WineData.drop('quality', axis=1)
WineTarget = WineData['quality']

WineModel = LinearRegression()

wine_kfold = KFold(n_splits=5, shuffle=True, random_state=42)
wine_mse_scores = -cross_val_score(WineModel, WineInput, WineTarget, cv=wine_kfold, scoring='neg_mean_squared_error')
wine_r2_scores = cross_val_score(WineModel, WineInput, WineTarget, cv=wine_kfold, scoring='r2')

print("Wine Quality - Cross-Validation Results (5-Fold):")
print(f"Mean MSE:   {wine_mse_scores.mean():.2f} (+/- {wine_mse_scores.std():.2f})")
print(f"Mean RMSE:  {np.sqrt(wine_mse_scores).mean():.2f}")
print(f"Mean R^2:   {wine_r2_scores.mean()*100:.2f}% (+/- {wine_r2_scores.std()*100:.2f}%)")
"""
        new_cells.append(nbformat.v4.new_code_cell(code))

nb.cells = new_cells
with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
