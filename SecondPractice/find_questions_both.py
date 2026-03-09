import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', [])).lower()
    if 'explain in words, why the cross validation' in source:
        print(f"Cell {i}: Cross-validation question")
    if 'refine the prompt' in source:
        print(f"Cell {i}: Prompt question")
    if 'write a short assessment' in source:
        print(f"Cell {i}: Assessment question")
    if 'winequality-red.csv' in source:
        print(f"Cell {i}: Wine section starts")
