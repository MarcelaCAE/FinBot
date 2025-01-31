import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

#st.title("Main Page")
st.sidebar.success("Select a page above.")

#if "my_input" not in st.session_state:
#    st.session_state["my_input"] = ""

#my_input = st.text_input("Input a text here", st.session_state["my_input"])
#submit = st.button("Submit")
#if submit:
#    st.session_state["my_input"] = my_input
#    st.write("You have entered: ", my_input)
    
    
import pymysql
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# Configuração do MySQL
server = 'localhost'
port = '3306'
database = 'FINAL_PROJECT'
username = 'root'
password = '1234'

# Criando a conexão com SQLAlchemy
connection_string = f"mysql+pymysql://{username}:{password}@{server}:{port}/{database}"
engine = create_engine(connection_string)

# Função para verificar se o User ID é válido no banco de dados
def is_valid_user_id(user_id):
    query = f"SELECT COUNT(*) FROM users_info WHERE user_id = '{user_id}'"
    with engine.connect() as conn:
        result = pd.read_sql(query, conn)
    return result.iloc[0, 0] > 0

# Função para carregar dados de um usuário específico
@st.cache_data
def load_user_data(user_id):
    query = f"""
    SELECT u.user_id, u.name, e.* 
    FROM users_info u 
    JOIN expenses_users_clean e ON u.user_id = e.user_id
    WHERE u.user_id = '{user_id}'
    """
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df

# Função para obter o salário médio do usuário
def get_average_salary(user_id):
    query = f"""
    SELECT SUM(salary) / COUNT(DISTINCT month) AS avg_salary
    FROM expenses_users_clean 
    WHERE user_id = '{user_id}'
    """
    with engine.connect() as conn:
        result = pd.read_sql(query, conn)
    
    return result['avg_salary'].iloc[0] if not result.empty else None

# Função para realizar o KMeans clustering com base nas despesas e saldo
def perform_clustering(df):
    # Selecionando características numéricas para o clustering (total_expenses e balance)
    features = df[['total_expenses', 'balance']]

    # Normalizando os dados para melhorar a performance do KMeans
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Realizando o KMeans com 3 clusters (ajustável conforme necessário)
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(scaled_features)

    return df, kmeans

# Função para visualizar os clusters
def plot_clusters(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='total_expenses', y='balance', hue='cluster', data=df, palette='viridis', ax=ax, s=100)
    ax.set_title("Clustering of Users Based on Total Expenses and Balance")
    ax.set_xlabel("Total Expenses")
    ax.set_ylabel("Balance")
    st.pyplot(fig)

# Função para visualizar os gastos do usuário
def plot_expenses_analysis(df, user_id):
    categories = ['housing', 'fixed expenses', 'transport', 'food', 'health', 'education', 
                'communication', 'other', 'investments and savings', 'credits and debts']
    
    if df.empty:
        st.error(f"No data found for User ID {user_id}.")
        return
    
    existing_columns = [col for col in categories if col in df.columns]
    category_totals = df[existing_columns].sum()
    total_expenses = category_totals.sum()
    category_percentages = (category_totals / total_expenses) * 100 if total_expenses > 0 else category_totals
    
    df_monthly_expenses = df.groupby('month')['total_expenses'].sum().reset_index()
    monthly_balance = df.groupby('month')['balance'].sum().reset_index()
    
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    
    sns.barplot(x=category_percentages.index, y=category_percentages.values, ax=axs[0], palette="viridis")
    axs[0].set_title(f'Expenses per Category (User {user_id})')
    axs[0].set_xlabel('Category')
    axs[0].set_ylabel('Percentage of Expenses (%)')
    axs[0].tick_params(axis='x', rotation=45)
    
    sns.lineplot(x='month', y='total_expenses', data=df_monthly_expenses, 
                marker='o', linewidth=2, ax=axs[1], color='b')
    axs[1].set_title(f'Total Expenses per Month (User {user_id})')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Total Expenses')
    axs[1].tick_params(axis='x', rotation=45)
    
    sns.barplot(x='month', y='balance', data=monthly_balance, ax=axs[2], palette="coolwarm")
    axs[2].set_title(f'Balance Amount per Month (User {user_id})')
    axs[2].set_xlabel('Month')
    axs[2].set_ylabel('Balance Amount')
    axs[2].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    st.pyplot(fig)

# Função para verificar se o usuário está conseguindo guardar 1% do salário
def analyze_savings(df, user_id):
    total_balance = df['balance'].sum()
    avg_salary = get_average_salary(user_id)

    if avg_salary is None:
        st.error("⚠️ Could not retrieve average salary data.")
        return

    min_savings = avg_salary * 0.01  # 1% do salário
    df['meets_savings_goal'] = df['balance'] >= min_savings

    # Meses em que ele conseguiu guardar 1% do salário
    months_saving = df[df['meets_savings_goal']]['month'].tolist()

    st.subheader("💡 Financial Advice")
    
    if total_balance < 0:
        st.warning(f"⚠️ Your total balance is negative! Try saving at least *${min_savings:.2f}* per month.")

    if months_saving:
        st.success(f"✅ You managed to save at least *1% of your salary* in the following months: {', '.join(map(str, months_saving))}")

# Função para permitir download do relatório em Excel
def download_report(df):
    excel_file = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Excel Report",
        data=excel_file,
        file_name="financial_report.csv",
        mime="text/csv",
    )

# Função para realizar a detecção de anomalias
def detect_anomalies(df):
    # Selecionando as características numéricas relevantes (despesas e saldo)
    features = df[['total_expenses', 'balance']]

    # Usando o modelo Isolation Forest para detectar anomalias
    model = IsolationForest(contamination=0.05, random_state=42)  # A contaminação é a fração de anomalias
    df['anomaly'] = model.fit_predict(features)

    # Anomalias serão marcadas com -1, dados normais com 1
    anomalies = df[df['anomaly'] == -1]

    return anomalies

# Função para exibir anomalias encontradas
def plot_anomalies(df):
    anomalies = detect_anomalies(df)

    if anomalies.empty:
        st.info("No anomalies detected in your expenses or balance.")
    else:
        st.warning("⚠️ Anomalies Detected!")
        st.write(anomalies[['month', 'total_expenses', 'balance']])
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.scatterplot(x='total_expenses', y='balance', hue='anomaly', data=df, palette='coolwarm', ax=ax, s=100)
        ax.set_title("Anomalies in Expenses and Balance")
        ax.set_xlabel("Total Expenses")
        ax.set_ylabel("Balance")
        st.pyplot(fig)

# Função principal do Streamlit
def main():
    st.title("📊 Financial Management Dashboard")
    
    user_id = st.text_input("Enter your User ID:").strip()
    
    if user_id:
        if not is_valid_user_id(user_id):
            st.error("User not found in the database. Try another ID.")
        else:
            st.success("✅ User validated! How can I help today?")
            
            df = load_user_data(user_id)
            
            if st.button("📈 View Financial Analysis"):
                plot_expenses_analysis(df, user_id)

            if st.button("🤖 Perform Clustering"):
                df_with_clusters, kmeans_model = perform_clustering(df)
                plot_clusters(df_with_clusters)

            if st.button("💡 Yes, give me some tips!"):
                analyze_savings(df, user_id)
                download_report(df)

            if st.button("🚨 Detect Anomalies"):
                plot_anomalies(df)

if __name__ == "__main__":
    main()

