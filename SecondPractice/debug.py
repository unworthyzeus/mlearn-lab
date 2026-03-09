import nbformat
with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'markdown':
        print(f'=== Cell {i} ===')
        print(cell.source)
        print()
