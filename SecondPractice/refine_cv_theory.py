import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update the Cross-Validation Comparison explanation to discuss K-selection
for cell in nb['cells']:
    src = "".join(cell.get('source', []))
    if "Cross-validation Comparison:" in src and "unseen data" in src:
        # Check if it's the wine or automobile one. If find wine specific keywords, we tailor it.
        # But both can benefit from the K explanation.
        is_wine = "wine" in src.lower()
        
        k_explanation = (
            "\n**Selection of 'K':** The choice of $k=5$ (or $k=10$) is a standard balance between **bias** and **variance**. \n"
            "- **For smaller datasets like BDCars (approx 200 samples):** A smaller $k$ (like 5) is often sufficient to avoid having too few samples in each test fold.\n"
            "- **For larger datasets like Wine Quality (approx 1600 samples):** We could potentially use a higher $k$ (like 10) to get an even more precise estimate, as we have enough data to maintain statistical significance in each fold's test set. However, $k=5$ remains a robust industry baseline for comparing different models."
        )
        
        # We append/replace the answer
        if is_wine:
            cell['source'] = create_markdown_cell(
"""1. <font color='red'>**Cross-validation Comparison:** Explain in words, why the cross validation provides a more accurate estimate of what happens with unseen data.</font>
**Answer:** Cross-validation (5-Fold) ensures that every single data point is used for testing exactly once across different iterations. This prevents 'overfitting' to a specific training subset. By averaging performance across these five folds, we get a realistic expectation of how the model will perform on a completely new bottle of wine from the same region.

**Selection of 'K':** Choosing the correct $k$ involves a trade-off. For the **Wine Quality** dataset (~1,599 samples), $k=5$ provides folds of ~320 samples, which is statistically robust. In smaller datasets like the **Automobile** one (~200 samples), $k=5$ results in folds of only 40 samples; in those cases, $k=10$ or even 'Leave-One-Out' might be considered to maximize training data, though $k=5$ is a safe conservative starting point for both."""
            )['source']

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Updated K-selection theory in Cross-Validation answers.")
