import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

def create_code_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find the wine analysis start to inject missing pieces
insert_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and "## Practice 2 Part B: Wine Quality Analysis" in "".join(cell.get('source', [])):
        insert_idx = i
        break

if insert_idx != -1:
    # Build the full, expanded wine analysis workflow to match Car
    wine_full_workflow = [
        create_markdown_cell("## Practice 2 Part B: Wine Quality Analysis\n---\nFollowing the same workflow as the Automobile dataset, we will now analyze the **Wine Quality** dataset."),
        
        create_markdown_cell("### 1. Load the Wine Data"),
        create_code_cell(
"""File = "winequality-red.csv"
Filename = os.path.join(os.getcwd(), 'Data', File)
data_wine = pd.read_csv(Filename)
data_wine.head()"""
        ),
        
        create_markdown_cell("### 2. Data Exploration and Cleaning\nWe check for null values and the data types of the features."),
        create_code_cell("data_wine.info()\nprint(f\"\\nNull values:\\n{data_wine.isnull().sum()}\")"),
        
        create_markdown_cell("### 3. Database Selection\nDefining the target variable (**quality**) and features."),
        create_code_cell(
"""Input_wine = data_wine.drop('quality', axis=1)
Target_wine = data_wine['quality']
Input_wine.head()"""
        ),
        
        create_markdown_cell("Next we estimate the parameters by **min squares**"),
        create_code_cell(
"""from sklearn import linear_model
WineModel = linear_model.LinearRegression()
WineModel.fit(Input_wine, Target_wine)

print(\"Coefficients:\")
print(WineModel.coef_)
print(\"\\nIntercept:\")
print(WineModel.intercept_)"""
        ),
        
        create_markdown_cell("### 4. Predictions and Visualization"),
        create_code_cell(
"""PredictedQuality = WineModel.predict(Input_wine)

import matplotlib.pyplot as plt
plt.scatter(Target_wine, PredictedQuality, color='darkred', alpha=0.5)
plt.title('Scatter plot: Predicted Quality vs Actual Quality')
plt.plot([Target_wine.min(), Target_wine.max()], [Target_wine.min(), Target_wine.max()], 'k--', lw=2)
plt.xlabel('Actual Quality')
plt.ylabel('Predicted Quality')
plt.show()"""
        ),
        
        create_markdown_cell("### 5. Numerical Evaluation (R\u00b2 and MSE)"),
        create_code_cell(
"""from sklearn.metrics import mean_squared_error, r2_score
print(f'MSE (Wine) = {mean_squared_error(Target_wine, PredictedQuality):.4f}')
print(f'Explained Variance (R\u00b2) = {r2_score(Target_wine, PredictedQuality)*100:.2f}%')"""
        ),
        
        create_markdown_cell("### 6. Cross-Validation (5-Fold)\nTo get a more reliable estimate of performance on unseen data."),
        create_code_cell(
"""from sklearn.model_selection import cross_val_score, KFold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# R2 Score
r2_scores_wine = cross_val_score(WineModel, Input_wine, Target_wine, cv=kfold, scoring='r2')

# MSE Score
mse_scores_wine = -cross_val_score(WineModel, Input_wine, Target_wine, cv=kfold, scoring='neg_mean_squared_error')

print(\"Cross-Validation results (Wine):\")
print(f\"Mean R\u00b2: {r2_scores_wine.mean()*100:.2f}%\")
print(f\"R\u00b2 Standard Deviation: {r2_scores_wine.std()*100:.2f}%\")
print(f\"Mean MSE: {mse_scores_wine.mean():.4f}\")
print(f\"MSE Standard Deviation: {mse_scores_wine.std():.4f}\")"""
        )
    ]
    
    # Identify items to replace (skip until we hit "Wine Quality Results")
    end_idx = insert_idx
    for i in range(insert_idx, len(nb['cells'])):
        if "Wine Quality Results and Infographic" in "".join(nb['cells'][i].get('source', [])):
            end_idx = i
            break
    
    # Replace the old wine analysis with the new full workflow
    nb['cells'] = nb['cells'][:insert_idx] + wine_full_workflow + nb['cells'][end_idx:]

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Expanded Wine section to include Coefs and Scatter plot to match Car dataset.")
