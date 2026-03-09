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

# 1. Delete cells 73 to 85
# NOTE: pop(73) 13 times (73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85)
# That's 13 cells.
for _ in range(13):
    if len(nb['cells']) > 73:
        nb['cells'].pop(73)

# 2. Find where the Wine analysis ends to insert the new Visualizations
# It ends after "MSE (Wine) = ..." which was around cell 70 before deletion.
# After deletion of middle cells, let's find it again.
target_idx = -1
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    if "MSE (Wine) =" in src:
        target_idx = i + 1
        break

if target_idx != -1:
    new_visualizations = [
        create_markdown_cell("### 7. Feature Relationships and Coefficients Analysis\nSimilarly to the automobile study, we look at the internal correlations and the impact of each feature on quality."),
        
        # Scatter Matrix
        create_markdown_cell("#### 7.1. Scatter Matrix of selected features\nWe select a subset of features: `fixed acidity`, `volatile acidity`, `citric acid`, `alcohol`, and `quality` to see how they relate to each other."),
        create_code_cell(
"""from pandas.plotting import scatter_matrix
subset_wine = data_wine[['fixed acidity', 'volatile acidity', 'citric acid', 'alcohol', 'quality']]
scatter_matrix(subset_wine, alpha=0.5, figsize=(12, 12), diagonal='hist')
plt.show()"""
        ),
        
        # Coefficients Visualization
        create_markdown_cell("#### 7.2. Model Coefficients\nBy visualizing the coefficients, we can see which variables have the most weight in predicting quality."),
        create_code_cell(
"""import pandas as pd
import matplotlib.pyplot as plt

# Get coefficients and feature names
coefs = pd.DataFrame(WineModel.coef_, index=Input_wine.columns, columns=['Coefficient'])
coefs = coefs.sort_values(by='Coefficient', ascending=False)

# Plot
coefs.plot(kind='barh', figsize=(10, 6), color='darkred')
plt.title('Linear Regression Coefficients for Wine Quality')
plt.axvline(x=0, color='black', linestyle='-')
plt.xlabel('Coefficient Value')
plt.show()

print(\"Numerical Coefficients:\")
print(coefs)"""
        )
    ]
    nb['cells'] = nb['cells'][:target_idx] + new_visualizations + nb['cells'][target_idx:]

# 3. Refine Infographic Prompt and Executive Report for Wine
for cell in nb['cells']:
    src = "".join(cell.get('source', [])).lower()
    
    # Update Wine Executive Report
    if "executive report: wine quality sensory analysis" in src:
        cell['source'] = create_markdown_cell(
"""## Wine Quality Results and Infographic

**Executive Report: Red Wine Quality Structural Analysis**

**Methodological Summary and Results:**
The Red Wine Quality analysis reveals a significantly more complex modeling challenge compared to the industrial Automobile dataset. While car prices follow strong linear relationships with physical dimensions and power, wine quality relies on a delicate balance of 11 physicochemical laboratory tests. Our Linear Regression model, validated with 5-Fold Cross-Validation, achieved a **Mean R\u00b2 of 34.24%** and a **Mean MSE of 0.43**. The visualizations clearly show that 'Alcohol' and 'Sulphates' are the primary positive drivers, while 'Volatile Acidity' acts as a strong negative indicator. However, the scatter matrix and the moderate R\u00b2 highlight that the linear mapping is insufficient to capture the subtle, non-linear chemical thresholds that define premium wines (scores 7-8) versus average ones (5-6).

**Strategic Recommendation:**
To move beyond a baseline 'flavor profile' predictor, we propose a transition to **Classification-based models (Random Forest or Gradient Boosting)**. The current project proves that chemistry can explain approximately one-third of the quality variance on a linear scale; a non-linear approach would likely capture another 20-30% of the variance by accounting for interaction effects between acidity levels and alcohol content. Future deployments should also prioritize addressing the class imbalance, as the model currently over-fits the high-frequency 'middle-tier' wines.

**Infographic Specification: Decanting Data - Red Wine Quality**
**Comprehensive Prompt for Image Generation:**
> \"Design a professional, high-density scientific infographic titled 'Decanting Data: Chemical Signatures of Wine Quality'. 
**Include these visual modules:**
1. **The Laboratory Source:** Representing the Red Wine Quality dataset with icons for pH meters, beakers, and sensory tasting panels.
2. **Correlation Grid:** A stylized 'Scatter Matrix' showing the messy but present relationships between alcohol, acidity, and quality.
3. **Weight Factors:** A bar chart showing the impact weights (Alcohol (+), Volatile Acidity (-)). 
4. **Validation Seal:** A '5-Fold Cross-Validation' icon with the metrics 'Mean MSE: 0.43' and 'R\u00b2: 34.24%'.
**Aesthetic:** Elegant Bordeaux and Deep Sage color scheme on a professional cream parchment background. Modern data-journalism style similar to 'The Economist' or 'Scientific American'.\"

[NEW INFOGRAPHIC PLACEHOLDER]"""
        )['source']

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Deleted cells 73-85, added wine visualizations, and refined reporting.")
