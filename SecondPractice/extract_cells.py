import nbformat
import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

with open('cells_debug.txt', 'w', encoding='utf-8') as f:
    for i, cell in enumerate(nb.cells):
        f.write(f"=== Cell {i} ({cell.cell_type}) ===\n")
        f.write(cell.source)
        f.write("\n\n")
