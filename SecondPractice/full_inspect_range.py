import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in range(50, 75):
    if i >= len(nb['cells']): break
    cell = nb['cells'][i]
    src = "".join(cell.get('source', []))
    print(f"--- Cell {i} ({cell.get('cell_type')}) ---")
    print(src)
    print("-" * 50)
