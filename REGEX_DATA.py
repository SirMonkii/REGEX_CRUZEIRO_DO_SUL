import re

def data_transform(match):
    yyyy, mm, dd = match.groups()
    return f"{dd}-{mm}-{yyyy}"

data = input("\nDigite a data no formato Ano-Mes-Dia: ")

padrao = r"(\d{4})-(\d{2})-(\d{2})"

data_formatada = re.sub(padrao, data_transform, data)

print("\nData formatada: ", data_formatada)
