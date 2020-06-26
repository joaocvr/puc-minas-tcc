from extracao.extracao_indicadores_relevantes import extrair_indicadores_relevantes

def main():
    print("Hello World!")
    extrair_indicadores_relevantes()

if __name__ == "__main__":
    main()

    ## Funções Pandas
    #print(df.loc[0,:])
    #print(df.dtypes) #tipos de cada coluna
    #print(df.index) #RangeIndex(start=0, stop=3665, step=1)
    #print(df.describe()) #retorna a quantidade, média, valor mínimo, 25%,  50%,  75% e max dos valores das colunas
    #print(df['1970']) #seleciona uma coluna
    #print(df[0:3]) #seleciona um range de linhas
    #print(df.loc[3662:3664, ['2008', '2009', '2010']]) #retorna subset de linhas (especficadas pelo seu número) e colunas.
    #df = df.fillna(value=0) #Substitui 'NaN' por '0'
    #print(df.loc[:, ['2008', '2009', '2010']]) #retorna subset de linhas (especficadas pelo seu número) e colunas.
    #print(df.groupby('1970').sum()) #Agrupa DF pelo nome da coluna.