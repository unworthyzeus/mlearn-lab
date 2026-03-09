import nbformat

with open('OGSecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    og_nb = nbformat.read(f, as_version=4)

new_cells = []

# Enhanced content with answers
enhanced_content = {
    "Relate price (target) to a subset of features":
    "### Exercise\n"
    "1. <font color='red'> Relate price (target) to a subset of features </font> \n"
    "2. <font color='red'> Relate subset of features ' city-mpg',' length',' engine-size' between themselves </font>\n\n"
    "**Relation of Price to Features:**\n"
    "The 'price' of a vehicle is most directly affected by features like `engine-size` and `length` (positive correlation), and `city-mpg` (negative correlation). Larger engines and longer vehicles typically command higher prices in the market, while more fuel-efficient cars (higher MPG) in this dataset tend to be in a lower price bracket.",

    "Explain in words, why correlation between input variables is bad": 
    "### Exercise\n"
    "1. <font color='red'> Explain in words, why correlation between input variables is bad, but with the output is good. </font>\n\n"
    "**Why correlation between inputs is bad, but with the output is good:**\n"
    "*   **With Output (Good):** If an input correlates well with the output, it is a strong, valuable predictor that helps the model estimate the target variable accurately.\n"
    "*   **Between Inputs (Bad for Linear Models):** High correlation between input variables is known as multicollinearity. It introduces redundant information, which confuses the model when trying to determine the individual impact (weight/coefficient) of each specific feature. This leads to erratic, unstable coefficients without adding any actual predictive value.",

    "meaning of each of the values of the weights": # OG Cell 45
    "### Exercise\n"
    "1. <font color='red'> Explain in words, the meaning of each of the values of the weights. What sense do they have? </font>\n"
    "2. <font color='red'> If collecting a database is expensive, what recommendation would you give? </font>\n\n"
    "**1. Meaning of Weights (Coefficients):**\n"
    "Each weight represents the expected change in the target variable (Price) for a one-unit change in that specific input variable, assuming all other variables stay constant. For example, a positive weight for `engine-size` means that as the engine size increases, the predicted price also increases. The magnitude tells us the 'strength' of that feature's influence on the price.\n\n"
    "**2. Recommendation if Data Collection is Expensive:**\n"
    "If collecting data is costly, I would recommend performing Feature Selection. By identifying the variables with the most significant weights and highest correlations with the target, you can focus on collecting only the most 'important' features (like engine size and curb weight) and ignore those that add little predictive value, thereby reducing costs without significantly compromising model performance.",

    "r^2 is more usefull than MSE": # OG Cell 53
    "### Exercise\n"
    "1. <font color='red'> Explain in words, why r^2 is more usefull than MSE. </font>\n\n"
    "**Why R^2 is more useful than MSE:**\n"
    "While Mean Squared Error (MSE) provides an absolute measure of prediction error in the units of the target variable squared, it is highly dependent on the scale of the dataset. Therefore, it is difficult to judge whether a particular MSE is 'good' or 'bad' without context. On the other hand, the Explained Variance ($R^2$) normalizes the error, providing a relative score between 0 and 1 (or 0% to 100%). It represents the proportion of variance in the target variable that is explained by the model, making it much easier to interpret and comparable across different datasets.",

    "Create an infographic for the work done </font> 1. Explain": # OG Cell 56
    "### Exercise: <font color='red'> Create an infographic for the work done </font>\n"
    "1. Explain in words, why the cross validation provides a more accurate estimate of what happens with unseen data.\n"
    "2. Explain in words, the usefulness of having a confidence margin.\n\n"
    "**1. Cross-validation for accurate estimates:**\n"
    "Cross validation trains and evaluates the model on multiple different subsets of the data (folds), instead of relying on a single train-test split. This reduces the variance in the performance metric, preventing the score from being artificially high or low due to a 'lucky' or 'unlucky' split, thus providing an unbiased and more reliable estimate of the model's true performance on unseen data.\n\n"
    "**2. Usefulness of a confidence margin:**\n"
    "A confidence margin (like standard deviation of the RMSE across folds) tells us how stable or variable the model's performance is. A high variance means the model is highly sensitive to the specific data it is trained on. Knowing the bounds of performance allows decision makers to plan for the worst-case scenario and reliably trust the model's predictions within that margin.",

    "Create an infographic for the work done </font>  Use either": # OG Cell 57
    "### Exercise: <font color='red'> Create an infographic for the work done </font>\n"
    "Use either notebooklm or any chat.\n"
    "Refine the prompt so that the explanation of the work done is clear.\n\n"
    "**Prompt to generate the Automobile Infographic (for Image Generators):**\n"
    "> \"A professional, clean, minimalist data science infographic about a Car Price Prediction model. The layout is divided into 3 clear visual sections. Section 1 shows an icon of a car and text 'Problem: Predicting Car Prices'. Section 2 shows data nodes and text 'Technique: Linear Regression & 5-Fold Cross-Validation'. Section 3 shows a moderate success gauge with text 'Results: Solid Baseline (72.5% R²)'. Modern corporate aesthetic, vector art style, blue and grey color palette, highly legible.\"\n\n"
    "<img src=\"unnamed (1).png\" width=\"80%\">",

    "Create an executive report </font> Write a short": # OG Cell 58
    "### Exercise: <font color='red'> Create an executive report </font>\n"
    "Write a short assessment of the work done. Difficulties, challenges, and proposals for a solution.\n\n"
    "**Executive Report: Automobile Car Price Prediction**\n\n"
    "**Methodological Summary and Results:**\n"
    "A Linear Regression model was built to predict car retail prices using the Automobile dataset. After cleaning the data (handling missing values and encoding categorical variables), the model achieved a cross-validated R² of ~72.5%, meaning it explains roughly 3 out of 4 units of price variability across unseen data splits.\n\n"
    "**Roadmap for Performance Enhancement:**\n"
    "To improve results, the next step should be replacing label encoding with one-hot encoding for nominal categories (e.g. body style, fuel type) and testing non-linear models such as Random Forests, which better capture complex feature interactions. Feature scaling and outlier treatment would also be recommended before any further deployment.",

    "Repeat the practice with the database **Wine Quality**": # OG Cell 59
    "### Exercise: <font color='red'> Repeat the practice with the database **Wine Quality** target (**quality**) </font>\n\n"
    "--- \n\n"
    "## Wine Quality Results and Infographic\n\n"
    "**Executive Report: Wine Quality Sensory Analysis**\n\n"
    "**Methodological Summary and Results:**\n"
    "This segment of the analysis employed a machine learning framework on the Red Wine Quality dataset to predict sensory quality ratings (0-10) using purely physicochemical laboratory data. The project analyzed several chemical factors, including alcohol concentration, pH levels, and volatile acidity. We deployed a Linear Regression model integrated with a 5-Fold Cross-Validation loop. The resulting metrics showed a moderate R², indicating that while physical chemistry is definitely correlated with perceived quality, a simple linear approach has difficulty mapping these continuous inputs to the subjective, integer-bounded scores typically provided by experts. The model is highly effective at identifying \"average\" wines but struggles with the nuances of exceptionally high or low-quality vintages.\n\n"
    "**Roadmap for Performance Enhancement:**\n"
    "The primary bottleneck is the nature of the target variable: quality is essentially an ordinal class, yet we are treating it as a continuous linear scale. To achieve a \"best-in-class\" prediction tool, we recommend re-framing this as a Classification or Ordinal Regression problem. Algorithms like SVM with RBF kernels or Neural Networks could capture the subtle chemical \"thresholds\" that distinguish a 7-score wine from a 6-score wine. Additionally, the dataset is heavily imbalanced toward mid-grade wines. We propose using synthetic data augmentation (SMOTE) to increase the representation of extreme scores, which would allow the model to better distinguish the chemical signatures of premium wines from budget-tier options, providing critical value for automated quality control in the vineyard.\n\n"
    "**Prompt to generate the Wine Quality Infographic (for Image Generators):**\n"
    "> \"A professional, clean, minimalist data science infographic about a Wine Quality Prediction model. The layout is divided into 3 clear visual sections. Section 1 shows a wine glass and lab beaker with text 'Problem: Predicting Wine Quality (0-10)'. Section 2 shows analytical charts and text 'Technique: Linear Regression & 5-Fold Cross Validation'. Section 3 shows a warning or moderate success icon with text 'Results: Moderate Accuracy due to categorical scores'. Modern analytics aesthetic, dark red and corporate white colors, vector art style.\"\n\n"
    "<img src=\"unnamed (2).png\" width=\"80%\">"
}

for cell in og_nb.cells:
    if cell.cell_type == 'markdown':
        # Fix typo and apply name replacement
        cell.source = cell.source.replace('Excercise', 'Exercise')
        cell.source = cell.source.replace('Auto-MPG', 'Automobile')
        cell.source = cell.source.replace('Auto-mpg', 'Automobile')
        cell.source = cell.source.replace('auto-mpg', 'automobile')
        
        # Check if we have an enhanced version of this exercise
        for key, enhanced in enhanced_content.items():
            if key in cell.source:
                cell.source = enhanced
                break
    
    new_cells.append(cell)

og_nb.cells = new_cells

with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(og_nb, f)

print('Re-assembled notebook from OG with all sections, typos fixed, and full answers preserved.')
