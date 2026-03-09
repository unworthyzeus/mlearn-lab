import json

def create_markdown_cell(source):
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in source.strip().split("\n")]}

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The content for Wine results (since it was likely skipped/deleted in the previous run)
wine_results = create_markdown_cell(
"""## Wine Quality Results and Infographic

**Executive Report: Wine Quality Sensory Analysis**

**Methodological Summary and Results:**
This segment of the analysis employed a machine learning framework on the Red Wine Quality dataset to predict sensory quality ratings (0-10) using purely physicochemical laboratory data. The project analyzed several chemical factors, including alcohol concentration, pH levels, and volatile acidity. We deployed a Linear Regression model integrated with a 5-Fold Cross-Validation loop. The resulting metrics showed a moderate R², indicating that while physical chemistry is definitely correlated with perceived quality, a simple linear approach has difficulty mapping these continuous inputs to the subjective, integer-bounded scores typically provided by experts. The model is highly effective at identifying "average" wines but struggles with the nuances of exceptionally high or low-quality vintages.

**Roadmap for Performance Enhancement:**
The primary bottleneck is the nature of the target variable: quality is essentially an ordinal class, yet we are treating it as a continuous linear scale. To achieve a "best-in-class" prediction tool, we recommend re-framing this as a Classification or Ordinal Regression problem. Algorithms like SVM with RBF kernels or Neural Networks could capture the subtle chemical "thresholds" that distinguish a 7-score wine from a 6-score wine. Additionally, the dataset is heavily imbalanced toward mid-grade wines. We propose using synthetic data augmentation (SMOTE) to increase the representation of extreme scores, which would allow the model to better distinguish the chemical signatures of premium wines from budget-tier options.

**Prompt to generate the Wine Quality Infographic (for Image Generators):**
> "A professional, clean, minimalist data science infographic about a Wine Quality Prediction model. The layout is divided into 3 clear visual sections. Section 1 shows a wine glass and lab beaker with text 'Problem: Predicting Wine Quality (0-10)'. Section 2 shows analytical charts and text 'Technique: Linear Regression & 5-Fold Cross Validation'. Section 3 shows a warning or moderate success icon with text 'Results: Moderate Accuracy due to categorical scores'. Modern analytics aesthetic, dark red and corporate white colors, vector art style."

<img src="unnamed (2).png" width="80%">"""
)

# Appendix content
appendix = create_markdown_cell(
"""## Appendix:
### Description of the variables (Automobile)
 1. make: The name of the produces of the car (a factor).
 2. fuel-type: The type of fuel used by the car, either diesel or gas (a factor).
 3. aspiration: Type of aspiration of fuel in the motor
 4. num-of-doors: The number of passenger doors, either two or four (a factor).
 5. body-style: The type of the car (a factor).
 6. drive-wheels: The wheels powered by the engine (a factor).
 7. engine-location: The location in the car of the engine (a factor).
 8. wheel-base: Distance between centers of front and rear wheels (numeric).
 9. length: Length of the body in inches (numeric).
 10. width: Width of the body in inches (numeric).
 11. height: Height in inches (numeric).
 12. curb-weight: Total weight in pounds (numeric).
 13. engine-type: Mechanical Feature.
 14. num-of-cylinders: Mechanical Feature.
 15. engine-size: Displacement in cubic inches (numeric).
 16. fuel-system: Mechanical Feature.
 17. bore: Mechanical Feature (numeric).
 18. stroke: Mechanical Feature (numeric).
 19. compression-ratio: Mechanical Feature (numeric).
 20. horsepower: Power in horsepowers (numeric).
 21. peak-rpm: Top speed in rounds-per-minute (numeric).
 22. city-mpg: Fuel consumption in city (numeric).
 23. highway-mpg: Fuel consumption in highway (numeric).
 24. price: Retail price in US Dollars (numeric).

## Description of variables: Wine Quality
### Input variables:
1. fixed acidity
2. volatile acidity
3. citric acid
4. residual sugar
5. chlorides
6. free sulfur dioxide
7. total sulfur dioxide
8. density
9. pH
10. sulphates
11. alcohol
12. quality (score 0-10)"""
)

# Code to load Wine data (from previous checks)
wine_code = {
 "cell_type": "code",
 "execution_count": None,
 "metadata": {},
 "outputs": [],
 "source": [
  "File = \"winequality-red.csv\"\n",
  "Filename = os.path.join(os.getcwd(),'Data',File)\n",
  "print(f'Filename with path: \\n {Filename}')\n",
  "Data = pd.read_csv(Filename)\n",
  "Data.head().T"
 ]
}

nb['cells'].append(wine_results)
nb['cells'].append(wine_code)
nb['cells'].append(appendix)

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Restored Wine results, Wine code, and Appendix.")
