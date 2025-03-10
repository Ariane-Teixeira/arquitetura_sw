import streamlit as st

class Visualizacao:
    def mostrar_dados(self, df):
        st.title("Análise de Dados do LinkedIn Job Postings ⚒")
        st.write("Esta aplicação mostra gráficos gerados a partir do dataset de postagens de emprego no LinkedIn.")
        
        def calculate_null_zero_percentage(df):
            total_values = df.size
            null_values = df.isnull().sum().sum()
            zero_values = (df == 0).sum().sum()
            
            null_percentage = (null_values / total_values) * 100
            zero_percentage = (zero_values / total_values) * 100
            
            return null_percentage, zero_percentage

        
        # Estatísticas Gerais
        st.header("Estatísticas Gerais")
        st.write(df.describe().round())
        
        # Calcular os percentuais de valores nulos e zeros no seu DataFrame
        null_percentage, zero_percentage = calculate_null_zero_percentage(df)

        st.write(f"Percentual de valores nulos: {null_percentage:.2f}%")
        st.write(f"Percentual de valores zeros: {zero_percentage:.2f}%")
        
        # Valores Nulos por coluna
        st.header("📊 Valores Nulos por Coluna")
        null_values = df.isnull().sum()
        st.bar_chart(null_values)
        
        # Distribuições de Variáveis Numéricas
        st.header("📉 Distribuições de Variáveis Numéricas")
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_columns:
            st.subheader(f"Distribuição da variável {col}")
            st.line_chart(df[col].dropna())