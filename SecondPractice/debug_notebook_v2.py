import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

keywords = [
    "cross validation",
    "prompt",
    "assessment",
    "automobile",
    "wine",
    "infographic",
    "explain in words",
    "refine the prompt",
    "short assessment"
]

for i, cell in enumerate(nb['cells']):
    source_text = "".join(cell.get('source', [])).lower()
    matches = [kw for kw in keywords if kw in source_text]
    if matches:
        print(f"Cell {i} ({cell['cell_type']}): Matches: {matches}")
        print(f"  Snippet: {source_text.strip()[:100]}...")
        if "notebooklm prompt – automobile" in source_text:
            print("  --- [FOUND] AUTOMOBILE INFOGRAPHIC ---")
        if "executive report: automobile" in source_text:
            print("  --- [FOUND] AUTOMOBILE EXECUTIVE REPORT ---")
        if "executive report: wine" in source_text:
            print("  --- [FOUND] WINE EXECUTIVE REPORT ---")
        print("-" * 20)
