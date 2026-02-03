# Teste Técnico – Estágio IntuitiveCare 2026

Este repositório contém a solução desenvolvida para o teste de nivelamento
do processo seletivo de Estágio da IntuitiveCare.

O objetivo do projeto é realizar a exploração, tratamento e análise de dados
contábeis públicos da ANS (Agência Nacional de Saúde Suplementar), demonstrando
conhecimentos fundamentais de programação, organização de código, documentação
e capacidade de tomada de decisões técnicas.

## Estrutura do projeto

```TESTE-INTUITIVECARE/
├── data/ # Dados de entrada (CSV da ANS)
├── scripts/ # Scripts Python para processamento dos dados
├── output/ # Arquivos CSV gerados após o processamento
├── sql/ # Scripts SQL (modelagem e consultas)
└── README.md
```
## Tecnologias utilizadas

- Python 3
- Biblioteca pandas
- SQL 

## Visão geral da solução

A solução foi dividida em etapas independentes, seguindo o princípio de
responsabilidade única (Single Responsibility Principle), facilitando a
leitura, manutenção e entendimento do fluxo de processamento dos dados.

O pipeline de dados é composto por:
1. Exploração inicial dos dados;
2. Filtragem de registros relevantes;
3. Limpeza e padronização dos valores;
4. Agregação dos dados para análise;
5. Modelagem e consultas SQL conceituais.

## Etapas do processamento

### 1. Exploração inicial dos dados

Foi realizada a leitura inicial do arquivo CSV da ANS para compreensão da
estrutura dos dados, colunas disponíveis e tipos de informação.

**Trade-off considerado:**  
Optou-se por uma análise exploratória simples (visualização de colunas e
amostras dos dados), em vez de validações complexas ou análises estatísticas
avançadas, priorizando entendimento rápido e clareza, conforme o escopo do teste.

### 2. Filtragem de despesas

Os registros foram filtrados com base na descrição das contas contábeis,
selecionando apenas informações relacionadas a despesas, eventos e sinistros.

Arquivo gerado:
- `output/despesas_eventos.csv`

**Trade-off considerado:**  
A filtragem foi baseada em texto (descrições), pois o conjunto de dados não
fornecia uma classificação explícita e padronizada para todos os registros.
Essa abordagem privilegia simplicidade, transparência e aderência ao princípio
KISS (Keep It Simple).

### 3. Limpeza e padronização dos dados

Os valores monetários passaram por:
- Padronização de separadores decimais;
- Conversão para formato numérico;
- Remoção de registros inválidos ou inconsistentes.

**Trade-off considerado:**  
Foi adotada uma validação conservadora, descartando registros que não puderam
ser convertidos corretamente, evitando inferências que poderiam comprometer
a confiabilidade dos resultados.

### 4. Agregação dos dados

Os dados limpos foram agregados por operadora de saúde (Registro ANS),
resultando no total de despesas por operadora.

Arquivo gerado:
- `output/despesas_agrupadas_por_operadora.csv`

**Trade-off considerado:**  
A agregação foi realizada apenas por operadora, sem segmentações adicionais
(por data ou tipo de despesa), para manter o foco no objetivo principal do teste
e garantir uma solução simples e eficiente.

## Execução do projeto

### Pré-requisitos
- Python 3
- Biblioteca pandas

### Instalação da dependência
```bash
pip install pandas

# Execução dos scripts

Os scripts devem ser executados na seguinte ordem:

python scripts/explorar_dados.py
python scripts/filtrar_despesas.py
python scripts/limpar_e_agrupar.py
Após a execução, os arquivos processados serão gerados na pasta output/.
```
## SQL

Foram elaborados scripts SQL para representar uma modelagem relacional simples
e consultas analíticas sobre os dados agregados por operadora.

Os scripts incluem:

Criação de tabela para armazenamento das despesas;

Ordenação das operadoras por volume de despesas;

Cálculo da média de despesas;

Identificação de operadoras com despesas acima da média.

Trade-off considerado:
A execução das consultas em um banco de dados não foi realizada, pois o objetivo
do teste é avaliar a capacidade de modelagem, escrita de consultas e raciocínio
lógico. As consultas seguem SQL padrão, garantindo compatibilidade com diferentes
SGBDs relacionais.

## Considerações Finais

A solução foi desenvolvida com foco em simplicidade, clareza e organização,
seguindo boas práticas de desenvolvimento e documentação.

As decisões técnicas priorizaram soluções simples, eficientes e explicáveis,
alinhadas ao contexto de um teste de nivelamento para estágio e ao princípio
KISS.