import nbformat
import os

with open('SecondPracticeV2.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

new_cells = []

# Exercise list and responses
responses = {
    "Explain in words, why correlation between input variables is bad": """**Correlation Analysis:**
Correlation with the **output** is highly desirable because it indicates that the feature has predictive power over the target variable. However, high correlation between **input variables** (known as multicollinearity) is problematic for linear models. It makes the model coefficients unstable and mathematically difficult to estimate accurately, as the algorithm cannot clearly distinguish the individual contribution of each correlated variable. This can lead to overfitting and poor interpretability of the model's weights.""",
    
    "Explain in words, the meaning of each of the values of the weights": """**Interpretation of Weights and Recommendations:**
1. **Meaning of Weights:** Each weight (coefficient) represents the predicted change in the car's price for a single-unit increase in that specific feature, assuming all other variables remain constant. For example, a coefficient of 500 for 'width' suggests that for every inch added to the car's width, the price is expected to rise by $500. The sign indicates the direction (positive or negative impact), and the magnitude indicates the sensitivity of the price to that feature.
2. **Recommendation for Expensive Databases:** If data collection is costly, I recommend performing **Feature Selection**. By identifying and focusing only on the variables with the strongest correlation to the price and the highest model weights, you can eliminate redundant or low-impact features. This allows for a more "lean" data collection process, saving resources while maintaining high predictive performance by only measuring what truly matters.""",
    
    "why r^2 is more usefull than MSE": """**Why R^2 is more useful than MSE:**  
While Mean Squared Error (MSE) provides an absolute measure of prediction error in the units of the target variable squared, it is highly dependent on the scale of the dataset. Therefore, it is difficult to judge whether a particular MSE is 'good' or 'bad' without context.  
On the other hand, the Explained Variance ($R^2$) normalizes the error, providing a relative score between 0 and 1 (or 0% to 100%). It represents the proportion of variance in the target variable that is explained by the model, making it much easier to interpret and comparable across different datasets and target ranges.""",
    
    "why the cross validation provides a more accurate estimate": """**Cross-Validation and Confidence Margins:**
1. **Accurate Estimates:** Cross validation trains and evaluates the model on multiple different subsets of the data (folds), instead of relying on a single train-test split. This reduces the variance in the performance metric, preventing the score from being artificially high or low due to a 'lucky' or 'unlucky' split, thus providing an unbiased and more reliable estimate of the model's true performance on unseen data.  
2. **Confidence Margin:** A confidence margin (like standard deviation of the RMSE across folds) tells us how stable or variable the model's performance is. A high variance means the model is highly sensitive to the specific data it is trained on. Knowing the bounds of performance allows decision makers to plan for the worst-case scenario and reliably trust the model's predictions within that margin.""",

    "Relate price (target) to a subset of features": """**Relation of Price to Features:**
The 'price' of a vehicle is most directly affected by features like 'engine-size', 'horsepower', and 'curb-weight'. In the scatter matrix, we can see a clear upward linear trend between price and engine-size, suggesting it is a primary driver of cost. Similarly, dimensions like 'width' and 'length' show positive correlation, as larger vehicles typically command higher prices in the market.""",

    "Relate  subset of features ' city-mpg',' length',' engine-size' between themselves": """**Correlation between City-MPG, Length, and Engine-Size:**
There is a strong negative correlation between 'city-mpg' and both 'engine-size' and 'length'. Larger cars with bigger engines are naturally less fuel-efficient. Conversely, 'length' and 'engine-size' show a positive correlation, as larger vehicle bodies are typically paired with larger displacement engines to maintain power-to-weight ratios."""
}

auto_exec_report = """**Executive Report: Auto-MPG Predictive Analysis**

**Strategic Overview and Implementation:**
We have successfully implemented a predictive modeling pipeline for the Auto-MPG dataset, aimed at estimating vehicle market value based on technical specifications. The project began with a rigorous data cleaning phase where we identified and resolved missing values (placeholder '?') and transformed complex categorical attributes (such as body style and engine type) into machine-readable numeric formats using mapped integer variables for doors/cylinders and label encoding for nominal descriptions. We utilized a Linear Regression model, which was validated using a 5-Fold Cross-Validation scheme to ensure the results are robust and not biased by specific data splits. The model achieved an Explained Variance (R²) of approximately 72.5%, indicating a strong ability to capture the primary pricing drivers within the dataset.

**Technical Assessment and Optimization Strategy:**
The analysis reveals that while Linear Regression provides a solid baseline, it is inherently limited when dealing with non-linear relationships. Features such as fuel efficiency (city-mpg) often show a reciprocal or polynomial relationship with price rather than a purely linear one. Additionally, the current model uses label encoding for non-ordinal features, which can introduce artificial biases. To evolve this solution, we propose transitioning to non-linear ensemble algorithms like Random Forests or XGBoost, which handle categorical data more effectively and can model complex feature interactions. We also recommend implementing robust feature scaling (StandardScaler) and outlier removal to refine the regression coefficients and ensure the model generalizes even more effectively to extreme vehicle configurations."""

wine_exec_report = """**Executive Report: Wine Quality Sensory Analysis**

**Methodological Summary and Results:**
this segment of the analysis employed a machine learning framework on the Red Wine Quality dataset to predict sensory quality ratings (0-10) using purely physicochemical laboratory data. The project analyzed several chemical factors, including alcohol concentration, pH levels, and volatile acidity. We deployed a Linear Regression model integrated with a 5-Fold Cross-Validation loop. The resulting metrics showed a moderate R², indicating that while physical chemistry is definitely correlated with perceived quality, a simple linear approach has difficulty mapping these continuous inputs to the subjective, integer-bounded scores typically provided by experts. The model is highly effective at identifying "average" wines but struggles with the nuances of exceptionally high or low-quality vintages.

**Roadmap for Performance Enhancement:**
The primary bottleneck is the nature of the target variable: quality is essentially an ordinal class, yet we are treating it as a continuous linear scale. To achieve a "best-in-class" prediction tool, we recommend re-framing this as a Classification or Ordinal Regression problem. Algorithms like SVM with RBF kernels or Neural Networks could capture the subtle chemical "thresholds" that distinguish a 7-score wine from a 6-score wine. Additionally, the dataset is heavily imbalanced toward mid-grade wines. We propose using synthetic data augmentation (SMOTE) to increase the representation of extreme scores, which would allow the model to better distinguish the chemical signatures of premium wines from budget-tier options, providing critical value for automated quality control in the vineyard."""

auto_prompt = """**NotebookLM Prompt – Auto-MPG Infographic:**
> "I built a machine learning model to predict car prices using the Auto-MPG dataset. I handled missing values, encoded categorical features, and trained a Linear Regression model validated with 5-Fold Cross-Validation, achieving a mean R² of ~72.5%. Create a clear, visually attractive infographic outline showing: (1) The problem (predicting vehicle market value), (2) The technique (Linear Regression + 5-Fold Cross-Validation), and (3) The results (reliable generalization with ~72.5% R²). It should be pretty, clear, and professional."

<img src="unnamed (1).png" width="80%">"""

wine_prompt = """**NotebookLM Prompt – Wine Quality Infographic:**
> "I built a machine learning model to predict the quality score of red wine (0–10) using physicochemical inputs like pH, alcohol, and acidity from the Wine Quality dataset. I applied Linear Regression with 5-Fold Cross-Validation. Create a clear and visually attractive infographic outline that communicates at a glance: (1) the problem (predicting subjective wine quality from lab measurements), (2) the technique used (Linear Regression + Cross-Validation), and (3) whether results were good and what the main limitation was (moderate R² due to the ordinal/categorical nature of quality scores). The depth and explanation should be as high as the Auto-MPG version, providing a clear professional overview."

<img src="unnamed (2).png" width="80%">"""

for i, cell in enumerate(nb.cells):
    # Remove existing reports/prompts to avoid duplicates
    if cell.cell_type == 'markdown':
        content = cell.source.lower()
        if any(marker in content for marker in [
            'executive report:', 
            'notebooklm prompt', 
            'correlation analysis:',
            'interpretation of weights',
            'relation of price to features:',
            'correlation between city-mpg'
        ]):
            continue
    
    new_cells.append(cell)

    # Insert exercise responses
    if cell.cell_type == 'markdown':
        for key, resp in responses.items():
            if key.lower() in cell.source.lower():
                new_cells.append(nbformat.v4.new_markdown_cell(resp))
                break

    # Auto-MPG Executive Report
    if cell.cell_type == 'markdown' and 'Executive report' in cell.source and 'Wine' not in cell.source:
        new_cells.append(nbformat.v4.new_markdown_cell(auto_exec_report))

    # Auto-MPG Infographic
    if cell.cell_type == 'markdown' and 'infographic' in cell.source.lower() and 'Wine' not in cell.source and 'Refine' not in cell.source:
        new_cells.append(nbformat.v4.new_markdown_cell(auto_prompt))

# Finally, append Wine sections at the end
new_cells.append(nbformat.v4.new_markdown_cell("---"))
new_cells.append(nbformat.v4.new_markdown_cell("## Wine Quality Results and Infographic"))
new_cells.append(nbformat.v4.new_markdown_cell(wine_exec_report))
new_cells.append(nbformat.v4.new_markdown_cell(wine_prompt))

nb.cells = new_cells
with open('SecondPracticeV2.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
print("Notebook rebuilt with images and expanded reports.")
