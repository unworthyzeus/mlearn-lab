import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

prompt_found = False
report_found = False
crossval_ans_found = False

for i, cell in enumerate(nb['cells']):
    source = "".join(cell.get('source', []))
    if 'NotebookLM Prompt – Automobile Infographic' in source:
        prompt_found = True
        print(f"Cell {i}: Found Infographic Prompt")
    if 'Executive Report: Automobile Car Price Prediction' in source:
        report_found = True
        print(f"Cell {i}: Found Executive Report")
    if '1. Cross-validation for accurate estimates' in source:
        crossval_ans_found = True
        print(f"Cell {i}: Found Cross-validation Answer")

if not prompt_found: print("Infographic Prompt NOT found")
if not report_found: print("Executive Report NOT found")
if not crossval_ans_found: print("Cross-validation Answer NOT found")
