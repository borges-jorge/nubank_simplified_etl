from extract import Extractor
from load import Loader
from transform import Transformer
from sql_queries.gold_account_transactions import gold_account_transactions_query
from sql_queries.gold_credit_transactions import gold_credit_transactions_query
from sql_queries.gold_faturas_resumo import gold_faturas_resumo_query
from sql_queries.gold_all_transactions import gold_all_transactions_query
from sql_queries.gold_future_transactions import gold_future_transactions_query


# Funções com a ETL de cada tabela

def gold_transactions_account_process(data_extractor, data_loader, data_transformer):
    # 1.1 Obtendo e processando os dados da account silver

    silver_transactions_account = data_extractor.get_account_transactions()
    df_transactions_account = data_transformer.create_account_transactions_dataframe(silver_transactions_account)
    
    
        # Carregando os dados no PostgreSQL

    data_loader.upload_to_postgres(df_transactions_account, "silver_transactions_account")


    # 1.2 lendo, processando e transformando os dados para account gold

    df_gold_transactions_account = data_loader.read_from_postgres(gold_account_transactions_query)
    
        # Carregando os dados no PostgreSQL

    data_loader.upload_to_postgres(df_gold_transactions_account, "gold_transactions_account")

def gold_credit_transactions_process(data_extractor, data_loader, data_transformer):
    # 2.1 Obtendo e processando os dados cartao de credito silver

    silver_transactions_credit = data_extractor.get_card_transactions()
    df_transactions_credit = data_transformer.create_transactions_dataframe(silver_transactions_credit)

        # Carregando os dados no PostgreSQL
    data_loader.upload_to_postgres(df_transactions_credit, "silver_transactions_credit")

    # 2.2 lendo, processando e transformando os dados para cartao de credito gold

    df_gold_credit_transactions = data_loader.read_from_postgres(gold_credit_transactions_query)

        # Carregando os dados no PostgreSQL

    data_loader.upload_to_postgres(df_gold_credit_transactions, "gold_credit_transactions")

def gold_faturas_resumo_process(data_extractor, data_loader, data_transformer):
    # 3.1 Obtendo e processando os dados fatura cartão silver

    silver_faturas_resumo = data_extractor.get_faturas()
    df_faturas = data_transformer.create_faturas_dataframe(silver_faturas_resumo)

        # Carregando os dados no PostgreSQL
    data_loader.upload_to_postgres(df_faturas, "silver_faturas_resumo")

    # 3.2 lendo, processando e transformando os dados para faturas gold

    df_gold_faturas_resumo = data_loader.read_from_postgres(gold_faturas_resumo_query)

        # Carregando os dados no PostgreSQL

    data_loader.upload_to_postgres(df_gold_faturas_resumo, "gold_faturas_resumo")

def gold_all_transactions_process(data_extractor, data_loader, data_transformer):
    # 4 Construindo e carregando gold_all_transactions (fatura com credit e account transactions, conferir query)

    df_gold_all_transactions = data_loader.read_from_postgres(gold_all_transactions_query)

        # Carregando os dados no PostgreSQL

    data_loader.upload_to_postgres(df_gold_all_transactions, "gold_all_transactions")

def gold_future_transactions_process(data_extractor, data_loader, data_transformer):
    # 5 Construindo e carregando gold_all_transactions (fatura com credit e account transactions, conferir query)

    df_gold_future_transactions = data_loader.read_from_postgres(gold_future_transactions_query)

        # Carregando os dados no PostgreSQL

    data_loader.upload_to_postgres(df_gold_future_transactions, "gold_future_transactions")


def main():

    # Iniciando instâncias

    data_extractor = Extractor()
    data_loader = Loader()
    data_transformer = Transformer()
    
    # Executando ETL

    gold_transactions_account_process(data_extractor, data_loader, data_transformer)
    gold_credit_transactions_process(data_extractor, data_loader, data_transformer)
    gold_faturas_resumo_process(data_extractor, data_loader, data_transformer)
    gold_all_transactions_process(data_extractor, data_loader, data_transformer)
    gold_future_transactions_process(data_extractor, data_loader, data_transformer)

if __name__ == "__main__":
    main()
