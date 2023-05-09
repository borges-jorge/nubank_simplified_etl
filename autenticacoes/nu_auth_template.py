from pynubank import Nubank

  # conferir como gerar arquivo .p12 no github do pynubank ou no readme aqui
  
def nu_auth():
    nu = Nubank()
    nu.authenticate_with_cert('seu_cpf', 'sua_senha_nu', '/caminho_para_arquivo/cert.p12')
    return nu
