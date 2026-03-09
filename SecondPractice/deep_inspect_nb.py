import json

def analyze_nb():
    with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    print(f"Total cells: {len(nb['cells'])}")
    for i, cell in enumerate(nb['cells']):
        src = "".join(cell.get('source', [])).strip()
        if cell['cell_type'] == 'markdown':
            # Summarize markdown content
            print(f"Cell {i} (MD): {src[:100]}...")
            if "Executive Report" in src:
                 print(f"   >>> FOUND EXECUTIVE REPORT in Cell {i}")
            if "Infographic" in src:
                 print(f"   >>> FOUND INFOGRAPHIC term in Cell {i}")
            if "prompt" in src.lower():
                 print(f"   >>> FOUND PROMPT term in Cell {i}")
            if "unnamed" in src:
                 print(f"   >>> FOUND IMAGE REFERENCE in Cell {i}")
        else:
            # Code cell summary
            print(f"Cell {i} (Code): {src[:60]}...")

analyze_nb()
