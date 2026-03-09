import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

indices = [60, 61, 62, 63, 64]
for i in indices:
    if i < len(nb['cells']):
        print(f"--- Cell {i} ---")
        src = "".join(nb['cells'][i].get('source', []))
        print(src)
        print("-" * 30)
