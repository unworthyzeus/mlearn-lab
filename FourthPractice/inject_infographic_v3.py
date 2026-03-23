import json
import shutil
import os

file_path = 'c:/mlearn-lab/FourthPractice/FourthPractice.ipynb'
image_src = r'C:/Users/guill/.gemini/antigravity/brain/e774ce46-5956-4400-bbcb-fdbd30df531a/bank_marketing_infographic_v3_1774281983349.png'
dest_path = 'c:/mlearn-lab/FourthPractice/bank_marketing_infographic_v3.png'

# Copy the generated image
shutil.copy(image_src, dest_path)

with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Update the exact prompt string shown before the image
for i, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    if cell['cell_type'] == 'markdown' and 'A modern, clean, and professional' in src:
        nb['cells'][i]['source'] = [
            "**Prompt used for generation:**\n",
            "\n",
            "> A modern, clean, and professional infographic about a Bank Marketing Machine Learning Classification project. The top should prominently display 'Bank Marketing Prediction'. Below, three clear sections should be present: \n",
            "1. 'The Problem': Predicting Term Deposit Subscriptions using customer demographics in a highly imbalanced dataset. \n",
            "2. 'The Technique': Logistic Regression optimized with LBFGS solver, utilizing advanced Feature Engineering: One-Hot Encoding, Domain-Specific Interactions, Log Transformations, and Quadratic features. \n",
            "3. 'The Result': '91.2% Accuracy' highlighted as a big, bold metric with a success icon. \n",
            "The design should use a soothing corporate palette with shades of blue, white, and a touch of green for highlighting the success. Clean layout, glassmorphism style, high quality, suitable for an executive presentation."
        ]

# Update the markdown cell holding the image
for i, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    if cell['cell_type'] == 'markdown' and 'bank_marketing_infographic' in src.lower() and 'Done! Infographic' in src:
        nb['cells'][i]['source'] = [
            "**Done! Infographic:**\n",
            "A comprehensive infographic highlighting the problem, the completely updated LBFGS robust feature engineering (One-Hot Encoding, Domain-Specific Interactions, Log Transformations, and Quadratic Features), and the definitive **91.2% Accuracy** result.\n",
            "\n",
            "![Bank Marketing Infographic v3](bank_marketing_infographic_v3.png)\n"
        ]

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f)

print("Infographic v3 injected successfully with updated 91.2% accuracies!")
