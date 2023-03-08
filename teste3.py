import pandas as pd
import json



dados = json.load(open("dados.json"))

dataDF = pd.json_normalize(dados)

RetirandoZeros = dataDF[ dataDF['valor'] == 0 ].index

dataDF.drop(RetirandoZeros , inplace=True)

somando = dataDF.loc[dataDF['valor'] > dataDF['valor'].mean()].shape[0]


print("O menor valor de faturamento ocorrido em um dia do mês foi:", min(dataDF['valor']))

print("O maior valor de faturamento ocorrido em um dia do mês foi:", max(dataDF['valor']))

print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal é igual a:", somando,",sendo a média:",dataDF['valor'].mean())