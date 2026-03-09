import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update Automobile Cross-Validation Code (K=5)
# I'll search for the Automobile CV block.
for cell in nb['cells']:
    src = "".join(cell.get('source', []))
    if "cross_val_score(model, X_filt, y_filt" in src or "cross_val_score(CarPrice" in src:
        # Update K
        cell['source'] = [line.replace("n_splits=5", "n_splits=5") for line in cell['source']] # Keep 5 or change to 10? 
        # Actually I'll change Auto to 5 and Wine to 10.
        pass

# 2. Update Wine Cross-Validation Code (K=10)
for cell in nb['cells']:
    src = "".join(cell.get('source', []))
    if "kfold = KFold(n_splits=5, shuffle=True, random_state=42)" in src and "WineModel" in src:
        cell['source'] = [line.replace("n_splits=5", "n_splits=10") for line in cell['source']]

# 3. Update the theory cells
for cell in nb['cells']:
    src = "".join(cell.get('source', []))
    if "Selection of 'K':" in src:
        is_wine = "wine" in src.lower()
        if is_wine:
             cell['source'] = create_markdown_cell(
"""1. <font color='red'>**Cross-validation Comparison:** Explain in words, why the cross validation provides a more accurate estimate of what happens with unseen data.</font>
**Answer:** Cross-validation ensures that every data point is used for testing across different iterations, preventing overfitting to a specific training subset. By averaging performance across multiple folds, we get a realistic expectation of model performance.

**Selection of 'K' (Adaptive K):** We have chosen different K-values based on sample size:
- **For Wine Quality (~1,600 samples):** We use **$k=10$**. With a larger dataset, $k=10$ provides a more fine-grained estimation of model variance and performance without losing too much training data per fold (~160 samples per test fold).
- **For Automobile (~200 samples):** We use **$k=5$**. In smaller datasets, using a higher K can lead to very small testing folds (e.g., only 20 samples per fold), which may lead to high variance in the results. $k=5$ (~40 samples per fold) provides a more stable evaluation for this scale."""
             )['source']
        else:
             # Look for automobile one if it exists separately
             pass

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Updated Wine K to 10 and Auto K to 5, with sample-size justification.")
