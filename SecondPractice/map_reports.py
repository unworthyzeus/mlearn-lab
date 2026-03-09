import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        source = "".join(cell.get('source', []))
        if 'automobile infographic' in source.lower():
            print(f"Cell {i}: Automobile Infographic Prompt")
        if 'automobile car price prediction' in source.lower():
            print(f"Cell {i}: Automobile Executive Report")
        if 'wine quality results and infographic' in source.lower():
            print(f"Cell {i}: Wine area starts header")
        if 'wine quality sensory analysis' in source.lower():
            print(f"Cell {i}: Wine Executive Report")
        if 'unnamed (1).png' in source:
            print(f"Cell {i} includes unnamed (1).png")
        if 'unnamed (2).png' in source:
            print(f"Cell {i} includes unnamed (2).png")
