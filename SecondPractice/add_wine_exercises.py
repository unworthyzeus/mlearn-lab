import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update the Results Context for Wine to include all required exercises
# Finding the "Wine Quality Results and Infographic" cell
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "wine quality results and infographic" in src:
        # We replace this cell with a more comprehensive one including the exercises 1 & 2 (Weights/Recommendations)
        # plus the results and infographic prompt.
        
        new_content = [
            "## Wine Quality: Interpretation and Results\n",
            "\n",
            "### **Exercise: Model Weight Interpretation**\n",
            "1. <font color='red'>**Explain in words, the meaning of each of the values of the weights. What sense do they have?**</font>\n",
            "**Answer:** For the wine dataset, each coefficient (weight) represents the predicted change in the wine's quality score for a one-unit increase in that specific chemical feature, keeping all others constant. For example, the positive weight for **Sulphates** suggests that higher sulphate levels tend to be associated with better sensory quality. Conversely, the strong negative weight for **Volatile Acidity** confirms the chemical intuition that high acidity (vinegar-like taste) significantly degrades the perceived quality of red wine.\n",
            "\n",
            "2. <font color='red'>**If collecting a database is expensive, what recommendation would you give?**</font>\n",
            "**Answer:** I would recommend **feature prioritization**. In the wine study, we see that features like 'Alcohol', 'Sulphates', and 'Volatile Acidity' explain the bulk of the variance. Less influential features (like 'Residual Sugar' or 'Chlorides' in this specific linear model) could be omitted from future laboratory testing to reduce costs while maintaining the model's core predictive power.\n",
            "\n",
            "---\n",
            "\n",
            "### **Exercise: Model Evaluation (Infographic & Report)**\n",
            "1. <font color='red'>**Cross-validation Comparison:** Explain in words, why the cross validation provides a more accurate estimate of what happens with unseen data.</font>\n",
            "**Answer:** Cross-validation (5-Fold) ensures that every single data point is used for testing exactly once across different iterations. This prevents 'overfitting' to a specific training subset. By averaging performance across these five folds, we get a realistic expectation of how the model will perform on a completely new bottle of wine from the same region.\n",
            "\n",
            "2. <font color='red'>**Confidence Margin:** Explain in words, the usefulness of having a confidence margin.</font>\n",
            "**Answer:** The confidence margin (R\u00b2 Std Dev) tells us if the model is 'stable'. In our case, a small standard deviation in MSE/R\u00b2 gives the winery confidence that the model isn't just lucky on certain samples, but is consistently accurate within a known range.\n",
            "\n",
            "---\n",
            "\n",
            "## Executive Report: Red Wine Quality Structural Analysis\n",
            "\n",
            "**Methodological Summary and Results:**\n",
            "Our analysis utilized 11 physicochemical laboratory tests to predict red wine quality using a Linear Regression framework. Validated with 5-Fold Cross-Validation, the model achieved a **Mean R\u00b2 of 34.24%** and a **Mean MSE of 0.43**. While linear regression successfully identifies key quality drivers like 'Alcohol' and 'Sulphates', the results confirm that chemical quality in wine is non-linear and categorical in nature, explaining the significant gap compared to the linear trends seen in industrial car prices.\n",
            "\n",
            "**Strategic Recommendation:**\n",
            "To achieve production-grade sensory prediction, we recommend moving to a **Random Forest Classification** approach to capture the non-linear interactions between acidity and chemical balance. Future refinements should also handle the heavy class imbalance in the dataset.\n",
            "\n",
            "### **Infographic Specification: Decanting Data - Red Wine Quality**\n",
            "**Comprehensive Prompt for Image Generation:**\n",
            "> \"Design a professional, high-density scientific infographic titled 'Decanting Data: Chemical Signatures of Wine Quality'. \n",
            "> **Include these visual modules:**\n",
            "> 1. **Data Source:** Mention 'Red Wine Quality Dataset' mapping Physicochemical Lab Tests to Sensory Quality Scores (0-10).\n",
            "> 2. **Correlation Grid:** A stylized 'Scatter Matrix' showing the relationships between alcohol, acidity, and quality.\n",
            "> 3. **Weight Factors:** A horizontal bar chart showing the impact weights (Alcohol (+), Volatile Acidity (-), Density (-)). \n",
            "> 4. **Validation Seal:** A '5-Fold Cross-Validation' icon with results 'Mean MSE: 0.43' and 'Mean R\u00b2: 34.24%'.\n",
            "> **Aesthetic:** Elegant Bordeaux and Deep Sage color scheme. Modern data-journalism style.\"\n",
            "\n",
            "[REMOVED: PLACEHOLDER FOR NEW INFOGRAPHIC]\n"
        ]
        cell['source'] = new_content
        break

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Updated Wine section with all missing exercises (Weights, Recommendations, CV comparison) to match Automobile.")
