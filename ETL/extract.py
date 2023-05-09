from nu_auth import nu_auth

class Extractor:

    """
    Classe para extrair dados da API do Nubank.

    A classe utiliza o pacote nu_auth para autenticação e acesso aos dados do Nubank.
    Os métodos da classe permitem obter as transações da conta, as transações do cartão
    e as faturas da conta.

    Args:
        nubank (nu_auth.Nubank): Um objeto Nubank autenticado para acesso à API.
            Se nenhum objeto Nubank for fornecido, um novo objeto será criado com as
            credenciais do usuário.

            Você pode criar sua autenticação usando pynubank:

            def nu_auth():
                nu = Nubank()
                nu.authenticate_with_cert('seu_cpf', 'sua_senha', 'seu_caminho_para/cert.p12')
                return nu

    Attributes:
        nubank (nu_auth.Nubank): O objeto Nubank usado para acessar a API.

    Methods:
        get_account_transactions(): Obtém as transações da conta do usuário.
        get_card_transactions(): Obtém as transações do cartão de crédito do usuário.
        get_faturas(): Obtém as faturas da conta do usuário.

    """

    def __init__(self, nubank=None):
        if nubank is None:
            nubank = nu_auth()
            
        self.nubank = nubank

    def get_account_transactions(self) -> list[dict]:

        transactions_data  = []
        has_next_page = True
        cursor = None

        while has_next_page:
            feed = self.nubank.get_account_feed_paginated(cursor)

            transactions_data.extend(feed['edges'])

            if not feed['pageInfo']['hasNextPage']:
                break

            cursor = feed['edges'][-1]['cursor']

        return transactions_data

    def get_card_transactions(self) -> list[dict]:
        transactions = self.nubank.get_card_statements()
        return transactions

    def get_faturas(self) -> list[dict]:
        faturas = self.nubank.get_bills()
        return faturas
