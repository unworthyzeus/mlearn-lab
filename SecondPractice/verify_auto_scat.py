import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find 'scatter_matrix(subset' (Automobile)
idx_auto_scat = -1
for i, cell in enumerate(nb['cells']):
    if "scatter_matrix(subset" in "".join(cell.get('source', [])) and "wine" not in "".join(cell.get('source', [])).lower():
         idx_auto_scat = i
         break

if idx_auto_scat != -1:
    print(f"--- Automobile Scatter Matrix at Cell {idx_auto_scat} ---")
    # Show following 3 cells
    for j in range(idx_auto_scat + 1, idx_auto_scat + 4):
        if j < len(nb['cells']):
             print(f"Cell {j}: {''.join(nb['cells'][j]['source'][:200])}")
else:
    print("Automobile Scatter Matrix not found!")
