import pandas as pd

# Lendo o arquivo CSV da ANS
df = pd.read_csv('data/dados_ans.csv', sep=';', encoding='latin1')

# Exibindo informações básicas
print("Colunas do arquivo:")
print(df.columns)

print("\nPrimeiras linhas:")
print(df.head())
