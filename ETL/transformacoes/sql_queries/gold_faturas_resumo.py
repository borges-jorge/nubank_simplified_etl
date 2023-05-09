gold_faturas_resumo_query = \
'''
WITH faturas_lucas AS(
    
    SELECT
        *
    FROM silver_faturas_resumo
)

SELECT * FROM faturas_lucas
'''
