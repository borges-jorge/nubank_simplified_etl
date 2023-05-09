gold_credit_transactions_query = \
'''
WITH silver_transactions_credit AS (
    SELECT 
        transaction_id
        , description AS fornecedor
        , title
        , CAST(time AS date) AS transaction_created_at
        , CAST(amount AS float)/100 AS amount
        , CASE WHEN valor_parcelado != 'none' THEN CAST(valor_parcelado AS float)/100 END AS valor_parcela
        , CASE WHEN details != 'none' THEN CAST(details AS integer) END AS qtd_parcelas
        
    FROM silver_transactions_credit
)

, column_categorizacao AS (
    SELECT
        *,
        CASE
            WHEN LOWER(fornecedor) SIMILAR TO '-*posto-*|-*shellbox-*|-*combust-*'
                THEN 'posto'        
            WHEN fornecedor = 'Servicar Paulinia Auto'
                THEN 'posto'

            -- você pode colocar mais categorias, como desejar



        END AS categoria
    FROM silver_transactions_credit
)

, transacoes_atuais as (
    SELECT 
        transaction_id,
        fornecedor,
        title,
        transaction_created_at,
        COALESCE(valor_parcela, amount) AS amount,
        CASE WHEN qtd_parcelas IS NOT NULL THEN amount END AS valor_parcelado,
        qtd_parcelas,
        categoria,
        DATE(transaction_created_at + interval '1 month'*(qtd_parcelas-1)) AS ultima_parcela_at
    FROM column_categorizacao order by transaction_created_at DESC
)

, gold_credit_transactions AS (
    SELECT 
        transaction_id
        , fornecedor
        , title
        , transaction_created_at
        , amount
        , valor_parcelado
        , qtd_parcelas
        , categoria
        , ultima_parcela_at
    FROM transacoes_atuais 
 )

SELECT 
    *
FROM gold_credit_transactions 
'''
