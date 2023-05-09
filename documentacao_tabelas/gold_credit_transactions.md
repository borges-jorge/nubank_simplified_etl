#### São as transações realizadas no cartão de crédito à vista ou parcelado

| colunas               | type   | descrição                                        |
|-----------------------|--------|--------------------------------------------------|
| transaction_id        | string | ID da transação                                  |
| fornecedor            | string | Nome do fornecedor ou estabelecimento             |
| title                 | string | Categoria vinda do app nubank                     |
| transaction_created_at| date   | Data em que a transação foi criada                |
| amount                | float  | Valor da transação ou da parcela (se houver)              |
| valor_parcelado       | float  | Valor total parcelado (se houver)    |
| qtd_parcelas          | int    | Quantidade de parcelas da transação (se houver)   |
| categoria             | string | Categoria da compra (criada no pipeline)           |
| ultima_parcela_at     | date   | Data da última parcela da transação (se houver)   |

