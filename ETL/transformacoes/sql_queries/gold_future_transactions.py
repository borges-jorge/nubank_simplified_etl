gold_future_transactions_query = \
'''
WITH gold_credit_transactions AS (

    SELECT 
        *
    FROM gold_credit_transactions

)

, calendar AS (
    SELECT
        DATE(date_trunc('month' ,date_at)) AS month
    FROM
        calendar
    GROUP BY 1

)

, transacoes_parceladas_ativas AS (  

    SELECT
        ultima_parcela_at,
        transaction_created_at,
        calendar.month,
        transaction_id
    FROM
        gold_credit_transactions periodo_parcela
    JOIN
        calendar calendar
    ON  DATE(date_trunc('month' ,periodo_parcela.transaction_created_at ))<= calendar.month  AND periodo_parcela.ultima_parcela_at >= calendar.month 
)

, transacoes_futuras AS (
    SELECT 
        transacoes.month AS transacao_futura_parcela_at,
        --transacoes.ultima_parcela_at,
        details.*
    FROM
        transacoes_parceladas_ativas transacoes
    LEFT JOIN 
        gold_credit_transactions details
        ON
        transacoes.transaction_id = details.transaction_id
)

SELECT
        transaction_id
    ,   transacao_futura_parcela_at
    ,   ultima_parcela_at
    ,   fornecedor
    ,   amount
    ,   valor_parcelado
    ,   qtd_parcelas
    ,   categoria
FROM
    transacoes_futuras
'''
