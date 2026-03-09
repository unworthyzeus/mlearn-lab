import json

def create_markdown_cell(source):
    # Ensure source is a list of strings ending with \n or a single string
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Update the cells
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        src_text = "".join(cell.get('source', [])).lower()
        
        # 1. Update Automobile Section (Prompt & Remove Image)
        if "automobile infographic prompt" in src_text or "automobile infographic outline" in src_text:
            cell['source'] = [
                "### **Infographic Specification: Automobile Car Price Engine**\n",
                "\n",
                "**Comprehensive Prompt for Image Generation:**\n",
                "> \"Create a detailed data science infographic titled 'Driving Decisions: Automobile Price Engine'. The layout should be split into 4 logical phases. \n",
                "> **Phase 1: Raw Data & Cleaning.** Visualize the 'BDCars.csv' dataset. Show icons of cars and icons representing 'Cleaning' (handling '?' values, removing nulls). \n",
                "> **Phase 2: The Model Implementation.** Show a flowchart 'Linear Regression Algorithm' mapping various car features (horsepower, engine-size, curb-weight) to Price ($). \n",
                "> **Phase 3: Robust Evaluation.** Illustrate '5-Fold Cross-Validation' using a grid of 5 blocks where 4 are used for training and 1 for testing, rotated 5 times. \n",
                "> **Phase 4: Final Results.** Highlight prominently: 'Mean R\u00b2: ~81.49%' and 'Reliable Price Baseline established'. \n",
                "> **Visual Style:** High-tech, clean flat design with vibrant blue and slate-grey tones. Use modern sans-serif typography. Keep background professional and minimalist.\"\n",
                "\n",
                "[REMOVED: PLACEHOLDER FOR NEW INFOGRAPHIC]\n"
            ]

        # 2. Update Wine Section (Prompt & Remove Image)
        if "wine quality infographic" in src_text or "prompt to generate the wine" in src_text:
            cell['source'] = [
                "### **Infographic Specification: Decanting Data - Red Wine Quality**\n",
                "\n",
                "**Comprehensive Prompt for Image Generation:**\n",
                "> \"Design a sophisticated data-driven infographic titled 'Decanting Data: Analyzing Wine Quality via Chemistry'. \n",
                "> **Include these components:** \n",
                "> 1. **Data Source:** Mention 'Red Wine Quality Dataset' mapping Physicochemical Lab Tests to Sensory Quality Scores (0-10).\n",
                "> 2. **Process:** Show the 'Linear Regression' modeling and '5-Fold Cross-Validation' methodology.\n",
                "> 3. **Metrics Panel:** Display prominently: 'Mean MSE: 0.43' and 'Mean R\u00b2: 34.24%'.\n",
                "> 4. **Analysis Note:** Add a visual or text saying 'Linear limit reached: Future recommendation for Random Forest or non-linear models'.\n",
                "> **Visual Style:** Elegant aesthetic with deep Bordeaux red, gold accents, and cream background. Mix laboratory glassware icons with wine-related illustrations. Professional and data-heavy style with clean charts.\"\n",
                "\n",
                "[REMOVED: PLACEHOLDER FOR NEW INFOGRAPHIC]\n"
            ]

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Prompts improved and current infographics removed as requested.")
