import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" if not line.endswith("\n") else line for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Collect
auto_internal_ex = None
auto_weights_ex = None
auto_eval_ex = None
auto_report = None

wine_internal_ex = None
wine_weights_ex = None
wine_eval_ex = None
wine_report = None

# Identify and remove
# Note: Automobile usually comes first.
cleaned_cells = []
for cell in nb['cells']:
    src = "".join(cell.get('source', [])).lower()
    found = False
    
    # Precise identification of these specific exercises/reports
    if "internal correlations" in src and "relationship analysis (automobile)" in src:
         auto_internal_ex = cell; found = True
    elif "model weight interpretation (automobile)" in src:
         auto_weights_ex = cell; found = True
    elif "automobile model evaluation" in src:
         auto_eval_ex = cell; found = True
    elif "strategic car price analysis" in src:
         auto_report = cell; found = True
    
    elif "internal correlations and feature analysis" in src or "relationship analysis (wine)" in src:
         wine_internal_ex = cell; found = True
    elif "model weight interpretation (wine)" in src:
         wine_weights_ex = cell; found = True
    elif "adaptive k selection" in src or "evaluating the model results (cross-validation)" in src:
         wine_eval_ex = cell; found = True
    elif "red wine quality structural analysis" in src:
         wine_report = cell; found = True
    
    if not found:
        cleaned_cells.append(cell)

nb['cells'] = cleaned_cells

# Re-insertion
def insert_after(nb_cells, marker_src, cell_to_insert):
    if cell_to_insert is None: return False
    for i, cell in enumerate(nb_cells):
        src = "".join(cell.get('source', [])).lower()
        if marker_src.lower() in src:
            nb_cells.insert(i + 1, cell_to_insert)
            return True
    return False

# Automobile inserts
# 1. Internal Correlations after Automobile Scatter Matrix code/header
insert_after(nb['cells'], "scatter_matrix(subset", auto_internal_ex)
# 2. Weights Meaning after fit/coefficients display
insert_after(nb['cells'], "carprice.fit", auto_weights_ex)
# 3. Model Evaluation Answers after CV code
insert_after(nb['cells'], "cross_val_score(model", auto_eval_ex)
# 4. Executive Report after Eval answers
insert_after(nb['cells'], "automobile model evaluation", auto_report)

# Wine inserts (Repeat same pattern)
insert_after(nb['cells'], "scatter_matrix(subset_wine", wine_internal_ex)
insert_after(nb['cells'], "winemodel.fit", wine_weights_ex)
insert_after(nb['cells'], "cross_val_score(winemodel", wine_eval_ex)
insert_after(nb['cells'], "evaluation theory (adaptive k selection)", wine_report)

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Synchronized order and content for both dataset sections.")
