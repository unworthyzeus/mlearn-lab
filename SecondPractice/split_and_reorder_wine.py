import json

def create_markdown_cell(source):
    if isinstance(source, list):
         source = [line + "\n" if not line.endswith("\n") else line for line in source]
    else:
         source = [line + "\n" if not line.endswith("\n") else line for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Locate the massive cell with "Exercise: Wine Dataset Analysis"
idx_massive = -1
massive_cell = None
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "exercise: wine dataset analysis" in src:
         idx_massive = i
         massive_cell = cell
         break

if idx_massive != -1:
    # 2. Split it
    src_lines = massive_cell['source']
    
    # Split point: before "### **Executive Report: Chemical Signatures of Wine Quality**"
    # or before "3. <font color='red'>**Cross-validation Comparison:** Why use K=10?</font>"
    # Let's split it so the Weights (1,2) go together.
    
    # Actually, let's just rewrite them as two separate variables.
    weights_meaning_src = [
        "### **Exercise: Wine Weight Interpretation**\n",
        "\n",
        "1. <font color='red'>**Explain in words, the meaning of each of the values of the weights. What sense do they have?**</font>\n",
        "**Answer:** The weights represent the predicted change in sensory quality score for each chemical unit increase. **Alcohol** and **Sulphates** are top positive drivers (quality boosters), while **Volatile Acidity** (vinegar taste) is a sharp negative driver (quality degrader), which aligns with wine chemistry expertise.\n",
        "\n",
        "2. <font color='red'>**If collecting a database is expensive, what recommendation would you give?**</font>\n",
        "**Answer:** Prioritize measuring just **Alcohol, Volatile Acidity, and Sulphates**. These three metrics account for most of the predictive variance, allowing for cost-effective lab testing.\n"
    ]
    
    rest_src = []
    found_rest = False
    for line in src_lines:
        if "3. <font color='red'>**Cross-validation Comparison:**" in line or "Executive Report" in line:
            found_rest = True
        if found_rest:
            rest_src.append(line)
            
    # 3. Reorder
    # Cell 71 is the coefficients plot. We insert Weights Meaning after it.
    idx_plot = -1
    for i, cell in enumerate(nb['cells']):
        src = "".join(cell.get('source', [])).lower()
        if "coefs.plot" in src and "wine" in src:
            idx_plot = i
            break
    
    # If not found precisely, search for any coefs plot in wine
    if idx_plot == -1:
        for i, cell in enumerate(nb['cells']):
            src = "".join(cell.get('source', [])).lower()
            if "winemodel.coef_" in src or "coefs =" in src:
                 if i > 50: # wine is usually later
                    idx_plot = i
                    # But if it's followed by plt.show or something, let's skip the next one too
                    if i+1 < len(nb['cells']) and ("plt." in "".join(nb['cells'][i+1].get('source', [])) or "coefs.plot" in "".join(nb['cells'][i+1].get('source', []))):
                        idx_plot = i + 1
                    break
                    
    # Remove the massive cell
    nb['cells'].pop(idx_massive)
    
    # Update current index of plot after pop if massive was before it
    if idx_massive < idx_plot:
        idx_plot -= 1
        
    # Re-insert the rest where the massive was (or keep at end)
    # Actually, keep the "Rest" at the end of the section (just before Appendix)
    idx_appendix = -1
    for i, cell in enumerate(nb['cells']):
        if "## appendix" in "".join(cell.get('source', [])).lower():
            idx_appendix = i
            break
            
    if idx_appendix != -1:
        nb['cells'].insert(idx_appendix, create_markdown_cell(rest_src))
    else:
        nb['cells'].append(create_markdown_cell(rest_src))
        
    # Finally, insert Weights Meaning after plot
    if idx_plot != -1:
        nb['cells'].insert(idx_plot + 1, create_markdown_cell(weights_meaning_src))

    with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

print("Split and Reordered Weight Interpretation for Wine specifically to follow the coefficients plot.")
