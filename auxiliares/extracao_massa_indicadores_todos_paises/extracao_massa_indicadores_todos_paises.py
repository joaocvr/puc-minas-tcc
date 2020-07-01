
import pandas as pd
import zipfile
import os
from pathlib import Path

def extrair_indicadores_todos_paises():
    print("Começando a extração dados dos indicadores relevantes de todos os países.")

    df = carregar_dados_educacao()
    lista_codigos_indicadores_relevantes = carregar_codigos_indicadores_relevantes()

    arquivo_massa_indicadores = open("./data/massa_indicadores_todos_paises.csv", "w")
    arquivo_massa_indicadores.write("Country Name;Indicator Name;Indicator Code;1999;2000;2001;2002;2003;2004;2005;2006;2007;2008;2009;2010;2011;2012;2013\n")

    coluna_nome_pais = 0
    coluna_indicador_nome = 2
    coluna_indicador_codigo = 3
    coluna_1999 = 33
    coluna_2013 = 48

    for i in range(df.shape[0]):
        if i == 0:
            continue
        
        indicador_codigo = str(df.iloc[i, coluna_indicador_codigo])
        if indicador_codigo not in lista_codigos_indicadores_relevantes:
            continue

        nome_pais = str(df.iloc[i, coluna_nome_pais])
        indicador_nome = str(df.iloc[i, coluna_indicador_nome])
        series_colunas_1999_a_2013 = df.iloc[i, coluna_1999:coluna_2013].fillna(0)
        
        dados_anos=""
        for ano_coluna in series_colunas_1999_a_2013:
            dados_anos = dados_anos + ";" + str(ano_coluna)
        
        linha = nome_pais + ';'+ indicador_nome + ';' + indicador_codigo + dados_anos + '\n'
        arquivo_massa_indicadores.write(linha)


def carregar_dados_educacao():
    os.chdir('..')
    os.chdir('..')    
    curDir = os.getcwd()
    zf = zipfile.ZipFile(curDir + '/data/Edstats_csv.zip')
    text_files = zf.infolist()
    df = None
    for csv_file in text_files:        
        if csv_file.filename == 'EdStatsData.csv':
            print("Abrindo o arquivo",csv_file.filename)
            df = pd.read_csv(zf.open(csv_file.filename))
            break

    if df.empty:
        exit("Erro ao ler o arquivo 'EdStatsData.csv' que fica dentro do 'Edstats_csv.zip' na pasta 'data'.")
    else:
        print("Arquivo 'EdStatsData.csv' carregado com sucesso.")
    
    return df


def carregar_codigos_indicadores_relevantes():
    codigos = []    
    with open(os.getcwd() + "/data/codigos_indicadores_relevantes.txt") as file:
        for line in file: 
            codigos.append(line.rstrip())
    
    if len(codigos) == 0:
        exit("Erro ao carregar os códigos dos indicadores relevantes previamente cadastrados.")
    else:
        print("Arquivo 'codigos_indicadores_relevantes.txt' carregado com sucesso.")

    return codigos


def main():
    print("Início da extração!")
    print("Esse processo objetiva extrair os dados relacionados aos indicadores presentes em 'indicadores_relevantes.csv.'.")
    print("A fonte dessa extração será o arquivo 'EdStatsData.csv' (localizado dentro do 'Edstats_csv.zip').")
    print("O resultado disso será armazenado em 'indicadores_relevantes_todos_paises.csv'")
    extrair_indicadores_todos_paises()
    print("Fim da extração!")

if __name__ == "__main__":
    main()