import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in range(55, 75):
    if i >= len(nb['cells']): break
    cell = nb['cells'][i]
    source = "".join(cell.get('source', []))
    print(f"--- Cell {i} ({cell['cell_type']}) ---")
    print(source[:500])
    print("-" * 30)
