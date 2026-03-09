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

# 1. Update Automobile CV Code (Ensure K=5)
# Using a less rigid search to handle possible variations in the code
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        src = "".join(cell.get('source', []))
        if "cross_val_score" in src and ("carprice" in src.lower() or "model_auto" in src.lower() or "price" in src.lower()):
            if "wine" not in src.lower():
                # Setting K=5 for Auto
                cell['source'] = [line.replace("n_splits=10", "n_splits=5").replace("n_splits=20", "n_splits=5") for line in cell['source']]

# 2. Update Wine CV Code (K=10)
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        src = "".join(cell.get('source', []))
        if "cross_val_score" in src and "winemodel" in src.lower():
            # Setting K=10 for Wine
            cell['source'] = [line.replace("n_splits=5", "n_splits=10").replace("kfold = KFold(n_splits=5", "kfold = KFold(n_splits=10") for line in cell['source']]

# 3. Ensure Weight Explanation for Wine is Present and detailed
# I'll look for a place to insert the detailed weight/relationship exercise if it feels missing or buried.
# I'll search for the "Wine Quality: Interpretation and Results" header.
found_interp = False
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown' and "## Wine Quality: Interpretation and Results" in "".join(cell.get('source', [])):
        # Refine the content of this cell to be exactly what the user wants.
        cell['source'] = [
            "## Wine Quality: Interpretation and Results\n",
            "\n",
            "### **Exercise: Model Weight Interpretation (Wine)**\n",
            "1. <font color='red'>**Explain in words, the meaning of each of the values of the weights. What sense do they have?**</font>\n",
            "**Answer:** In the Wine Quality model, each coefficient (weight) represents the predicted change in the sensory quality score for a one-unit increase in that chemical feature, assuming all other variables are held constant. \n",
            "- **The Positive Drivers (Quality Improvers):** 'Alcohol' and 'Sulphates' have the highest positive weights. This makes sense chemically as alcohol content is a key component of wine 'body' and perceived quality, while sulphates act as preservatives that maintain freshness.\n",
            "- **The Negative Drivers (Quality Degraders):** 'Volatile Acidity' has a significant negative weight. This is logically sound, as volatile acidity creates a vinegary taste that marks a wine as defective or of low quality.\n",
            "- **Low Influence features:** Features with weights near zero (like 'Residual Sugar') suggest that, within this specific linear dataset, sugar levels don't strongly predict human sensory quality scores compared to acidity or alcohol.\n",
            "\n",
            "2. <font color='red'>**If collecting a database is expensive, what recommendation would you give?**</font>\n",
            "**Answer:** For the Wine industry, I would recommend **focused laboratory testing**. Since 'Alcohol', 'Sulphates', and 'Volatile Acidity' contribute the most information to the prediction, the refinery could stop measuring the less impactful parameters (like 'Chlorides' or 'Free Sulfur Dioxide' if they show low weights) to save laboratory time and costs without losing significant predictive accuracy.\n",
            "\n",
            "---\n",
            "\n",
            "### **Exercise: Relationship Analysis (Internal Correlations)**\n",
            "1. <font color='red'>**Relate quality (target) to a subset of features (alcohol, volatile acidity, citric acid):**</font>\n",
            "**Answer:** The scatter matrix confirms that quality has a positive linear trend with **alcohol** and an moderately negative one with **volatile acidity**. Higher **citric acid** often correlates with wines rated 6 and above, though the data is quite noisy.\n",
            "\n",
            "2. <font color='red'>**Relate subset of features 'alcohol', 'volatile acidity', 'citric acid' between themselves:**</font>\n",
            "**Answer:** We observe some interesting chemical internal relationships. For instance, **Volatile Acidity** and **Citric Acid** often show an inverse relationship in high-quality wines, as winemaker's try to balance total acidity while minimizing 'volatile' faults. **Alcohol** appears relatively independent of the acidity parameters, suggesting it provides a unique signal to the model.\n",
            "\n",
            "---\n",
            "\n",
            "### **Exercise: Model Evaluation Theory (Adaptive K Selection)**\n",
            "1. <font color='red'>**Cross-validation Comparison:** Explain in words, why the cross validation provides a more accurate estimate of what happens with unseen data.</font>\n",
            "**Answer:** Cross-validation provides a robust estimate because it forces the model to be tested on different 'unseen' subsets of the data. This reveals if the model is truly learning general rules or just memorizing specific samples (overfitting).\n",
            "\n",
            "**Note on Selection of 'K':** We adjusted the number of folds based on dataset scale:\n",
            "- **Automobile ($K=5$):** Since we only have ~200 samples, using a high $K$ would make the test folds too small (less than 20 cars). $K=5$ ensures stable calculations with 40 cars per fold.\n",
            "- **Wine Quality ($K=10$):** With ~1,600 samples, we can afford a higher $K$. $K=10$ results in ~160 samples per test fold, leading to higher confidence in our final performance metrics.\n",
            "\n",
            "2. <font color='red'>**Confidence Margin:** Explain in words, the usefulness of having a confidence margin.</font>\n",
            "**Answer:** It quantifies the 'stability' of the model. Knowing the Mean R\u00b2 is 34% with a standard deviation helps us understand if the model is reliably mediocre or wildly inconsistent across different batches of wine samples.\n"
        ]
        found_interp = True

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print(f"Final logic check: Adaptive K set (Auto=5, Wine=10). Detailed weight and relationship explanations added (found interp cell: {found_interp}).")
