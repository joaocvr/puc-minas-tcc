import pandas as pd
import os
import math
from pathlib import Path

def extrair_indicadores_relevantes_brasil():
    print("Começando a extração e classificação de indicadores relevantes...")
    
    diretorio_projeto = Path().resolve().parent.parent
    df = pd.read_csv(filepath_or_buffer=diretorio_projeto.as_uri() + '/data/brasil_indicadores.csv')
        
    arquivo_indicadores_brasil = open("../../data/brasil_relevancia_indicadores.csv", "w")

    coluna_indicador_nome = 2
    coluna_indicador_codigo = 3
    coluna_1990 = 24
    coluna_2015 = 49
    qtd_colunas = qtd_colunas = coluna_2015 - coluna_1990

    qtd_relevantes_e_preenchidos = 0
    for i in range(df.shape[0]):        
        indicador_nome = str(df.iloc[i, coluna_indicador_nome])
        indicador_codigo = str(df.iloc[i, coluna_indicador_codigo])
        relevancia = (df.iloc[i, coluna_1990:coluna_2015].isna().sum()/qtd_colunas)
        dado_coluna_2015_preenchido = math.isnan(float(df.iloc[i, coluna_2015])) == False
                
        if relevancia >= 0.6 and dado_coluna_2015_preenchido == True:
            linha = indicador_nome + ';' + indicador_codigo + ';' + str(relevancia) + '\n'        
            arquivo_indicadores_brasil.write(linha)
            qtd_relevantes_e_preenchidos = qtd_relevantes_e_preenchidos + 1



def main():
    print("Início da extração!")
    print("Esse processo objetiva listar os indicadores, presentes em '../data/brasil.csv', que possuem acima de 60% dos dados válidos.")
    print("Além disso, o intervalo de anos utilizado nesse processo foi a partir de 1990 até 2015.")
    print("Porém, os dados do ano de 2015 serão utilizados a fim de validação da predição e os outros a fim de treinamento.")
    print("O resultado disso estará armazenado no arquivo 'brasil_relevancia_indicadores.csv'.")
    extrair_indicadores_relevantes_brasil()
    print("Fim da extração!")

if __name__ == "__main__":
    main()