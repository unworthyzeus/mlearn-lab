import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("Automobile Section Checklist:")
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if 'car' in src or 'price' in src or 'scatter' in src or 'coef' in src:
         if i < 60: # Automobile section is roughly cells 0-59
             print(f"Cell {i} ({cell['cell_type']}): {src[:100]}")
