import json

def create_markdown_cell(source):
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in source.strip().split("\n")]}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

new_cells = []
i = 0
found_auto_exercise = False

while i < len(nb['cells']):
    cell = nb['cells'][i]
    source = "".join(cell.get('source', [])).lower()
    
    # Identify the Automobile exercise area
    if not found_auto_exercise and ("create an infographic for the work done" in source or "cross validation provides a more accurate estimate" in source):
        found_auto_exercise = True
        
        # 1. THE QUESTIONS for Automobile
        questions = create_markdown_cell(
"""### **Exercises: Automobile Model Evaluation**
1. <font color='red'>**Cross-validation Comparison:** Explain in words, why the cross validation provides a more accurate estimate of what happens with unseen data.</font>
2. <font color='red'>**Confidence Margin:** Explain in words, the usefulness of having a confidence margin.</font>
3. <font color='red'>**Infographic:** Create an infographic of the work done using NotebookLM or similar tool. Refine the prompt for clarity.</font>
4. <font color='red'>**Executive Report:** Write a short assessment of the work done (Difficulties, challenges, and proposals for a solution).</font>"""
        )
        new_cells.append(questions)
        
        # 2. THE ANSWERS (Infographic + Report) for Automobile
        auto_results = create_markdown_cell(
"""## Results Context: Automobile Price Prediction (BDCars)

---

### **Interpretation of Model Performance**
**1. Cross-validation for accurate estimates:**  
Cross-validation trains and evaluates the model on multiple different subsets of the data (folds), instead of relying on a single train-test split. This reduces the variance in the performance metric, preventing the score from being artificially high or low due to a 'lucky' or 'unlucky' split, thus providing an unbiased and more reliable estimate of the model's true performance on unseen data.  

**2. Usefulness of a confidence margin:**  
A confidence margin (standard deviation of the R² across folds) tells us how stable the model's performance is. A high variance means the model is sensitive to specific data samples. Knowing these bounds allows decision-makers to set realistic expectations and trust the predictions within a known range of error.

---

### **Automobile Price Prediction: Infographic Outline**
**Prompt to generate the Automobile Infographic:**
> "I built a machine learning model to predict car prices using the Automobile (BDCars) dataset. I cleaned the data and trained a Linear Regression model validated with 5-Fold Cross-Validation (Mean R² ≈ 71.1%). Create a professional data science infographic outline that shows: (1) the problem (predicting car price), (2) the technique (Regression + Cross-Val), and (3) the results (R² ~71% is a solid baseline). Style: Modern, clean, dark theme with blue and white accents, vector art."

<img src="unnamed (1).png" width="80%">

---

### **Executive Report: Automobile Car Price Prediction**

**Methodological Summary and Results:**
A Linear Regression model was implemented to predict car retail prices using the **BDCars.csv** dataset. After addressing data quality issues (handling missing values and basic encoding), the model achieved a cross-validated R² of **~71.1%**. This indicates a strong positive correlation, where the model successfully explains over 70% of the price variance, serving as a robust first baseline for the pricing engine.

**Roadmap for Performance Enhancement:**
The primary challenge was handling high-cardinality categorical variables (like car make/model) with basic encoding. To reach production-level accuracy (>85%), we recommend:
1. **Advanced Feature Engineering:** Replacing label encoding with Target Encoding or One-Hot encoding for nominal features.
2. **Non-Linear Models:** Testing Random Forests or Gradient Boosting, which are better at capturing non-linear pricing plateaus.
3. **Scaling & Outliers:** Standardizing numeric features and removing extreme price outliers to stabilize regression weights."""
        )
        new_cells.append(auto_results)
        
        # Skip until we hit the Wine section instruction
        while i < len(nb['cells']):
            next_src = "".join(nb['cells'][i].get('source', [])).lower()
            if "repeat the practice with the database wine quality" in next_src:
                break
            i += 1
        # The loop will advance normally after this if-block
        if i >= len(nb['cells']):
            break
        # Process the Wine instruction cell now
        cell = nb['cells'][i]
        source = "".join(cell.get('source', []))
        # Keep the instruction but maybe clean the results part from it
        q_part = source.split("---")[0] if "---" in source else source
        new_cells.append(create_markdown_cell(q_part))
        i += 1
        continue

    new_cells.append(cell)
    i += 1

nb['cells'] = new_cells

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Final cleanup of Automobile reports and results.")
