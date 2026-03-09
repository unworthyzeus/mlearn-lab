import json

with open('OGSecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb_og = json.load(f)

for i in range(59, len(nb_og['cells'])):
    cell = nb_og['cells'][i]
    src = "".join(cell.get('source', [])).strip().replace("\n", " ")
    print(f"Cell {i} ({cell['cell_type']}): {src[:120]}")
