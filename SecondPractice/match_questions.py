import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', [])).lower()
    if "explain in words" in source:
        print(f"Cell {i} MATCHED CrossVal Question: {source[:100]}...")
    if "refine the prompt" in source:
        print(f"Cell {i} MATCHED Prompt Question: {source[:100]}...")
    if "write a short assessment" in source:
        print(f"Cell {i} MATCHED Assessment Question: {source[:100]}...")
