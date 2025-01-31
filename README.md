#  Financial environment development Project

## Objective of the Project
Build a chatbot-driven financial environment to assist users in managing their finances effectively.
Promote healthy financial habits by offering personalized, actionable guidance aligned with individual goals.
Leverage insights from two financial books (The Richest Man in Babylon and  The Intelligent Investor) to provide practical strategies for sustained wealth-building and financial success.


## Dataset Overview:
Generated a synthetic dataset using the Faker library.
The Dataset contains 3.000 rows and 16 columns and  includes user information, income, expenses, and financial allocations such as savings and investments.


## Challenges & Solutions
Challenge: Determine the best interface for the financial environment, focusing on individual user experience, the overall user base, or the analysis of usage patterns.
Solution : Build a dashboard to analyze patterns across all users and focus the chatbot experience on personalized user engagement and needs.

## Methodology

### **ETL**

Generate synthetic data for 250 users over 12 months.
Load raw data into the MySQL database and retrieve it using an SQL query.
Create a function to execute the SQL query and fetch the data.
Explore the dataset by checking for nulls, duplicates, and data types.
Clean the data by standardizing column names.

### ** Exploratory Data Analysis, Data Preprocessing & Visualizations **
-Define a method to calculate key statistics like the average, median, and range of the data.
-Visualize the distribution of data with graphs for each numerical column.
Define a function to calculate and visualize expense categories, total monthly expenses, and balance data.
Create and display three side-by-side charts: a bar chart for category contributions, a line chart for monthly expenses, and a bar chart for monthly balance.
Correlation Matrix: 
Remove features with no correlation to the target and those showing high multicollinearity with the target or between each other.
Keep only the relevant columns that contribute meaningfully to the model's predictions.

### ** Feature Engineering **
Drop the column name and perform data engineering by creating new features.

### ** Modelling  **
Performed a 70/30 train-test split to divide the dataset into training and testing sets.
Selected total expenses and balance as the target variables for prediction.
Used K-Means for clustering to identify spending patterns.
Applied Isolation Forest for anomaly detection to detect unusual financial behaviors.
Implemented XGBoost and Random Forest to predict total expenses and balance based on user financial data.

Models used:

k-means:
Used KMeans to group users into categories like Essential, Semi-Essential and Extra based on their expenses.
Displayed a pie chart to show how users are distributed across clusters.
Created reports that compare each user's expenses to their cluster’s average.

Isolation forest:
Implemented the Isolation Forest model to identify anomalies in the dataset, categorizing data points as -1 (anomaly) and 1 (normal).
Trained the model using 100 estimators, with the assumption that 10% of the data is expected to be anomalous.
Counted the anomalies and normal data points, and add a new column to indicate the anomaly status.

Random Forest:The model performes well achiving 95% for the target Total Expenses and 96% acuracy for target 2 balance.
XGBoost: The model performes well achiving 97% for the target Total Expenses and 98% for balance.

Streamlit Financial Environments
Users can review finances, track expenses, and download reports with highlighted anomalies by month.
The bot provides financial advice based on two financial books, tailored to user needs.
Streamlit Interface & Dashboard: Built on Streamlit, offering an intuitive interface and dashboard for visualizing financial data and insights.

Finbot
CHATBOT DEVELOPMENT
Driven Points:
Chatbot Development: Build AI-driven chatbot using OpenAI and NLP for context-aware financial advice.
Data Retrieval: Retrieve relevant financial documents from SQL database for accurate responses.
NLP & Prompt Engineering: Created a promped to provide clear and concise financial advice, with practical solutions based on  the financial books, explaining key concepts by using analogies.
Deployment & Integration: Deploy on Streamlit, integrate Chroma DB for fast document retrieval.
Maintenance & Improvements: Monitor and improve model parameters, enhance clustering model and dashboard filters for better analysis.



### ** Conclusions & Next Steps**
The average user balance is generally very low, while total spending exhibits a high range and variance.
The clustering model reveals that users with higher salaries tend to have better financial balances than others. However, in some cases, the model struggles to accurately capture group patterns.
The Isolation Forest model is performing well in anomaly detection, and XGBoost, the chosen model, achieves over 90% accuracy in predicting financial outcomes
Fine Tuning the K-means model to improve the silhuete score metric,  and exploring evalution on the Isolation Forest Model. 
Improve the Streamlit Dashboard to capture more hiden patterns.

### ** Delivarables
Jupyter Notebook with Full Code in Python: Contains all steps from data preprocessing to model evaluation.
PowerPoint Presentation: A concise overview of the project, including methodology, results, and key findings, supported by visual plots.
Streamlit App: Dashboard view with data retrieve from database with the expenses and predictions and chatbot that retrieve data from the financial books and gaves advice how the user can control their finances and show a report of the month expenses. 












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
