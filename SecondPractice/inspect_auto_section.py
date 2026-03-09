import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("--- AUTOMOBILE SECTION (Cells 30-60) ---")
for i in range(30, 60):
    if i < len(nb['cells']):
        cell = nb['cells'][i]
        src = "".join(cell.get('source', [])).strip()
        if cell['cell_type'] == 'markdown':
             print(f"Cell {i} (MD): {src[:150]}...")
        else:
             print(f"Cell {i} (Code): {src[:60]}...")
