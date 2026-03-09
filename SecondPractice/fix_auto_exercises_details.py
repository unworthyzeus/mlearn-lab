import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [line + "\n" for line in source.strip().split("\n")]
    return {"cell_type": "markdown", "metadata": {}, "source": source}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update Automobile Weights interpretation cell
# Finding the cell that has "Explain in words, the meaning of each of the values of the weights."
# but NO answer yet.
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "explain in words, the meaning of each of the values of the weights" in src and "answer:" not in src and "automobile" in src:
         # Replace with answered version
         cell['source'] = [
             "### **Exercise: Model Weight Interpretation (Automobile)**\n",
             "1. <font color='red'>**Explain in words, the meaning of each of the values of the weights. What sense do they have?**</font>\n",
             "**Answer:** For the Automobile dataset, each weight represents the expected change in the vehicle's price ($) for a one-unit increase in that variable. For example, a positive weight for **engine-size** means that larger engines directly increase the predicted price. A negative weight for **city-mpg** would reflect the market trend where fuel-efficient cars (higher MPG) are often priced lower than powerful, gas-intensive luxury models.\n",
             "\n",
             "2. <font color='red'>**If collecting a database is expensive, what recommendation would you give?**</font>\n",
             "**Answer:** I would recommend **feature selection**. In the 'BDCars' dataset, features like 'Engine Size' and 'Curb Weight' provide the most predictive power. Less influential features (like 'height' or 'bore') could be omitted from the database to save on survey and maintenance costs with negligible impact on the overall model accuracy.\n"
         ]

# 2. Update Automobile Internal Correlation cell
for i, cell in enumerate(nb['cells']):
    src = "".join(cell.get('source', [])).lower()
    if "relate price (target) to a subset of features" in src and "answer:" not in src:
         cell['source'] = [
             "### **Exercise: Relationship Analysis (Automobile)**\n",
             "1. <font color='red'>**Relate price (target) to a subset of features:**</font>\n",
             "**Answer:** The scatter matrix shows strong positive linear relationships between **price** and features like **engine-size** and **curb-weight**. This confirms that as the size and power of the car increase, the market value follows a predictable upward trend.\n",
             "\n",
             "2. <font color='red'>**Relate subset of features 'city-mpg',' length',' engine-size' between themselves:**</font>\n",
             "**Answer:** We observe clear mechanical dependencies: **engine-size** and **length** have a positive correlation (longer cars generally have larger engines), while **city-mpg** shows an inverse (negative) relationship with both size and weight. This reflects the engineering trade-off between vehicle mass and fuel efficiency.\n"
         ]

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Automobile weight/relationship exercises completed.")
