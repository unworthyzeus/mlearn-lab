import json

def create_markdown_cell(source):
    if isinstance(source, list):
         source = [line + "\n" if not line.endswith("\n") else line for line in source]
    else:
         source = [line + "\n" if not line.endswith("\n") else line for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Collect all special content cells
auto_weights = None
auto_relationships = None
auto_eval = None
auto_report = None

wine_weights = None
wine_relationships = None
wine_eval = None
wine_report = None

# Identify and extract
cleaned = []
for cell in nb['cells']:
    src = "".join(cell.get('source', [])).lower()
    found = False
    
    # Auto
    if "exercise: automobile weight interpretation" in src:
         auto_weights = cell; found = True
    elif "exercise: relationship analysis (automobile)" in src:
         auto_relationships = cell; found = True
    elif "exercises: automobile model evaluation" in src:
         auto_eval = cell; found = True
    elif "executive report: strategic car price analysis" in src:
         auto_report = cell; found = True
    
    # Wine
    elif "exercise: wine weight interpretation" in src:
         wine_weights = cell; found = True
    elif "exercise: internal correlations and feature analysis" in src or "relationship analysis (wine)" in src:
         wine_relationships = cell; found = True
    elif "evaluation theory (adaptive k selection)" in src or "evaluating the model results (cross-validation)" in src:
         wine_eval = cell; found = True
    elif "chemical signatures of wine quality" in src:
         wine_report = cell; found = True
    
    if not found:
        cleaned.append(cell)

nb['cells'] = cleaned

# Helper to insert
def insert_after(cells, marker, to_insert):
    if to_insert is None: return
    for i, cell in enumerate(cells):
        if marker.lower() in "".join(cell.get('source', [])).lower():
            cells.insert(i + 1, to_insert)
            return True
    return False

# Automobile Inserts
insert_after(nb['cells'], "scatter_matrix(subset", auto_relationships)
insert_after(nb['cells'], "carprice.fit", auto_weights)
insert_after(nb['cells'], "cross_val_score(model", auto_eval)
insert_after(nb['cells'], "automobile model evaluation", auto_report)

# Wine Inserts
insert_after(nb['cells'], "scatter_matrix(subset_wine", wine_relationships)
insert_after(nb['cells'], "winemodel.fit", wine_weights)
# More specifically for wine weights plot:
for i, cell in enumerate(nb['cells']):
     src = "".join(cell.get('source', [])).lower()
     if "coefs.plot" in src and "wine" in src:
          if wine_weights not in nb['cells']:
             nb['cells'].insert(i + 1, wine_weights)
          break

insert_after(nb['cells'], "cross_val_score(winemodel", wine_eval)
insert_after(nb['cells'], "evaluation theory (adaptive k selection)", wine_report)

# If any are still missing (no marker), append before appendix
idx_app = -1
for i, cell in enumerate(nb['cells']):
    if "## appendix" in "".join(cell.get('source', [])).lower():
        idx_app = i
        break
        
rest = [auto_relationships, auto_weights, auto_eval, auto_report, 
        wine_relationships, wine_weights, wine_eval, wine_report]

for item in rest:
    if item and item not in nb['cells']:
        if idx_app != -1:
            nb['cells'].insert(idx_app, item)
            idx_app += 1
        else:
            nb['cells'].append(item)

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Final Comprehensive Reordering of all Exercises and Reports to their correct context.")
