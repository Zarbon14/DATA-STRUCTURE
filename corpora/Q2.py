import pandas as pd
import json
import re


arquivo = pd.read_csv("corpus-q2.csv")

arquivo.head()

tam_arquivo = len(arquivo)

dicionario = {}

for rows in range (tam_arquivo):
    linha = re.findall('\w+',arquivo['gr'][rows])
    coluna = re.findall('\w+',arquivo['gi'][rows])

    for columns in range(len(linha)):
        if(linha[columns]) in dicionario:
            dicionario[linha[columns]] += 1
        else:
            palavra = linha[columns].lower()
            dicionario[palavra] = 1

    for columns in range (len(coluna)):
        if(coluna[columns]) in dicionario:
            dicionario[coluna[columns]] += 1
        else:
            palavra = coluna[columns].lower()
            dicionario[palavra] = 1

tam_dicionario = len(dicionario)

result = json.dumps(dicionario,ensure_ascii=False)

print(result)
