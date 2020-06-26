import pandas as pd
import os
from pathlib import Path


def extrair_indicadores_relevantes():
    print("Começando a extração e classificação de indicadores relevantes...")
    current_path = os.path.dirname(__file__)
    diretorio_projeto = Path(current_path).parent.parent    
    
    df = pd.read_csv(filepath_or_buffer=diretorio_projeto.as_uri() + '/data/brasil.csv')
        
    arquivo = open("../data/brasil_relevancia_indicadores.csv", "w")
    for i in range(df.shape[0]):        
        indicador_nome = str(df.iloc[i, 2])
        indicador_codigo = str(df.iloc[i, 3])
        relevancia = 1 - (df.iloc[i, 34:52].isna().sum()/19)
        if relevancia >= 0.6:
            linha = indicador_nome + ';' + indicador_codigo + ';' + str(relevancia) + '\n'        
            arquivo.write(linha)
