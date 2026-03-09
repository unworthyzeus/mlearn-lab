import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source_text = "".join(cell.get('source', [])).lower()
    if 'automobile' in source_text:
        print(f"Cell {i} ({cell.get('cell_type', 'unknown')}):")
        print(f"  Snippet: {source_text.strip()[:100]}...")
    if 'cross validation' in source_text or 'infographic' in source_text or 'report' in source_text:
        print(f"Cell {i} ({cell.get('cell_type', 'unknown')}): [Special] {source_text.strip()[:100]}...")
