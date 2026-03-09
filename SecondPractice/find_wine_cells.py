import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', [])).lower()
    if 'wine' in source:
        print(f"Cell {i} (contains 'wine'): {source[:80].strip()}")
