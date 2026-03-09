import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', [])).lower()
    if 'repeat the practice' in source:
        print(f"Cell {i} (contains 'repeat the practice'): {source[:80].strip()}")
    if 'executive report: automobile' in source:
        print(f"Cell {i} (contains 'Automobile report')")
