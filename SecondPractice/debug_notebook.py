import json
import nbformat

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source_text = "".join(cell.get('source', [])).lower()
    
    # Check for keywords related to the missing sections
    if any(kw in source_text for kw in ["cross validation", "assessment", "infographic", "automobile", "wine"]):
        # Identify interesting sections
        print(f"Cell {i} ({cell['cell_type']}):")
        snippet = source_text.strip()[:150]
        print(f"  {snippet}...")
        
        # Check if the missing content is ALREADY there
        if "notebooklm prompt – automobile" in source_text:
            print("  --- FOUND AUTOMOBILE INFOGRAPHIC PROMPT ---")
        if "executive report: automobile car price prediction" in source_text:
            print("  --- FOUND AUTOMOBILE EXECUTIVE REPORT ---")
        if "executive report: wine quality prediction" in source_text:
            print("  --- FOUND WINE EXECUTIVE REPORT ---")
