import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in range(50, 85):
    if i >= len(nb['cells']): break
    cell = nb['cells'][i]
    src = "".join(cell.get('source', [])).strip().replace("\n", " ")
    print(f"Cell {i} ({cell['cell_type']}): {src[:120]}")
