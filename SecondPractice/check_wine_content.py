import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

wine_report_found = False
for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', [])).lower()
    if 'executive report' in source and 'wine' in source:
        wine_report_found = True
        print(f"Cell {i}: Found Wine Executive Report")
    if 'prompt' in source and 'wine' in source:
        print(f"Cell {i}: Found Wine Prompt/Infographic info")

if not wine_report_found: print("Wine Executive Report NOT found")
