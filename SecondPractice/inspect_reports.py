import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in [61, 62, 63, 64, 65]:
    cell = nb['cells'][i]
    print(f"--- Cell {i} ---")
    print("".join(cell.get('source', [])))
