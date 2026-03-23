import json

file_path = 'c:/mlearn-lab/FourthPractice/FourthPractice.ipynb'
with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

found_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and 'rest of the categorical variables' in str(cell.get('source', '')):
        found_idx = i
        break

if found_idx != -1:
    new_cells = []
    
    code1 = """# Mapping the rest of the categorical variables
binary_vars = ['housing', 'loan']
other_cat_vars = ['marital', 'education', 'contact', 'month', 'poutcome']

# Binary mapping
for var in binary_vars:
    mapping = {'no': -1, 'yes': 1}
    Data[var] = Data[var].map(mapping).astype(float)

# Other categorical variables mapping
for var in other_cat_vars:
    mapping = {val: i+1 for i, val in enumerate(Data[var].unique())}
    Data[var] = Data[var].map(mapping).astype(float)

print("Categorical variables mapped.")
"""
    new_cells.append({
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': [line + '\n' for line in code1.split('\n')][:-1]
    })
    
    code2 = """# Exploratory Data Analysis
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.figure(figsize=(10, 6))
sns.countplot(x='y', data=Data)
plt.title("Target Variable Distribution")
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(Data.corr(), annot=False, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

Data.hist(bins=20, figsize=(14,10), color='blue', alpha=0.7)
plt.tight_layout()
plt.show()
"""
    new_cells.append({
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': [line + '\n' for line in code2.split('\n')][:-1]
    })
    
    nb['cells'] = nb['cells'][:found_idx+1] + new_cells + nb['cells'][found_idx+1:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("Added categorical variable mapping and EDA successfully.")
else:
    print("Target cell not found.")

# Let's also fix the other homework sections
# 3. Homework: Explain a strategy of classification by reading the coefficients...
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and 'Explain a strategy of classification by reading the coefficients' in str(cell.get('source', '')):
        # insert markdown answer
        nb['cells'].insert(i+1, {
            'cell_type': 'markdown',
            'metadata': {},
            'source': [
                "<font color='red'>\n",
                "**Explanation of Classification Strategy based on Coefficients:**\n",
                "- **Sign of the coefficient:** A positive coefficient indicates that as the value of the variable increases, the probability of the target class (y=yes) increases. A negative coefficient means that an increase in the variable decreases the probability of the target class.\n",
                "- **Absolute value:** The magnitude of the coefficient represents the strength or importance of the feature's effect on the prediction. Larger absolute values correspond to stronger influence.\n",
                "- **Distribution and range:** Because the variables are on different scales (e.g., duration is in seconds, balance is in magnitude of thousands, while categorical mapped variables are 1 to N), their coefficients cannot be directly compared to gauge feature importance without standardization or normalization. A feature with a large numerical range might have a very small coefficient but still significantly influence the model.\n",
                "</font>"
            ]
        })
        break

# 4. Homework: Explain what has happened. Why irrelevant variables in one scale are important in another scale
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and 'Why irrelevant variables in one scale are important in another scale' in str(cell.get('source', '')):
        nb['cells'].insert(i+1, {
            'cell_type': 'markdown',
            'metadata': {},
            'source': [
                "<font color='red'>\n",
                "**Explanation:**\n",
                "- When using regularized linear models like Logistic Regression with an L2 penalty, the model penalizes large coefficients.\n",
                "- If a variable ranges from $10^3$ to $10^5$ (like balance) and another from 1 to 5 (like some categorical variables), the small-scale variable might require a huge coefficient to have an impact. Since regularization suppresses large coefficients, it disproportionately affects the small-scale variables.\n",
                "- By standardizing or taking the log-transform, all variables are brought to a relatively similar scale and variance (similar roughly to standard Normal if using Standard Scaler). This ensures that the penalty is applied uniformly across features, allowing the model to correctly identify and use genuinely important variables, preventing those with artificially tiny or huge scales from dominating due to numerical reasons.\n",
                "</font>"
            ]
        })
        break

# 5. Homework: Compute the accuracy in the test database
# 6. Homework: Compute the performance in the initial model with the variables in linear scale
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and 'Compute the accuracy in the test database' in str(cell.get('source', '')):
        # we found the cell that has those 3 homework items
        # let's add the code for test accuracy and linear scale computation
        code3 = """# Computing accuracy on the test set for the initial model
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import numpy as np

y_hat_test_original = logreg.predict(X_test) # Predict on X_test if available from partition
accuracy_orig = accuracy_score(y_test, y_hat_test_original)
print(\"<font color='red'>Accuracy on Test Database (Initial model): %0.1f%%</font>\" % (accuracy_orig * 100))
print(confusion_matrix(y_test, y_hat_test_original))
"""
        nb['cells'].insert(i+1, {
            'cell_type': 'code',
            'execution_count': None,
            'metadata': {},
            'outputs': [],
            'source': [line + '\n' for line in code3.split('\n')][:-1]
        })
        break

# 7. Homework: Feature engineering for improving the performance
found_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown' and 'Do some feature engineering for improving the performance' in str(cell.get('source', '')):
        found_idx = i
        break
if found_idx != -1:
    code4 = """# Feature engineering justifications
# Common sense & Distributions: Variables like 'balance' and 'duration' have heavy-tailed (skewed) distributions.
# Applying a log transformation helps to make these distributions more Gaussian-like, which improves the performance of Logistic Regression.
Data['balance_logSale'] = np.log(np.abs(Data['balance'])+1)*np.sign(Data['balance'])
Data['duration'] = np.log(Data['duration']+1)
# We also scale numerical features for the logistic regression model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
numerical_cols = ['age', 'balance_logSale', 'day', 'duration', 'campaign', 'pdays', 'previous']
Data[numerical_cols] = scaler.fit_transform(Data[numerical_cols])

print(\"Feature engineering complete.\")
"""
    nb['cells'].insert(found_idx+1, {
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': [line + '\n' for line in code4.split('\n')][:-1]
    })


with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
print("Finished updating explanations and code.")
