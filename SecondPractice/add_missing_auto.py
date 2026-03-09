import nbformat
import json

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, 4)

new_cells = []

for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'markdown':
        if 'explain in words, why the cross validation provides a more accurate estimate' in cell.source.lower():
            # append the question cell first
            new_cells.append(cell)
            
            # append answer cell
            ans = nbformat.v4.new_markdown_cell(
"**1. Cross-validation for accurate estimates:**  \n"
"Cross validation trains and evaluates the model on multiple different subsets of the data (folds), instead of relying on a single train-test split. This reduces the variance in the performance metric, preventing the score from being artificially high or low due to a 'lucky' or 'unlucky' split, thus providing an unbiased and more reliable estimate of the model's true performance on unseen data.  \n"
"**2. Usefulness of a confidence margin:**  \n"
"A confidence margin (like standard deviation of the RMSE across folds) tells us how stable or variable the model's performance is. A high variance means the model is highly sensitive to the specific data it is trained on. Knowing the bounds of performance allows decision makers to plan for the worst-case scenario and reliably trust the model's predictions within that margin."
            )
            new_cells.append(ans)
            continue
            
        elif 'refine the prompt so that the explanation of the work done is clear' in cell.source.lower():
            new_cells.append(cell)
            
            c1 = nbformat.v4.new_markdown_cell(
"**NotebookLM Prompt – Automobile Infographic:**\n"
"> \"I built a machine learning model to predict car prices. I used the Automobile dataset, cleaned missing values and encoded categorical variables, then trained a Linear Regression model validated with 5-Fold Cross-Validation (mean R² ≈ 72.5%). Create a clear and visually attractive infographic outline that shows at a glance: (1) the problem being solved (predicting car price), (2) the technique used (Linear Regression + Cross-Validation), and (3) whether the results were good (R² ~72.5% means a solid but improvable baseline). Keep it concise, professional, and easy to understand in under 30 seconds.\"\n\n"
"<img src=\"unnamed (1).png\" width=\"80%\">"
            )
            new_cells.append(c1)
            continue
            
        elif 'write a short assessment of the work done' in cell.source.lower():
            new_cells.append(cell)
            
            c2 = nbformat.v4.new_markdown_cell(
"**Executive Report: Automobile Car Price Prediction**\n\n"
"**Methodological Summary and Results:**\n"
"A Linear Regression model was built to predict car retail prices using the Automobile dataset. After cleaning the data (handling missing values and encoding categorical variables), the model achieved a cross-validated R² of ~72.5%, meaning it explains roughly 3 out of 4 units of price variability across unseen data splits.\n\n"
"**Roadmap for Performance Enhancement:**\n"
"To improve results, the next step should be replacing label encoding with one-hot encoding for nominal categories (e.g. body style, fuel type) and testing non-linear models such as Random Forests, which better capture complex feature interactions. Feature scaling and outlier treatment would also be recommended before any further deployment."
            )
            new_cells.append(c2)
            continue
            
        elif '**1. cross-validation for accurate estimates**' in cell.source.lower() or 'executive report: automobile car price prediction' in cell.source.lower() or 'notebooklm prompt – automobile' in cell.source.lower():
            # Skip existing occurrences so we don't duplicate when inserting above
            continue

    new_cells.append(cell)

nb.cells = new_cells

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print('Added missing Automobile infographic and executive report')
