import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        src = "".join(cell.get('source', []))
        
        # Insert Automobile Infographic
        if "Automobile Pricing: Final Results and Report" in src and "[NEW INFOGRAPHIC PLACEHOLDER]" in src:
            cell['source'] = [line.replace("[NEW INFOGRAPHIC PLACEHOLDER]", '<img src="unnamed (3).png" width="90%">') for line in cell['source']]
        
        # Insert Wine Infographic
        if "Decanting Data: Analyzing Wine Quality" in src or "Red Wine Quality Structural Analysis" in src:
             if "[REMOVED: PLACEHOLDER FOR NEW INFOGRAPHIC]" in src:
                 cell['source'] = [line.replace("[REMOVED: PLACEHOLDER FOR NEW INFOGRAPHIC]", '<img src="unnamed (4).png" width="90%">') for line in cell['source']]
             elif "[NEW INFOGRAPHIC PLACEHOLDER]" in src:
                 cell['source'] = [line.replace("[NEW INFOGRAPHIC PLACEHOLDER]", '<img src="unnamed (4).png" width="90%">') for line in cell['source']]

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Infographics inserted into their respective sections.")
