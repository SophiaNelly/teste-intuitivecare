-- Consulta 1: total de despesas por operadora
SELECT
    reg_ans,
    valor_total
FROM despesas_operadoras
ORDER BY valor_total DESC;


-- Consulta 2: média das despesas entre operadoras
SELECT
    AVG(valor_total) AS media_despesas
FROM despesas_operadoras;


-- Consulta 3: operadoras com despesas acima da média
SELECT
    reg_ans,
    valor_total
FROM despesas_operadoras
WHERE valor_total > (
    SELECT AVG(valor_total)
    FROM despesas_operadoras
)
ORDER BY valor_total DESC;
