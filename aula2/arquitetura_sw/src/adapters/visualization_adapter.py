import pandas as pd
import streamlit as st

class VisualizationAdapter:
    def visualize_data(self, df):
        st.title("Análise de Dados do LinkedIn Job Postings")
        st.write("Este aplicativo mostra gráficos gerados a partir do dataset de postagens de emprego no LinkedIn.")
        
        # Estatísticas Gerais
        st.header("Estatísticas Gerais")
        st.write(df.describe().round())
        
        # Percentual de valores nulos
        st.header("Percentual de Valores Nulos")
        percent_null = (df.isnull().sum() / len(df)) * 100
        st.write(percent_null.round(2))
        
        # Percentual de valores zero
        st.header("Percentual de Valores Zero")
        percent_zero = (df == 0).sum() / len(df) * 100
        st.write(percent_zero.round(2))
        
        # Valores Nulos por coluna
        st.header("Valores Nulos por Coluna")
        st.write(df.isnull().sum())
        
        # Distribuições de Variáveis Numéricas
        st.header("Distribuições de Variáveis Numéricas")
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_columns:
            st.subheader(f"Distribuição da variável {col}")
            st.line_chart(df[col].dropna())