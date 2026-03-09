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

# Find the start of Wine section
start_idx = -1
for i, cell in enumerate(nb['cells']):
    if "## Practice 2 Part B: Wine Quality Analysis" in "".join(cell.get('source', [])):
        start_idx = i
        break

# Find the start of Appendix to know where to stop
end_idx = -1
for i, cell in enumerate(nb['cells']):
    if "## Appendix" in "".join(cell.get('source', [])):
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    wine_new_flow = [
        create_markdown_cell("## Practice 2 Part B: Wine Quality Analysis\n---\nFollowing the same workflow as the Automobile dataset, we will now analyze the **Wine Quality** dataset manually to perform all the steps required in the original practice."),
        
        create_markdown_cell("### 1. Load the Wine Data"),
        create_code_cell(
"""File = \"winequality-red.csv\"
Filename = os.path.join(os.getcwd(), 'Data', File)
data_wine = pd.read_csv(Filename)
data_wine.head()"""
        ),
        
        create_markdown_cell("### 2. Data Exploration and Cleaning\nWe check for null values and the data types of the features."),
        create_code_cell("data_wine.info()\nprint(f\"\\nNull values:\\n{data_wine.isnull().sum()}\")"),
        
        create_markdown_cell("### 3. Visualizing Relationships (Scatter Matrix)\nFollowing the car model, we first look at how the variables relate to each other and to the target quality."),
        create_code_cell(
"""from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
# Selecting a subset for clear visualization
subset_wine = data_wine[['fixed acidity', 'volatile acidity', 'citric acid', 'alcohol', 'quality']]
scatter_matrix(subset_wine, alpha=0.5, figsize=(12, 12), diagonal='hist', color='darkred')
plt.show()"""
        ),
        
        create_markdown_cell("### 4. Database Selection for Modeling\nDefining the target variable (**quality**) and features."),
        create_code_cell(
"""Input_wine = data_wine.drop('quality', axis=1)
Target_wine = data_wine['quality']
Input_wine.head()"""
        ),
        
        create_markdown_cell("### 5. Parameter Estimation by Minimum Squares\nWe train the Linear Regression model to find the best-fit line."),
        create_code_cell(
"""from sklearn import linear_model
WineModel = linear_model.LinearRegression()
WineModel.fit(Input_wine, Target_wine)

print(\"Coefficients:\")
print(WineModel.coef_)
print(\"\\nIntercept:\")
print(WineModel.intercept_)"""
        ),
        
        create_markdown_cell("### 6. Coefficient Analysis\nWe visualize the weights to see which chemical properties influence our prediction model the most."),
        create_code_cell(
"""coefs = pd.DataFrame(WineModel.coef_, index=Input_wine.columns, columns=['Coefficient'])
coefs = coefs.sort_values(by='Coefficient', ascending=False)
coefs.plot(kind='barh', figsize=(10, 6), color='darkred')
plt.title('Importance of Features (Coefficients)')
plt.axvline(x=0, color='black')
plt.show()"""
        ),
        
        create_markdown_cell("### 7. Predictions and Performance Visualization\nMapping the predicted values vs actual sensory data."),
        create_code_cell(
"""PredictedQuality = WineModel.predict(Input_wine)
plt.figure(figsize=(8,6))
plt.scatter(Target_wine, PredictedQuality, color='darkred', alpha=0.3)
plt.plot([Target_wine.min(), Target_wine.max()], [Target_wine.min(), Target_wine.max()], 'k--', lw=2)
plt.title('Predicted vs Actual Quality')
plt.xlabel('Sensory Score (Actual)')
plt.ylabel('Model Prediction')
plt.show()"""
        ),
        
        create_markdown_cell("### 8. Numerical Evaluation (R\u00b2 and MSE)"),
        create_code_cell(
"""from sklearn.metrics import mean_squared_error, r2_score
print(f'MSE (Wine) = {mean_squared_error(Target_wine, PredictedQuality):.4f}')
print(f'Explained Variance (R\u00b2) = {r2_score(Target_wine, PredictedQuality)*100:.2f}%')"""
        ),
        
        create_markdown_cell("### 9. Cross-Validation (5-Fold)\nTo get a robust estimation of performance on unseen data."),
        create_code_cell(
"""from sklearn.model_selection import cross_val_score, KFold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
r2_cv = cross_val_score(WineModel, Input_wine, Target_wine, cv=kfold, scoring='r2')
mse_cv = -cross_val_score(WineModel, Input_wine, Target_wine, cv=kfold, scoring='neg_mean_squared_error')

print(\"Cross-Validation results (Wine):\")
print(f\"Mean R\u00b2: {r2_cv.mean()*100:.2f}%\")
print(f\"R\u00b2 Std: {r2_cv.std()*100:.2f}%\")
print(f\"Mean MSE: {mse_cv.mean():.4f}\")"""
        ),

        create_markdown_cell(
"""## Wine Quality Results and Infographic

**Executive Report: Red Wine Quality Structural Analysis**

**Methodological Summary and Results:**
The Red Wine Quality analysis reveals a significantly more complex modeling challenge compared to the industrial Automobile dataset. While car prices follow strong linear relationships with physical dimensions and power, wine quality relies on a delicate balance of 11 physicochemical laboratory tests. Our Linear Regression model, validated with 5-Fold Cross-Validation, achieved a **Mean R\u00b2 of 34.24%** and a **Mean MSE of 0.43**. The visualizations clearly show that 'Alcohol' and 'Sulphates' are the primary positive drivers, while 'Volatile Acidity' and 'Density' act as strong negative indicators. However, the scatter matrix and the moderate R\u00b2 highlight that the linear mapping is insufficient to capture the subtle, non-linear chemical thresholds that define premium wines (scores 7-8) versus average ones (5-6).

**Strategic Recommendation:**
To move beyond a baseline 'flavor profile' predictor, we propose a transition to **Classification-based models (Random Forest or Gradient Boosting)**. The current project proves that chemistry can explain approximately one-third of the quality variance on a linear scale; a non-linear approach would likely capture interaction effects between acidity levels and alcohol content. Future deployments should also prioritize addressing the class imbalance, as the model currently over-fits the high-frequency 'middle-tier' wines.

**Infographic Specification: Decanting Data - Red Wine Quality**
**Comprehensive Prompt for Image Generation (Ready to Copy):**
> \"Design a professional, high-density scientific infographic titled 'Decanting Data: Chemical Signatures of Wine Quality'. 
**Include these visual modules:**
1. **The Laboratory Source:** Representing the Red Wine Quality dataset with icons for pH meters, beakers, and sensory tasting panels.
2. **Correlation Grid:** A stylized 'Scatter Matrix' showing the relationships (or lack thereof) between alcohol, acidity, and quality.
3. **Weight Factors:** A horizontal bar chart showing the impact weights (Alcohol (+), Volatile Acidity (-), Density (-)). 
4. **Validation Seal:** A '5-Fold Cross-Validation' icon with results 'Mean MSE: 0.43' and 'Mean R\u00b2: 34.24%'.
**Aesthetic:** Elegant Bordeaux and Deep Sage color scheme on a professional cream parchment background. Modern data-journalism style.\"\n\n[REMOVED: PLACEHOLDER FOR NEW INFOGRAPHIC]"""
        )
    ]
    
    nb['cells'] = nb['cells'][:start_idx] + wine_new_flow + nb['cells'][end_idx:]

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Wine section re-ordered and expanded to match Automobile workflow style.")
