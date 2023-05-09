#### São as transações realizadas na conta: transferências, pagamentos, pix, débito

| Coluna                  | Tipo    | Descrição                                 |
|-------------------------|----------|-------------------------------------------|
| transaction_id          | string   | ID da transação.         |
| type_transaction        | string   | Tipo da transação realizada.               |
| transaction_created_at  | date     | Data de criação da transação.              |
| amount                  | float    | Valor da transação.                        |
| terceiro                | string   | Nome do fornecedor envolvido na transação.   |
| categoria               | string   | Categoria da transação realizada (criada no pipeline)   |
| receita_despesa         | int      | Indicador de receita (1) ou despesa (-1) da transação. |
