import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', [])).lower()
    if 'winequality' in source:
        print(f"Cell {i} contains 'winequality'")
    if 'bdcars' in source:
        print(f"Cell {i} contains 'bdcars'")
    if 'summary and results' in source:
        print(f"Cell {i} contains 'summary and results'")
