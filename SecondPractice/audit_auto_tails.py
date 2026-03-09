import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Show cells 45-56 (The Automobile results area)
for i in range(45, 57):
    if i < len(nb['cells']):
        print(f"--- Cell {i} ---")
        print("".join(nb['cells'][i]['source']))
        print("-" * 50)
