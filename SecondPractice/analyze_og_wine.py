import json

with open('OGSecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb_og = json.load(f)

# Find where the Wine exercise starts in OG
wine_start_idx = -1
for i, cell in enumerate(nb_og['cells']):
    source = "".join(cell.get('source', [])).lower()
    if 'repeat the practice with the database wine quality' in source:
        wine_start_idx = i
        break

if wine_start_idx != -1:
    print(f"Wine exercise starts at OG cell {wine_start_idx}")
    # Print the next few cells to understand what "everything" means
    for i in range(wine_start_idx, min(wine_start_idx + 25, len(nb_og['cells']))):
        cell = nb_og['cells'][i]
        src = "".join(cell.get('source', [])).strip().replace("\n", " ")
        print(f"Cell {i} ({cell['cell_type']}): {src[:100]}")
else:
    print("Could not find Wine exercise start in OG.")
