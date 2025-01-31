# Financial Environment Development Project

## Project Overview
This project aims to build a chatbot-driven financial environment to assist users in managing their finances effectively. 
The goal is to promote healthy financial habits by offering personalized, actionable guidance aligned with individual goals. 
The project leverages insights from two financial books (*The Richest Man in Babylon* and *The Intelligent Investor*) to provide practical strategies for sustained wealth-building and financial success.

## Dataset Overview
- A **synthetic dataset** containing **3,000 rows** and **16 columns** was generated using the **Faker** library.
- The dataset includes user information, income, expenses, and financial allocations such as savings and investments.

## Key Features
- **Financial Advice Chatbot**: Powered by OpenAI and NLP, this chatbot provides personalized financial advice based on user inputs, referencing key concepts from *The Richest Man in Babylon* and *The Intelligent Investor*.
- **Data Dashboard**: Built with Streamlit, the dashboard offers an intuitive interface for users to review finances, track expenses, and visualize financial data. It includes tools for anomaly detection, clustering, and trend analysis.
- **Expense Prediction**: The project utilizes machine learning models like K-Means, Isolation Forest, XGBoost, and Random Forest for clustering, anomaly detection, and prediction of total expenses and balances.

## Methodology

### 1. ETL Process
- Synthetic data was generated for **250 users** over **12 months**.
- The data was loaded into a **MySQL database** and retrieved using SQL queries.
- Data was explored and cleaned by checking for null values, duplicates, and standardizing column names.

### 2. Exploratory Data Analysis & Visualizations
- Key statistics such as **average**, **median**, and **range** were calculated.
- Visualizations were created for expense categories, monthly expenses, and balances.
- Correlation matrix analysis was performed to identify and remove irrelevant features for model predictions.

### 3. Feature Engineering
- Data engineering steps included creating new features to improve model performance.

### 4. Modelling
- Performed a 70/30 train-test split to divide the dataset into training and testing sets.
- Selected total expenses and balance as the target variables for prediction.
- **K-Means Clustering**: Used to categorize users based on spending behavior (e.g., Essential, Semi-Essential, Extra) and clustering to identify spending patterns.
- **Isolation Forest**: Anomaly detection was implemented to identify unusual financial behaviors.
- **XGBoost and Random Forest**: Models were used to predict total expenses and balances.

#### Models Results

**K-Means Clustering**:
- Used KMeans to group users into categories like Essential, Semi-Essential and Extra based on their expenses.
- Displayed a pie chart to show how users are distributed across clusters.
- Created reports that compare each user's expenses to their cluster’s average.

**Isolation Forest**
- Implemented the Isolation Forest model to identify anomalies in the dataset, categorizing data points as -1 (anomaly) and 1 (normal).
- Trained the model using 100 estimators, with the assumption that 10% of the data is expected to be anomalous.
- Counted the anomalies and normal data points, and add a new column to indicate the anomaly status.

**Random Forest**:
The model performed well achieving 95% for (target 1) Total Expenses and 96% accuracy for (target 2) balance.

**XGBoost**
XGBoost: The model performed well achieving 97% accuracy for (target 1) Total Expenses and (target 2) 98% for balance.

### 5. Streamlit Application
- The **Streamlit app** allows users to interact with the financial data, visualize trends, and receive advice from the chatbot.
- **Chroma DB** was integrated for efficient document retrieval from the financial books.

## Deliverables
1. **Jupyter Notebook**: Full Python code from data preprocessing to model evaluation.
2. **PowerPoint Presentation**: An overview of the project, methodology, results, and key findings.
3. **Streamlit App**: The final dashboard view with financial data, predictions, and chatbot integration.

## Conclusions & Next Steps
- Users with higher salaries tend to have better financial balances, but there is variability in spending patterns.
- The clustering model reveals that users with higher salaries tend to have better financial balances than others. However, in some cases, the model struggles to accurately capture group patterns.
- The Isolation Forest model is performing well in anomaly detection, and XGBoost, the chosen model, achieves over 90% accuracy in predicting financial outcomes
- Next steps include fine-tuning the **K-Means** clustering model to improve the silhouette score and enhancing the **Streamlit dashboard** to uncover hidden financial patterns.


