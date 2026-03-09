import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', []))
    # Using a safer way to print summary
    summary = src[:100].strip().replace("\n", " ")
    print(f"Cell {i} ({cell['cell_type']}): {summary}")
