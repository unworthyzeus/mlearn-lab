import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in range(50, 70):
    if i >= len(nb['cells']): break
    cell = nb['cells'][i]
    if cell['cell_type'] == 'markdown':
        src = "".join(cell.get('source', []))
        if any(kw in src.lower() for kw in ['executive', 'infographic', 'automobile', 'prompt']):
            print(f"--- Cell {i} ---")
            print(src)
            print("-" * 50)
