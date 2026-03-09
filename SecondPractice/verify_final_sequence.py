import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in range(55, len(nb['cells'])):
    cell = nb['cells'][i]
    src = "".join(cell.get('source', [])).strip().replace("\n", " ")[:100]
    print(f"Cell {i} ({cell['cell_type']}): {src}")
