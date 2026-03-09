import json

def create_markdown_cell(source):
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in source.strip().split("\n")]}

def create_code_cell(source):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [line + "\n" for line in source.strip().split("\n")]}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update Wine Step 6 Code
target_wine_code = "print(f\"Mean R\u00b2: {r2_scores_wine.mean()*100:.2f}%\")"
found_wine_code = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and any(target_wine_code in line for line in cell.get('source', [])):
        cell['source'] = [
            "from sklearn.model_selection import cross_val_score, KFold\n",
            "kfold = KFold(n_splits=5, shuffle=True, random_state=42)\n",
            "\n",
            "# R2 Score\n",
            "r2_scores_wine = cross_val_score(model_wine, X_wine, y_wine, cv=kfold, scoring='r2')\n",
            "\n",
            "# MSE Score\n",
            "mse_scores_wine = -cross_val_score(model_wine, X_wine, y_wine, cv=kfold, scoring='neg_mean_squared_error')\n",
            "\n",
            "print(\"Cross-Validation results (Wine):\")\n",
            "print(f\"Mean R\u00b2: {r2_scores_wine.mean()*100:.2f}%\")\n",
            "print(f\"R\u00b2 Standard Deviation: {r2_scores_wine.std()*100:.2f}%\")\n",
            "print(f\"Mean MSE: {mse_scores_wine.mean():.4f}\")\n",
            "print(f\"MSE Standard Deviation: {mse_scores_wine.std():.4f}\")\n"
        ]
        found_wine_code = True
        break

# 2. Improve Infographic Prompts
# I'll update the Results Context cells (Car and Wine)
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        src = "".join(cell['source']).lower()
        
        # Update Automobile Prompt
        if "prompt to generate the automobile infographic" in src:
            cell['source'] = create_markdown_cell(
"""### **Automobile Price Prediction: Comprehensive Infographic Prompt**
**Prompt to generate the Automobile Infographic:**
> "Create a high-end, professional data science infographic for a car price prediction project using the 'BDCars' dataset. 
**Process steps to include:** 
1. **Data Cleaning:** Handling missing values ('?') in the price column and encoding categorical features like 'make' and 'body-style'.
2. **Phase 1 (The Model):** Using a Linear Regression algorithm.
3. **Phase 2 (Validation):** Implementing 5-Fold Cross-Validation for stability.
4. **Results:** Achievement of a robust Mean R² score (Highlight approx 81% or 72% based on your specific run).
**Visual Style:** Modern, tech-focused aesthetic with flat vector illustrations of cars and bar charts. Use a professional color palette like Deep Navy, Slate Grey, and Accent Cyan. Ensure the title 'Automobile Pricing Engine' is prominent."

<img src="unnamed (1).png" width="80%">"""
            )['source']

        # Update Wine Prompt
        if "prompt to generate the wine quality infographic" in src:
             cell['source'] = create_markdown_cell(
"""### **Wine Quality Prediction: Comprehensive Infographic Prompt**
**Prompt to generate the Wine Quality Infographic:**
> "Create a sophisticated, minimalist infographic titled 'Decanting Data: Red Wine Quality Prediction'. 
**Key Narrative points:**
1. **Objective:** Mapping 11 physicochemical laboratory tests (pH, Alcohol, Acidity) to subjective human sensory scores (0-10).
2. **Technique:** Linear Regression model validated with 5-Fold Cross-Validation.
3. **The Challenge:** Highlighting that wine quality is hard to predict linearly (R² ≈ 34.24%). 
4. **Metrics:** Display prominently: Mean MSE = 0.43 and R² = 34.24%.
**Visual Style:** Elegant, wine-themed color palette (Bordeaux Red, Soft Cream, Charcoal). Use clean icons for laboratory beakers, wine glasses, and mathematical formulas. Professional and academic look."

<img src="unnamed (2).png" width="80%">"""
             )['source']

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print(f"Updated Wine code (found: {found_wine_code}) and improved prompts.")
