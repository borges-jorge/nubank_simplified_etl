gold_all_transactions_query = \
'''
WITH gold_transactions_account_filtered AS (
    SELECT 
        transaction_id
        , terceiro AS fornecedor
        , CAST(transaction_created_at AS DATE) AS transaction_created_at
        , amount
        , 0 AS valor_parcelado
        , categoria
        , 'debit' AS credit_debit
        
    FROM gold_transactions_account
    WHERE type_transaction LIKE 'Compra-*no-*bito'

)

, gold_credit_transactions_filtered AS (

    SELECT 
        transaction_id
        , fornecedor
        , CAST(transaction_created_at AS DATE) AS transaction_created_at
        , amount
        , valor_parcelado
        , categoria
        , 'credit' AS credit_debit
    FROM gold_credit_transactions

)

    SELECT
        *
    FROM
        gold_transactions_account_filtered
    UNION ALL
    SELECT
        *
    FROM
        gold_credit_transactions_filtered
'''
