import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', [])).lower()
    # Looking for pieces of the missing question
    if "cross validation" in source:
        print(f"Cell {i}: {source[:150]}")
    if "infographic" in source:
        print(f"Cell {i}: {source[:150]}")
    if "executive report" in source:
        print(f"Cell {i}: {source[:150]}")
