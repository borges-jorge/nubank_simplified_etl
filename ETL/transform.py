import pandas as pd


class Transformer:
    """
    Classe para transformar dados brutos (bronze) em dataframe utilizando pandas

    Métodos:
    - create_account_transactions_dataframe()
    - create_transactions_dataframe()
    - create_faturas_dataframe()

    Parâmetros:
    - transactions_data: lista de dicionários contendo informações sobre transações da conta.
    - transactions: lista de dicionários contendo informações sobre transações.
    - faturas: lista de dicionários contendo informações sobre faturas.

    Retornos:
    - df: dataframe criado a partir dos dados brutos fornecidos para cada método.

    """
     
    def __init__(self):
        pass

    def create_account_transactions_dataframe(self, transactions_data: list[dict]) -> pd.DataFrame: 
        
        title = []
        id = []
        postDate = []
        detail = []
        amount = []

        data = {
            'type_transaction': title,
            'transaction_created_at': postDate,
            'amount': amount,
            'detail': detail,
            'transaction_id': id
        }

        for transaction in transactions_data:
                title.append(transaction['node'].get('title'))
                id.append(transaction['node'].get('id'))
                postDate.append(transaction['node'].get('postDate'))
                detail.append(transaction['node'].get('detail'))
                amount.append(transaction['node'].get('amount'))
                
        df = pd.DataFrame(data)

        print(df.head(10))
        
        return df

    def create_transactions_dataframe(self, transactions: list[dict]) -> pd.DataFrame:
        description = []
        time = []
        title = []
        valor_parcelado = []
        amount = []
        details = []
        transaction_id = []
        
        for transaction in transactions:
            description.append(transaction.get('description', 'none'))
            time.append(transaction.get('time','none'))
            title.append(transaction.get('title','none'))
            amount.append(float(transaction.get('amount', 'none')))

            charges = transaction['details'].get('charges')
            if charges:
                details.append(charges.get('count'))
                valor_parcelado.append(charges.get('amount'))
            else:
                details.append('none')
                valor_parcelado.append('none')

            transaction_id.append(transaction.get('id','none'))

        data = {
            'description': description,
            'time': time,
            'title': title,
            'valor_parcelado': valor_parcelado,
            'amount': amount,
            'details': details,
            'transaction_id': transaction_id
        }

        df = pd.DataFrame(data)

        print(df.head(10))
        
        return df


    def create_faturas_dataframe(self, faturas: list[dict]) -> pd.DataFrame:
        due_date = []
        spent_amount = []

        for i in faturas:
            due_date.append(i['summary'].get('due_date'))
            spent_amount.append(float(i['summary'].get('spent_amount', 0)))

        data = {
            'due_date' : due_date,
            'spent_amount' : spent_amount
        }

        df = pd.DataFrame(data)

        print(df.head(10))

        return df 
