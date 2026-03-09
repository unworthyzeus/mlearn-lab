import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Extract the content of the exercises we need to move
internal_correlations_cell = None
weight_interpretation_cell = None

for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "### **exercise: internal correlations and feature analysis**" in src:
        internal_correlations_cell = cell
        nb['cells'][i] = None # Temporary marker
    if "### **exercise: model weight interpretation (wine)**" in src:
        weight_interpretation_cell = cell
        nb['cells'][i] = None

# Remove the marked cells
nb['cells'] = [c for c in nb['cells'] if c is not None]

# 2. Insert Internal Correlations after the Scatter Matrix
insert_idx_scatter = -1
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "scatter_matrix(" in src and "wine" in src:
        insert_idx_scatter = i + 1
        break

if insert_idx_scatter != -1 and internal_correlations_cell:
    nb['cells'].insert(insert_idx_scatter, internal_correlations_cell)

# 3. Insert Weight Interpretation after the Coefficient Bar Plot
insert_idx_weights = -1
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "coefs.plot(kind='barh'" in src and "wine" in src: # Using lower() search might be safer
        insert_idx_weights = i + 1
        # No break, find the LAST occurance or use more specific search
        
# Refined search for weight insert
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "coefs.plot" in src and "wine" in src:
         insert_idx_weights = i + 1
         break # First one is the plot

if insert_idx_weights != -1 and weight_interpretation_cell:
    nb['cells'].insert(insert_idx_weights, weight_interpretation_cell)

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Reordered Wine exercises to follow their respective visualizations.")
