import nbformat

with open('OGSecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    og_nb = nbformat.read(f, as_version=4)

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    curr_nb = nbformat.read(f, as_version=4)

og_mds = [c.source.strip() for c in og_nb.cells if c.cell_type == 'markdown']
curr_mds = [c.source.strip() for c in curr_nb.cells if c.cell_type == 'markdown']

print("=== MARKDOWN CELLS IN OG BUT NOT IN CURRENT ===")
for md in og_mds:
    # simple check
    found = False
    for cmd in curr_mds:
        if md.lower() == cmd.lower() or md[:20].lower() in cmd.lower():
            found = True
            break
    if not found:
        print(f"MISSING:\n{md[:100]}...\n")

og_codes = [c.source.strip() for c in og_nb.cells if c.cell_type == 'code']
curr_codes = [c.source.strip() for c in curr_nb.cells if c.cell_type == 'code']

print("=== CODE CELLS IN OG BUT NOT IN CURRENT ===")
for code in og_codes:
    if not code: continue
    found = False
    for ccode in curr_codes:
        if code.lower() in ccode.lower() or code[:30].lower() in ccode.lower():
            found = True
            break
    if not found:
        print(f"MISSING:\n{code[:100]}...\n")
