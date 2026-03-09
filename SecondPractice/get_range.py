import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

indices = range(56, 75)
for i in indices:
    if i < len(nb['cells']):
        print(f"--- Cell {i} ---")
        src = "".join(nb['cells'][i].get('source', []))
        print(src)
        print("-" * 50)
