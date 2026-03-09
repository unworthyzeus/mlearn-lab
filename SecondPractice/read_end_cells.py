import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in range(70, len(nb['cells'])):
    cell = nb['cells'][i]
    src = "".join(cell.get('source', []))
    print(f"--- Cell {i} ({cell['cell_type']}) ---")
    print(src)
    print("-" * 50)
