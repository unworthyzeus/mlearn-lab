import json

def create_markdown_cell(source):
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in source.strip().split("\n")]}

def create_code_cell(source):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [line + "\n" for line in source.strip().split("\n")]}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The content to insert
wine_practice_cells = [
    create_markdown_cell("## Practice 2 Part B: Wine Quality Analysis\n---\nFollowing the same workflow as the Automobile dataset, we will now analyze the **Wine Quality** dataset manually to perform all the steps required in the original practice."),
    
    create_markdown_cell("### 1. Load the Wine Data"),
    create_code_cell(
"""File = "winequality-red.csv"
Filename = os.path.join(os.getcwd(), 'Data', File)
data_wine = pd.read_csv(Filename)
data_wine.head()"""
    ),
    
    create_markdown_cell("### 2. Data Exploration and Cleaning\nWe check for null values and the data types of the features."),
    create_code_cell("data_wine.info()\nprint(f\"\\nNull values:\\n{data_wine.isnull().sum()}\")"),
    
    create_markdown_cell("### 3. Model Preparation\nDefining the target variable (**quality**) and features."),
    create_code_cell(
"""X_wine = data_wine.drop('quality', axis=1)
y_wine = data_wine['quality']
X_wine.head()"""
    ),
    
    create_markdown_cell("### 4. Linear Regression Model\nTraining the model on the full dataset for initial evaluation."),
    create_code_cell(
"""from sklearn import linear_model
model_wine = linear_model.LinearRegression()
model_wine.fit(X_wine, y_wine)
predicted_wine = model_wine.predict(X_wine)"""
    ),
    
    create_markdown_cell("### 5. Evaluation (R² and MSE)"),
    create_code_cell(
"""from sklearn.metrics import mean_squared_error, r2_score
print(f'MSE (Wine) = {mean_squared_error(y_wine, predicted_wine):.4f}')
print(f'Explained Variance (R²) = {r2_score(y_wine, predicted_wine)*100:.2f}%')"""
    ),
    
    create_markdown_cell("### 6. Cross-Validation (5-Fold)\nTo get a more reliable estimate of performance on unseen data."),
    create_code_cell(
"""from sklearn.model_selection import cross_val_score, KFold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
r2_scores_wine = cross_val_score(model_wine, X_wine, y_wine, cv=kfold, scoring='r2')

print(\"Cross-Validation results (Wine):\")
print(f\"Mean R²: {r2_scores_wine.mean()*100:.2f}%\")
print(f\"R² Standard Deviation: {r2_scores_wine.std()*100:.2f}%\")"""
    ),
    
    create_markdown_cell("### 7. Wine Practice Conclusion\nFollowing the analysis above, we can now provide the executive report and infographic prompt based on these results.")
]

# Insertion point: After Automobile executive report (Cell 57) and before Wine Results (Cell 58)
insert_pos = 58 

new_cells = nb['cells'][:insert_pos] + wine_practice_cells + nb['cells'][insert_pos:]
nb['cells'] = new_cells

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Successfully inserted full Wine analysis steps between Automobile report and Wine results.")
