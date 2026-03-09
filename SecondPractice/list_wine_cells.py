import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).strip().replace("\n", " ").lower()
    if 'wine' in src or 'automobile' in src or 'price' in src or 'quality' in src:
        print(f"Cell {i} ({cell['cell_type']}): {src[:100]}")
