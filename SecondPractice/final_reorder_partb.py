import json

def create_markdown_cell(source):
    if isinstance(source, list):
         source = [line + "\n" if not line.endswith("\n") else line for line in source]
    else:
         source = [line + "\n" if not line.endswith("\n") else line for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Identify and extract all special reporting blocks
auto_report = None
wine_report = None
auto_eval = None
wine_eval = None
auto_weights = None
wine_weights = None
auto_rels = None
wine_rels = None

cleaned_cells = []
for cell in nb['cells']:
    src = "".join(cell.get('source', [])).lower()
    
    # Auto
    if "executive report: strategic car price analysis" in src:
         auto_report = cell; continue
    if "automobile model evaluation" in src:
         auto_eval = cell; continue
    if "automobile weight interpretation" in src:
         auto_weights = cell; continue
    if "relationship analysis (automobile)" in src:
         auto_rels = cell; continue
         
    # Wine
    if "chemical signatures of wine quality" in src:
         wine_report = cell; continue
    if "adaptive k selection" in src or "evaluating the model results (cross-validation)" in src:
         wine_eval = cell; continue
    if "wine weight interpretation" in src:
         wine_weights = cell; continue
    if "relationship analysis (wine)" in src or "internal correlations and feature analysis" in src:
         wine_rels = cell; continue
         
    cleaned_cells.append(cell)

nb['cells'] = cleaned_cells

# 2. DEFINITIVE RE-INSERTION PLAN

def insert_after(cells, marker, to_insert):
    if to_insert is None: return False
    for i, cell in enumerate(cells):
        src = "".join(cell.get('source', [])).lower()
        if marker.lower() in src:
             cells.insert(i+1, to_insert)
             return True
    return False

# Automobile Logic (Part A)
# Scatter Matrix -> Relationship Analysis
insert_after(nb['cells'], "scatter_matrix(subset", auto_rels)
# Coefficients Display -> Weight Interpretation
insert_after(nb['cells'], "carprice.fit", auto_weights)
# Cross-Validation Output -> Evaluation Exercises
insert_after(nb['cells'], "cross_val_score(model", auto_eval)

# Report and Infographic for Automobile (User wants it JUST BEFORE PART B)
idx_part_b = -1
for i, cell in enumerate(nb['cells']):
    if "wine quality analysis" in "".join(cell.get('source', [])).lower():
         idx_part_b = i
         break

if idx_part_b != -1 and auto_report:
    nb['cells'].insert(idx_part_b, auto_report)

# Wine Logic (Part B)
# Scatter Matrix -> Relationship Analysis
insert_after(nb['cells'], "scatter_matrix(subset_wine", wine_rels)
# Coefficients Display -> Weight Interpretation
# Finding the wine coef plot specifically
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "coefs.plot" in src and "wine" in src:
         if wine_weights:
             nb['cells'].insert(i+1, wine_weights)
         break

# CV Results -> Evaluation Theory
insert_after(nb['cells'], "cross_val_score(winemodel", wine_eval)

# Final Wine Report (User wants before Appendix)
idx_appendix = -1
for i, cell in enumerate(nb['cells']):
    if "## appendix" in "".join(cell.get('source', [])).lower():
         idx_appendix = i
         break

if idx_appendix != -1 and wine_report:
    nb['cells'].insert(idx_appendix, wine_report)
elif wine_report:
    nb['cells'].append(wine_report)

# If any still missing from sequence, insert at end or before appendix
leftover = [auto_rels, auto_weights, auto_eval, auto_report, wine_rels, wine_weights, wine_eval, wine_report]
for item in leftover:
    if item and item not in nb['cells']:
         # This shouldn't happen with correct markers, but for safety:
         if "## appendix" in "".join(nb['cells'][-1].get('source', [])).lower():
              nb['cells'].insert(len(nb['cells'])-1, item)
         else:
              nb['cells'].append(item)

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Synchronized order and content. Move Automobile Report/Infographic before Wine Section.")
