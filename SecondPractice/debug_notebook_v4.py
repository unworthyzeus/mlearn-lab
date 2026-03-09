import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source_text = "".join(cell.get('source', [])).lower()
    
    # Matching for the Automobile practice questions:
    if "explain in words, why the cross validation provides a more accurate estimate" in source_text:
        print(f"Cell {i} (FOUND question 1: CrossVal)")
        # Look at the *next* block to see if it's the answer
        next_cell = nb['cells'][i+1] if i+1 < len(nb['cells']) else None
        if next_cell:
            print(f"  Next cell content: {''.join(next_cell['source'])[:200]}")
            
    if "refine the prompt so that the explanation of the work done is clear" in source_text:
        print(f"Cell {i} (FOUND question 2: Prompt)")
        next_cell = nb['cells'][i+1] if i+1 < len(nb['cells']) else None
        if next_cell:
            print(f"  Next cell content: {''.join(next_cell['source'])[:200]}")
            
    if "write a short assessment of the work done" in source_text:
        # Check if it's the Automobile one or the Wine one
        # Automobile is first, Wine is second (after 'wine quality red' appears)
        # Actually it's simpler to check for context in preceding/current cell
        print(f"Cell {i} (FOUND question 3: Assessment)")
        next_cell = nb['cells'][i+1] if i+1 < len(nb['cells']) else None
        if next_cell:
            print(f"  Next cell content: {''.join(next_cell['source'])[:200]}")
