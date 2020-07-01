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
    coluna_1999 = 33
    coluna_2013 = 47
    qtd_colunas = coluna_2013 - coluna_1999 + 1
    for i in range(df.shape[0]):
        indicador_nome = str(df.iloc[i, coluna_indicador_nome])
        indicador_codigo = str(df.iloc[i, coluna_indicador_codigo])
        relevancia = 1 - (df.iloc[i, coluna_1999:coluna_2013].isna().sum()/qtd_colunas)
        dado_coluna_2013_preenchido = math.isnan(float(df.iloc[i, coluna_2013])) == False        

        if relevancia >= 0.6 and dado_coluna_2013_preenchido:
            linha = indicador_nome + ';' + indicador_codigo + ';' + str(relevancia) + '\n'        
            arquivo_indicadores_brasil.write(linha)
        



def main():
    print("Início da extração!")
    print("Esse processo objetiva listar os indicadores, presentes em '../data/brasil.csv', que possuem acima de 60% dos dados válidos.")
    print("Além disso, o intervalo de anos utilizado nesse processo foi a partir de 1999 até 2013.")
    print("Porém, os dados do ano de 2013 serão utilizados a fim de validação da predição e os outros a fim de treinamento.")
    print("O resultado disso estará armazenado no arquivo 'brasil_relevancia_indicadores.csv'.")
    extrair_indicadores_relevantes_brasil()
    print("Fim da extração!")

if __name__ == "__main__":
    main()