import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('full_output_utf8.txt', 'w', encoding='utf-8') as out:
    for i in range(50, 85):
        if i >= len(nb['cells']): break
        cell = nb['cells'][i]
        out.write(f"--- Cell {i} ({cell.get('cell_type')}) ---\n")
        out.write("".join(cell.get('source', [])))
        out.write("\n" + "-" * 50 + "\n")
