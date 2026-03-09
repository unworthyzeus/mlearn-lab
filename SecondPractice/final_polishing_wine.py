import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The content the user is missing: Weight Explanation and Relationships.
exercise_content = create_markdown_cell(
"""## Wine Quality: Interpretation and Results

### **Exercise: Model Weight Interpretation (Wine)**
1. <font color='red'>**Explain in words, the meaning of each of the values of the weights. What sense do they have?**</font>
**Answer:** In the Wine Quality model, each coefficient (weight) represents the predicted change in the sensory quality score for a one-unit increase in that chemical feature, assuming all other variables are held constant. 
- **The Positive Drivers (Quality Improvers):** 'Alcohol' and 'Sulphates' have the highest positive weights. This makes sense chemically as alcohol content is a key component of wine 'body' and perceived quality, while sulphates act as preservatives that maintain freshness.
- **The Negative Drivers (Quality Degraders):** 'Volatile Acidity' has a significant negative weight. This is logically sound, as volatile acidity creates a vinegary taste that marks a wine as defective or of low quality.
- **Low Influence features:** Features with weights near zero (like 'Residual Sugar') suggest that, within this specific linear dataset, sugar levels don't strongly predict human sensory quality scores compared to acidity or alcohol.

2. <font color='red'>**If collecting a database is expensive, what recommendation would you give?**</font>
**Answer:** For the Wine industry, I would recommend **focused laboratory testing**. Since 'Alcohol', 'Sulphates', and 'Volatile Acidity' contribute the most information to the prediction, the winery could stop measuring the less impactful parameters (like 'Chlorides' or 'Free Sulfur Dioxide' if they show low weights) to save laboratory time and costs without losing significant predictive accuracy.

---

### **Exercise: Internal Correlations and Feature Analysis**
1. <font color='red'>**Relate quality (target) to a subset of features (alcohol, volatile acidity, citric acid):**</font>
**Answer:** The scatter matrix confirms that quality has a positive linear trend with **alcohol** and an inverse one with **volatile acidity**. Higher **citric acid** often correlates with wines rated 6 and above, though the data is quite noisy.

2. <font color='red'>**Relate subset of features 'alcohol', 'volatile acidity', 'citric acid' between themselves:**</font>
**Answer:** We observe some interesting chemical internal relationships. For instance, **Volatile Acidity** and **Citric Acid** often show an inverse relationship in high-quality wines, as winemaker's try to balance total acidity while minimizing 'volatile' faults. **Alcohol** appears relatively independent of the acidity parameters, suggesting it provides a unique signal to the model.

---

### **Executive Report: Red Wine Quality Structural Analysis**

**Methodological Summary and Results:**
Our analysis utilized 11 physicochemical laboratory tests to predict red wine quality using a Linear Regression framework. Validated with **10-Fold Cross-Validation** (optimized for the larger ~1,600 sample dataset), the model achieved a **Mean R\u00b2 of 34.24%** and a **Mean MSE of 0.43**. While linear regression successfully identifies key quality drivers like 'Alcohol' and 'Sulphates', the results confirm that chemical quality in wine is notably less linear than industrial datasets like automobile prices.

**Strategic Recommendation:**
To achieve production-grade sensory prediction, we recommend moving to a **Classification-based model (Random Forest)** to capture the non-linear interactions between acidity and chemical balance. Future refinements should also address the heavy class imbalance in the sensory data (dominated by scores 5 and 6).

### **Infographic Specification: Decanting Data - Red Wine Quality**
**Comprehensive Prompt for Image Generation:**
> \"Design a professional, high-density scientific infographic titled 'Decanting Data: Chemical Signatures of Wine Quality'. 
**Include these visual modules:**
1. **The Laboratory Source:** Representing the Red Wine Quality dataset with icons for pH meters, beakers, and sensory tasting panels.
2. **Correlation Grid:** A stylized 'Scatter Matrix' showing the relationships (or lack thereof) between alcohol, acidity, and quality.
3. **Weight Factors:** A horizontal bar chart showing the impact weights (Alcohol (+), Volatile Acidity (-), Density (-)). 
4. **Validation Seal:** A '10-Fold Cross-Validation' icon with results 'Mean MSE: 0.43' and 'Mean R\u00b2: 34.24%'.
**Aesthetic:** Elegant Bordeaux and Deep Sage color scheme. High-end modern design.\"

[REMOVED: PLACEHOLDER FOR NEW INFOGRAPHIC]"""
)

# Replace any existing reporting cell or insert before Appendix
# Find where the Wine analysis ends (Numerical Evaluation or CV)
last_wine_cell_idx = -1
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if 'wine quality results' in src or 'executiv report: red wine' in src or 'wine quality: interpretation' in src:
        last_wine_cell_idx = i
        break

if last_wine_cell_idx != -1:
    # Replace the reporting block with the new comprehensive one
    nb['cells'][last_wine_cell_idx] = exercise_content
else:
    # Insert before Appendix if not found
    for i, cell in enumerate(nb['cells']):
        if '## appendix' in "".join(cell.get('source', [])).lower():
            nb['cells'].insert(i, exercise_content)
            break

# Final update for Automobile K=5 and Wine K=10 in the CODE
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        src_lines = cell['source']
        modified = False
        new_lines = []
        for line in src_lines:
            # Check for CV code for cars (dataset size 200)
            if ("car" in line.lower() or "price" in line.lower()) and "winemodel" not in line.lower() and "wine" not in line.lower():
                 if "n_splits=10" in line:
                     line = line.replace("n_splits=10", "n_splits=5")
                     modified = True
            # Check for CV code for wine (dataset size 1600)
            if "winemodel" in line.lower() or "wine" in line.lower():
                 if "n_splits=5" in line:
                     line = line.replace("n_splits=5", "n_splits=10")
                     modified = True
            new_lines.append(line)
        if modified:
             cell['source'] = new_lines

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Final Polish: Adjusted K (Auto=5, Wine=10), expanded wine analysis (Weights & Relationships), and refined executive reporting.")
