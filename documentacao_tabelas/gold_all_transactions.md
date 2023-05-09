#### É o union all da tabela gold_transactions_account com a gold_credit_transactions

| colunas                | type   | descrição                       |
|-----------------------|--------|--------------------------------|
| transaction_id        | string | identificador único da transação|
| fornecedor            | string | nome do fornecedor              |
| transaction_created_at | date   | data em que a transação foi criada|
| amount                | float  | valor da transação ou da parcela (se houver)       |
| valor_parcelado        | float  | valor total parcelado (se houver)    |
| categoria             | string | categoria da transação          |
| credit_debit          | string | se a transação é crédito ou débito|
