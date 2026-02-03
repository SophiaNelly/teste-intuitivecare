import pandas as pd

# Ler arquivo filtrado
df = pd.read_csv('output/despesas_eventos.csv', sep=';')

# Trocar vírgula por ponto e converter para número
df['VL_SALDO_FINAL'] = (
    df['VL_SALDO_FINAL']
    .astype(str)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
)

df['VL_SALDO_FINAL'] = pd.to_numeric(df['VL_SALDO_FINAL'], errors='coerce')

# Remover valores inválidos ou negativos
df = df[df['VL_SALDO_FINAL'] > 0]

# Agrupar por operadora (REG_ANS)
df_agrupado = (
    df.groupby('REG_ANS')['VL_SALDO_FINAL']
    .sum()
    .reset_index()
)

# Salvar resultado final
df_agrupado.to_csv('output/despesas_agrupadas_por_operadora.csv', index=False, sep=';')

print('Arquivo output/despesas_agrupadas_por_operadora.csv gerado com sucesso!')
