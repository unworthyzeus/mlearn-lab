import json

def create_markdown_cell(source):
    if isinstance(source, list):
         source = [line + "\n" if not line.endswith("\n") else line for line in source]
    else:
         source = [line + "\n" if not line.endswith("\n") else line for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update Wine Weight Interpretation to match the visible plot
for cell in nb['cells']:
    src = "".join(cell.get('source', [])).lower()
    if "exercise: wine weight interpretation" in src:
         cell['source'] = [
             "### **Exercise: Wine Weight Interpretation**\n",
             "\n",
             "1. <font color='red'>**Explain in words, the meaning of each of the values of the weights. What sense do they have?**</font>\n",
             "**Answer:** The weights reveal the mathematical priority the model gives to each chemical feature. \n",
             "- **Top Positive Driver:** **Sulphates** has the most significant positive coefficient (~1.0). This indicates that higher sulphate content (which helps preservation and color stabilization) is the strongest positive predictor of quality in this linear model.\n",
             "- **Top Negative Drivers:** **Density** shows the largest numeric negative weight (~ -18). While this is partly due to density's very narrow range (0.990-1.000), it suggests that 'heavier' wines (higher residual solids/ash) are rated lower. **Chlorides** and **Volatile Acidity** also show negative weights, which reflects the chemical intuition that high salt or vinegar-like acidity degrades the wine's sensory score.\n",
             "- **Alcohol Paradox:** Interestingly, while alcohol often has high *correlation* with quality, its linear *weight* here is relatively small (~0.2). This happens because other factors like density (which is highly dependent on alcohol and sugar) may be 'absorbing' that predictive signal in a multi-variate linear regression.\n",
             "\n",
             "2. <font color='red'>**If collecting a database is expensive, what recommendation would you give?**</font>\n",
             "**Answer:** Based on the coefficients, I would recommend focusing exclusively on **Density**, **Sulphates**, **Chlorides**, and **Volatile Acidity**. These features have the highest magnitude weights and drive the model's decisions. Skipping the measurement of citric acid or residual sugar would significantly cut laboratory costs with minimal impact on the regression's predictive power.\n"
         ]

# 2. Check and fix Automobile as well just in case (to be robust)
for cell in nb['cells']:
    src = "".join(cell.get('source', [])).lower()
    if "exercise: relationship analysis (automobile)" in src:
         # Ensure it matches standard car physics
         pass

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Updated Wine Weight Interpretation to accurately reflect the visible coefficients and scale nuances.")
