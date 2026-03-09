import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" if not line.endswith("\n") else line for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Collect all special purpose cells for both sections
auto_internal_ex = None
auto_weights_ex = None
auto_eval_ex = None
auto_report = None

wine_internal_ex = None
wine_weights_ex = None
wine_eval_ex = None
wine_report = None

# Identify and remove these cells from their current positions
# (We'll re-insert them exactly where they belong)
cleaned_cells = []
for cell in nb['cells']:
    src = "".join(cell.get('source', [])).lower()
    
    # Automobile identification
    if "automobile" in src or "price" in src or "car" in src:
         if "internal correlations" in src or "relationship analysis (automobile)" in src:
              auto_internal_ex = cell
              continue
         if "model weight interpretation (automobile)" in src:
              auto_weights_ex = cell
              continue
         if "automobile model evaluation" in src:
              auto_eval_ex = cell
              continue
         if "executive report: strategic car price analysis" in src:
              auto_report = cell
              continue
    
    # Wine identification
    if "wine" in src:
         if "internal correlations and feature analysis" in src or "relationship analysis (wine)" in src:
              wine_internal_ex = cell
              continue
         if "model weight interpretation (wine)" in src:
              wine_weights_ex = cell
              continue
         if "evaluation theory (adaptive k selection)" in src or "evaluating the model results (cross-validation)" in src:
              wine_eval_ex = cell
              continue
         if "executive report: red wine quality structural analysis" in src:
              wine_report = cell
              continue
    
    cleaned_cells.append(cell)

nb['cells'] = cleaned_cells

# Re-insertion plan:
def insert_after(nb_cells, marker_src, cell_to_insert):
    for i, cell in enumerate(nb_cells):
        if marker_src.lower() in "".join(cell.get('source', [])).lower():
            nb_cells.insert(i + 1, cell_to_insert)
            return True
    return False

# Automobile inserts
insert_after(nb['cells'], "scatter_matrix(subset", auto_internal_ex) # If found
insert_after(nb['cells'], "carprice.fit", auto_weights_ex) # After fit/coeff display
insert_after(nb['cells'], "cross_val_score(model", auto_eval_ex) 
insert_after(nb['cells'], "automobile model evaluation", auto_report)

# Wine inserts
insert_after(nb['cells'], "scatter_matrix(subset_wine", wine_internal_ex)
insert_after(nb['cells'], "winemodel.fit", wine_weights_ex)
insert_after(nb['cells'], "cross_val_score(winemodel", wine_eval_ex)
insert_after(nb['cells'], "evaluation theory (adaptive k selection)", wine_report)

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Final Reordering and Content Synchronization finished for both sections.")
