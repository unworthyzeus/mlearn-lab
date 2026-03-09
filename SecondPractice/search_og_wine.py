import json

with open('OGSecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb_og = json.load(f)

for i, cell in enumerate(nb_og['cells']):
    source = "".join(cell.get('source', [])).lower()
    if 'wine' in source:
        print(f"Cell {i} (contains 'wine'): {source[:100].strip()}")
