import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', []))
    if "Create an infographic for the work done" in source:
        print(f"Cell index: {i}")
        print("Source:")
        print(source)
    if "1. Explain in words, why the cross validation" in source:
        print(f"Cell index: {i}")
        print("Source:")
        print(source)
