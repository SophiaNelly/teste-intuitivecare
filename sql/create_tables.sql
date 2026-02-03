-- Criação da tabela para armazenar despesas agregadas por operadora
CREATE TABLE despesas_operadoras (
    reg_ans INTEGER NOT NULL,
    valor_total NUMERIC(15,2) NOT NULL
);