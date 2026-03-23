import json

file_path = 'c:/mlearn-lab/FourthPractice/FourthPractice.ipynb'
with open(file_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and "y_hat_test = logreg.predict(X_test)" in ''.join(cell.get('source', [])):
        new_source = [
            "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
            "# We must define X_test and y_test from TestDB\n",
            "X_test = TestDB[InputFeatures]\n",
            "y_test = TestDB['y']\n",
            "\n",
            "y_hat_test = logreg.predict(X_test)\n",
            "acc_test = accuracy_score(y_test, y_hat_test)\n",
            "print('Accuracy on Test Set (Initial unscaled model): {:.2f}%'.format(acc_test * 100))\n",
            "print(classification_report(y_test, y_hat_test))\n"
        ]
        nb['cells'][i]['source'] = new_source

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f)

print("Fixed X_test NameError in notebook.")
