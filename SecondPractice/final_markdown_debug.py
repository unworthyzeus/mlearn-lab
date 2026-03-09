import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        src = "".join(cell.get('source', []))
        if "Exercise" in src or "Report" in src:
            print(f"--- Cell {i} ---")
            print(src)
            print("-" * 30)
