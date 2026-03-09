import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("--- EXERCISE SEARCH ---")
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        src = "".join(cell.get('source', []))
        if "Explain in words" in src or "Relate" in src or "Executive Report" in src:
            print(f"Cell {i} (MD): {src[:150].strip()}...")
            # Check if answer is present
            if "Answer:" in src or "Methodological Summary" in src:
                print("   [Verified: Answer/Report present]")
            else:
                print("   [WARNING: Missing Answer/Report!]")
        if "K =" in src:
             print(f"     -> K-logic mentioned: {src[:50].strip()}...")
