import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in [60, 61, 62, 63]:
    if i < len(nb['cells']):
        print(f"--- Cell {i} ---")
        print("".join(nb['cells'][i].get('source', [])))
        print("-" * 30)
