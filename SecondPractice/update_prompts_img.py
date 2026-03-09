import nbformat

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, 4)

for cell in nb.cells:
    if cell.cell_type == 'markdown':
        source = cell.source
        if 'NotebookLM Prompt – Automobile Infographic:' in source or 'NotebookLM Prompt - Automobile Infographic:' in source:
            cell.source = """**Prompt to generate the Automobile Infographic (for Image Generators):**
> "A professional, clean, minimalist data science infographic about a Car Price Prediction model. The layout is divided into 3 clear visual sections. Section 1 shows an icon of a car and text 'Problem: Predicting Car Prices'. Section 2 shows data nodes and text 'Technique: Linear Regression & 5-Fold Cross-Validation'. Section 3 shows a moderate success gauge with text 'Results: Solid Baseline (72.5% R²)'. Modern corporate aesthetic, vector art style, blue and grey color palette, highly legible."

<img src="unnamed (1).png" width="80%">"""

        elif 'NotebookLM Prompt – Wine Quality Infographic:' in source or 'NotebookLM Prompt - Wine Quality Infographic:' in source:
             cell.source = """**Prompt to generate the Wine Quality Infographic (for Image Generators):**
> "A professional, clean, minimalist data science infographic about a Wine Quality Prediction model. The layout is divided into 3 clear visual sections. Section 1 shows a wine glass and lab beaker with text 'Problem: Predicting Wine Quality (0-10)'. Section 2 shows analytical charts and text 'Technique: Linear Regression & 5-Fold Cross Validation'. Section 3 shows a warning or moderate success icon with text 'Results: Moderate Accuracy due to categorical scores'. Modern analytics aesthetic, dark red and corporate white colors, vector art style."

<img src="unnamed (2).png" width="80%">"""

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print('Prompts updated for image generators.')
