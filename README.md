# TCC - PUC Minas - Núcleo de Ensino a Distância :: Trabalho de Conclusão de Curso :: João Carlos Valadares Ribeiro Filho

Passo a passo para execução:

1) Instalar [python](https://wiki.python.org/moin/BeginnersGuide/Download)
2) Instalar bibliotecas listas na seção "Bibliotecas"


Bibliotecas:

- Pandas
- Zipfile
- Matplotlib
- Numpy
- Scikit-learn


Dataset:

- Descrição: "A 'World Bank EdStats All Indicator Query' contém mais de 4.000 indicadores comparáveis ​​internacionalmente que descrevem o acesso à educação, progressão, conclusão, alfabetização, professores, população e despesas. Os indicadores abrangem o ciclo educacional, do ensino pré-primário ao ensino profissional e superior. A consulta também contém dados de resultados de aprendizagem de avaliações de aprendizagem internacionais e regionais (por exemplo, PISA, TIMSS, PIRLS), dados de equidade de pesquisas domiciliares e dados de projeção / realização para 2050. Para mais informações, visite o site da EdStats".
- Link: https://datacatalog.worldbank.org/dataset/education-statistics
- Origem: http://www.barrolee.com/


Textos:

- Script "extracao_indicadores_relevantes.py":
Como o dataset original abrange vários países e o Brasil foi o escolhido como referência, então foi realizada uma seleção prévia dos indicadores desse país e armazenados em "basil_indicadores.csv".
A fim de escolher os indicadores, do Brasil, numericamente relevantes (com coluna de 2015 preenchida e com mais de 60% dos dados preenchidos entre 1990 e 2014), foi criado o script "extracao_indicadores_relevantes.py" que resulta na escrita do arquivo "brasil_relevancia_indicadores.csv" com a lista de indicadores seguindo essas sespecificações.
Após isso, o arquivo "brasil_relevancia_indicadores.csv" permitiu a escolha dos indicadores que possuem relação semântica.
