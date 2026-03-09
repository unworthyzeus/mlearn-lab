import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('final_verify_out_utf8.txt', 'w', encoding='utf-8') as out:
    for i in range(54, len(nb['cells'])):
        cell = nb['cells'][i]
        out.write(f"--- Cell {i} ({cell.get('cell_type')}) ---\n")
        out.write("".join(cell.get('source', [])))
        out.write("\n" + "-" * 50 + "\n")
