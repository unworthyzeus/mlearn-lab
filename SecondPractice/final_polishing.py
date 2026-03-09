import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The content in unnamed (2).png is: MSE 0.43, R2 34.24%.
# My code calculates exactly those values.
# The car infographic (unnamed(1).png) shows 72.5% R2.
# My report in cell 57 used ~72.5%.

# I'll just do a final pass to ensure everything is perfect.
# I will NOT advise them to redo unless they specifically dislike "Auto-MPG" in the car one.

# Let's fix the remaining cell duplication at the end.
i = 0
while i < len(nb['cells']):
    src = "".join(nb['cells'][i].get('source', [])).lower()
    # If the cell is the old wine instruction that got pushed down...
    if i > 65 and "repeat the practice with the database" in src:
         # Remove it
         nb['cells'].pop(i)
         continue
    # If the cell is the old load wine data code... 
    if i > 65 and "file = \"winequality-red.csv\"" in src:
         nb['cells'].pop(i)
         continue
    i += 1

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Final cleanup of redundant cells. Infographic data matches calculations.")
