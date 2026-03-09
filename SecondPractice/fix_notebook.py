import nbformat
import sys

notebook_path = r'c:\mlearn-lab\SecondPractice\SecondPracticeV2.ipynb'

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    new_cells = []
    
    for i, cell in enumerate(nb.cells):
        new_cells.append(cell)

        # Look for the scatter matrix plot cell
        if cell.cell_type == 'code' and 'scatter_matrix' in cell.source and 'city-mpg' in cell.source and 'price' in cell.source:
            # Check if answer is already there in next cell
            already_added = False
            if i + 1 < len(nb.cells) and '**1. Explaining the plotted relationships:**' in nb.cells[i+1].source:
                already_added = True
            
            if not already_added:
                ans_cell1 = nbformat.v4.new_markdown_cell(
                    "**1. Explaining the plotted relationships:**\n"
                    "*   **Between the input features:** `engine-size` and `length` are positively correlated (longer cars require larger engines). `city-mpg` is negatively correlated with both `engine-size` and `length` (larger/longer cars are heavier and consume more fuel, leading to a lower MPG).\n"
                    "*   **With the target (price):** `price` is positively correlated with `length` and `engine-size` (larger, more powerful cars are more expensive), and negatively correlated with `city-mpg` (more fuel-efficient cars are relatively cheaper)."
                )
                new_cells.append(ans_cell1)

        # Look for the markdown cell asking to explain correlation...
        if cell.cell_type == 'markdown' and 'Explain in words, why correlation between input variables is bad' in cell.source:
            # Check if it was already added to prevent duplicates
            already_added = False
            if i + 1 < len(nb.cells) and '**2. Why correlation between inputs is bad, but with the output is good:**' in nb.cells[i+1].source:
                already_added = True
            
            if not already_added:
                ans_cell2 = nbformat.v4.new_markdown_cell(
                    "**2. Why correlation between inputs is bad, but with the output is good:**\n"
                    "*   **With Output (Good):** If an input correlates well with the output, it is a strong, valuable predictor that helps the model estimate the target variable accurately.\n"
                    "*   **Between Inputs (Bad for Linear Models):** High correlation between input variables is known as multicollinearity. It introduces redundant information, which confuses the model when trying to determine the individual impact (weight/coefficient) of each specific feature. This leads to erratic, unstable coefficients without adding any actual predictive value."
                )
                new_cells.append(ans_cell2)

    nb.cells = new_cells

    # Now replace Auto-MPG with Automobile in all markdown cells
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            cell.source = cell.source.replace('Auto-MPG', 'Automobile')
            cell.source = cell.source.replace('Auto-mpg', 'Automobile')
            cell.source = cell.source.replace('auto-mpg', 'automobile')

    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
        
    print("Notebook fixes applied successfully.")
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
