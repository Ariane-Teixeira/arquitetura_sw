from domain.autenticacao import Autenticacao
from domain.dados import Dados
from domain.visualizacao import Visualizacao
from adapters.kaggle_adapter import KaggleAdapter
from adapters.visualization_adapter import VisualizationAdapter

def main():
    # Autenticar na API do Kaggle
    autenticacao = Autenticacao()
    api = autenticacao.autenticar_kaggle()

    # Baixar o dataset
    dados = Dados()
    dataset_name = "arshkon/linkedin-job-postings"
    file_name = dados.baixar_dataset(api, dataset_name)

    # Carregar os dados
    df = dados.carregar_dados(file_name)

    # Mostrar os dados e gráficos
    visualizacao = Visualizacao()
    visualizacao.mostrar_dados(df)

if __name__ == '__main__':
    main()