import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in range(40, 75):
    if i >= len(nb['cells']): break
    cell = nb['cells'][i]
    content = "".join(cell.get('source', [])).replace("\n", " ")[:120]
    print(f"Cell {i} ({cell['cell_type']}): {content}")
