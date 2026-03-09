import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("CELLS CONTAINING 'scatter_matrix':")
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    if "scatter_matrix" in src:
         print(f"Cell {i} ({cell['cell_type']}): {src[:150]}...")
