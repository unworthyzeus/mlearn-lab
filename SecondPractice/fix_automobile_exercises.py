import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update Automobile Evaluation Section with Answers
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        src = "".join(cell.get('source', [])).lower()
        if "exercises: automobile model evaluation" in src:
            # Replace with answered version
            cell['source'] = [
                "## Exercises: Automobile Model Evaluation\n",
                "\n",
                "1. <font color='red'>**Cross-validation Comparison:** Explain in words, why the cross validation provides a more accurate estimate of what happens with unseen data.</font>\n",
                "**Answer:** Cross-validation (5-Fold) is superior to a single train/test split because it uses the entire 'BDCars' dataset for both training and validation over multiple iterations. In a small dataset (~200 cars), a single split might be unrepresentative if 'expensive' cars are all in the test set or all in the training set. By averaging performance over five folds, we ensure our R\u00b2 score reflects the model's general ability to price different types of vehicles.\n",
                "\n",
                "**Note on Selection of 'K':** For the Automobile dataset, we used **$K=5$**. With only 205 raw samples, a higher $K$ (like 10) would result in tiny test folds (~20 cars), which could lead to high variance in local results. $K=5$ (~41 cars per fold) provides a stable and statistically significant evaluation.\n",
                "\n",
                "2. <font color='red'>**Confidence Margin:** Explain in words, the usefulness of having a confidence margin.</font>\n",
                "**Answer:** The confidence margin (R\u00b2 Std Dev) quantifies the reliability of the system. For a pricing engine, an R\u00b2 of 81% is good, but if the standard deviation were very high (e.g., 20%), it would mean the model works perfectly for some brands but fails for others. A low margin of error gives us the confidence to deploy the model in a commercial setting.\n",
                "\n",
                "3. **Infographic:** [Specification and Prompt below].\n",
                "4. **Executive Report:** [Provided in the results section].\n"
            ]

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Answered Automobile evaluation exercises and justified K=5 choice.")
