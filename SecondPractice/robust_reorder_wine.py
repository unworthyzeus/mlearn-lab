import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Collect and Remove cells
internal_correlations_cell = None
weight_interpretation_cell = None

cleaned_cells = []
for cell in nb['cells']:
    src = "".join(cell.get('source', [])).lower()
    if "exercise: internal correlations and feature analysis" in src:
        internal_correlations_cell = cell
        continue
    if "exercise: model weight interpretation (wine)" in src:
        weight_interpretation_cell = cell
        continue
    cleaned_cells.append(cell)

nb['cells'] = cleaned_cells

# 2. Insert Internal Correlations (after scatter matrix)
insert_idx_scatter = -1
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    if "scatter_matrix(" in src and "Wine" in src: # Wine capital?
        insert_idx_scatter = i + 1
        # Continue to find the plot display one if present
        
# A safer way: find the scatter matrix plot code cell for Wine
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "scatter_matrix(" in src and ("wine" in src or "subset_wine" in src):
        insert_idx_scatter = i + 1
        break

if insert_idx_scatter != -1 and internal_correlations_cell:
    nb['cells'].insert(insert_idx_scatter, internal_correlations_cell)

# 3. Insert Weight Interpretation (after bar plot)
insert_idx_weights = -1
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "coefs.plot(" in src and "coefs" in src: # The wine coefs plot
        insert_idx_weights = i + 1
        break

if insert_idx_weights != -1 and weight_interpretation_cell:
    nb['cells'].insert(insert_idx_weights, weight_interpretation_cell)

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Succesfully reordered the Wine exercises.")
