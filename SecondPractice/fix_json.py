import nbformat

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Set version to 4.4 to be safe
nb.nbformat = 4
nb.nbformat_minor = 4

for cell in nb.cells:
    if 'id' in cell:
        del cell['id']

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
print("IDs removed and version set to 4.4")
