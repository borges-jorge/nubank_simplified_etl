gold_account_transactions_query = \
    '''
    WITH raw_transactions AS (
        SELECT 
            *
        FROM silver_transactions_account
    )

    , cc_receita_despesa AS (

        SELECT
            *,
            
            LEFT(detail, STRPOS(detail, 'R$') -2) AS terceiro,
            CASE 
                WHEN type_transaction in(
                        'Compra no débito',
                        'Transferência enviada',
                        'Pagamento da fatura', -- cartão crédito
                        'Dinheiro guardado',
                        'Pagamento efetuado', -- boleto
                        'Recarga efetuada'
                        ) THEN -1
                WHEN type_transaction in(
                        'Transferência recebida',
                        'Dinheiro resgatado', --poupança
                        'Depósito recebido',
                        'Estorno de débito' ,
                        'Resgate RDB' --caixinhas   
                        ) THEN 1

            END receita_despesa

        FROM raw_transactions

    )

    , cc_categorias AS (
        
        SELECT
            *,
            CASE
                WHEN LOWER(terceiro) SIMILAR TO '-*posto-*|-*shellbox-*|-*combust-*'
                    THEN 'posto'        
                WHEN terceiro = 'Servicar Paulinia Auto'
                    THEN 'posto'
                    
               -- você pode colocar mais categorias, como desejar

            END AS categoria
        FROM cc_receita_despesa
            
    )

    , silver_account_transactions AS(

        SELECT
            transaction_id
            , type_transaction
            , transaction_created_at
            , amount
            , terceiro
            , categoria
            , receita_despesa
        FROM cc_categorias

    )

    SELECT 
        *
    FROM silver_account_transactions 
    '''
