import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', [])).lower()
    if 'wine' in source and 'assessment' in source:
        print(f"Cell {i}: Wine assessment area")
    if 'wine' in source and 'infographic' in source:
        print(f"Cell {i}: Wine infographic area")
    if 'wine' in source and 'prompt' in source:
        print(f"Cell {i}: Wine prompt area")
