import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as nfb:
    nb = json.load(nfb)

print(f"Total cells: {len(nb['cells'])}")
for i in range(60, len(nb['cells'])):
    cell = nb['cells'][i]
    src = "".join(cell.get('source', [])).strip().replace("\n", " ")
    print(f"Cell {i} ({cell.get('cell_type')}): {src[:60]}")
