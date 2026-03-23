import json

file_path = 'c:/mlearn-lab/FourthPractice/FourthPractice.ipynb'
with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and "Advanced Feature Engineering completed successfully" in ''.join(cell.get('source', [])):
        new_source = [
            "# 1. Feature Engineering on 'pdays'\n",
            "Data['contacted_before'] = (Data['pdays'] != -1).astype(float)\n",
            "Data['pdays'] = Data['pdays'].apply(lambda x: 0 if x == -1 else x) # Floor unconnected days to 0\n",
            "\n",
            "# 2. Feature Engineering on Heavy-Tailed distributions\n",
            "Data['balance_logSale'] = np.log(np.abs(Data['balance'])+1)*np.sign(Data['balance'])\n",
            "Data['duration_log'] = np.log(Data['duration']+1)\n",
            "\n",
            "# 3. Add Polynomial Interactions for Numerical Fields to capture demographic intersections\n",
            "from sklearn.preprocessing import PolynomialFeatures\n",
            "numerical_cols = ['age', 'balance_logSale', 'day', 'duration_log', 'campaign', 'pdays', 'previous']\n",
            "poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)\n",
            "poly_feats = poly.fit_transform(Data[numerical_cols])\n",
            "poly_feature_names = [f'poly_{k}' for k in range(poly_feats.shape[1])]\n",
            "\n",
            "import pandas as pd\n",
            "poly_df = pd.DataFrame(poly_feats, columns=poly_feature_names, index=Data.index)\n",
            "\n",
            "# Combine Back & Drop original non-logged numericals if they remain\n",
            "Data = pd.concat([Data, poly_df], axis=1)\n",
            "\n",
            "# 4. Standard Scaling numerical features\n",
            "from sklearn.preprocessing import StandardScaler\n",
            "scaler = StandardScaler()\n",
            "scale_cols = poly_feature_names + numerical_cols\n",
            "for col in scale_cols:\n",
            "    if col in Data.columns:\n",
            "        Data.loc[:, col] = scaler.fit_transform(Data[[col]])\n",
            "\n",
            "print('Advanced Regression Features (Polynomial + Log) created successfully!')\n"
        ]
        nb['cells'][i]['source'] = new_source

# Switch CV back from class_weight='balanced' to avoid extreme accuracy drop since the user complained about accuracy
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and 'LogisticRegressionCV' in ''.join(cell.get('source', [])):
        s = ''.join(cell['source'])
        if "penalty='l2', class_weight='balanced'" in s:
            s_new = s.replace("penalty='l2', class_weight='balanced'", "penalty='l2', class_weight=None")
            nb['cells'][i]['source'] = [line + '\n' for line in s_new.split('\n')][:-1]

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f)

print("Updated FourthPractice.ipynb with interactions!")
