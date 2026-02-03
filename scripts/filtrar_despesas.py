import pandas as pd

# Ler os dados
df = pd.read_csv('data/dados_ans.csv', sep=';', encoding='latin1')

# Padronizar descrição para facilitar filtro
df['DESCRICAO'] = df['DESCRICAO'].str.upper()

# Filtrar despesas relacionadas a eventos/sinistros
filtro = df['DESCRICAO'].str.contains('SINISTRO|EVENTO|ASSIST', na=False)
df_filtrado = df[filtro]

# Selecionar apenas colunas relevantes
df_final = df_filtrado[['DATA', 'REG_ANS', 'DESCRICAO', 'VL_SALDO_FINAL']]

# Salvar resultado
df_final.to_csv('output/despesas_eventos.csv', index=False, sep=';')

print('Arquivo output/despesas_eventos.csv gerado com sucesso!')
