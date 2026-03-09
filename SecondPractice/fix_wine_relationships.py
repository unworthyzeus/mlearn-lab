import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

def create_code_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Locate the scatter matrix cell to add the explanations AFTER it
insert_idx = -1
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if 'scatter_matrix' in src and 'wine' in src:
        insert_idx = i + 1
        break

if insert_idx != -1:
    relationship_ex = [
        create_markdown_cell(
"""### **Exercise: Relationship Analysis (Wine)**

1. <font color='red'>**Relate quality (target) to a subset of features (alcohol, volatile acidity, sulphates):**</font>
   **Answer:** Examining the scatter matrix against the target variable **quality**, we observe that **alcohol** and **sulphates** show a visible positive correlation with higher quality scores. Conversely, **volatile acidity** shows a downward trend, meaning wines with higher vinegar characteristics consistently receive lower sensory scores.

2. <font color='red'>**Relate subset of features 'alcohol', 'volatile acidity', 'citric acid' between themselves:**</font>
   **Answer:** The scatter matrix reveals that **citric acid** and **volatile acidity** show an inverse relationship in some clusters (higher citric often implies lower volatile acidity in stable wines). **Alcohol** appears relatively independent from the acidity metrics in this specific visualization, showing that quality is influenced by multiple distinct chemical profiles simultaneously."""
        )
    ]
    # Check if this exercise is already there to avoid duplicates
    existing = any("Relate quality (target) to a subset of features" in "".join(nb['cells'][j].get('source', [])) for j in range(max(0, insert_idx-5), min(len(nb['cells']), insert_idx+5)))
    if not existing:
        nb['cells'] = nb['cells'][:insert_idx] + relationship_ex + nb['cells'][insert_idx:]
    else:
        print("Relationship exercise already present.")

# 2. Fix order/Redundancy: The user mentioned duplications. 
# Let's check for duplicate wine loading or analysis blocks.
seen_wine_load = False
i = 0
while i < len(nb['cells']):
    src = "".join(nb['cells'][i].get('source', [])).lower()
    if 'winequality-red.csv' in src:
        if seen_wine_load:
             print(f"Removing duplicate wine load at cell {i}")
             nb['cells'].pop(i)
             continue
        seen_wine_load = True
    i += 1

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Added Wine Relationship exercises and cleaned duplicates.")
