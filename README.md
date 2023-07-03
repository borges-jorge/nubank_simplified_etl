### O que é o projeto
Oi :wave:

Aqui você encontra um pipeline de dados super simples que extrae seus dados do banco nubank, transforma e carrega eles em um outro banco (de dados) que pode ser conectado por um data viz qualquer.

Esse projeto busca facilitar minha vida financeira, e a sua, de uma forma bem mais personalizável e automática do que os aplicativos que encontro por aí.

![Image](https://github.com/lsilvestrepereira/nubank_simplified_etl/assets/120492595/c502d7d2-acc3-4db6-859e-c0fd26ad6adc)



### Como eu posso começar a usar?

Dá um clone no repositório para a sua máquina e vai:

#### Primeiro você precisa ter tudo que está no setup.sh instalado

#### Depois vem a autenticação do nubank:

* Vai no repositório do pynubank instala a biblioteca e baixa o cert.p12 https://github.com/andreroggeri/pynubank/blob/main/examples/login-certificate.md

* Tendo isso, aqui em **autenticacoes/nu_auth_template.py**  você coloca seu cpf e senha e o caminho pro p12 que baixou.

#### Em seguida, precisa ter um postgres para carregar os dados.

O jeito mais fácil de fazer isso é usando a parte gratuita do https://www.elephantsql.com/

Vai lá que é fácil criar a conta e o banco de até 20 mb. 

Com isso tu pega sua uri e cola na variável connection_uri no **autenticacoes/postgres_auth_template.py**. Já na variável db_schema você coloca o schema que aparece no 
www.elephantsql.com

**Dica:** para ter mais facilidade em administrar o banco de dados, baixa o dbeaver, lá você consegue deletar tabelas com o mouse, por exemplo :smiling_face_with_three_hearts:

#### Tendo tudo isso, já dá para rodar o pipeline executando o arquivo main.py

```python
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
```

Isso irá subir as tabelas raw, silver e gold ao postgresql

Agora é só brincar no dataviz de preferência :)


*... Vamos explorar um pouco mais o projeto ...*

### Se o objetivo do projeto é facilitar a vida financeira, como ele faz isso?

Já tentei utilizar diversos aplicativos brazukas, mas sempre encontro dois problemas: pouco personalizável e/ou pouco automático.

Este projeto resolve ambos problemas. Mas, por enquanto apenas pessoas que sabem codar vão conseguir utilizar e aproveitar disso.

Como?

Primeiro, a parte de extração roda bem e pega todos os dados que detalhei (Nubank apenas, por enquanto) da tua conta. Então isso já automatiza o acesso, evitando entrar no app e extrair csv por csv.

Segundo, a parte de categorização nas transformações em sql tentam, dentro do possível, colocar categorias para suas compras. Infelizmente, é manual no sentido de código, mas certamente é mais automático do que vemos em apps por aí. Principalmente se você normalmente compra nos mesmos lugares.

Olha só:

``` sql
        ...
            CASE
                WHEN LOWER(terceiro) SIMILAR TO '-*posto-*|-*shellbox-*|-*combust-*'
                    THEN 'posto'  
		     WHEN LOWER(terceiro) SIMILAR TO '-*telefonica brasil-*'
                    THEN 'internet'
                WHEN LOWER(terceiro) SIMILAR TO '-*companhia paulista de forca e luz-*'
                    THEN 'luz'
        ...
```

Essa é a lógica para a categorização, é manual no começo, mas pega retroativo e tudo que vier depois. 

Evidentemente, tem que tomar cuidado para não construir uma lógica que categorize errado.

Por fim, como tudo é lançado num Postgres depois fica fácil visualizar em um dataviz free. Assim é possível construir um dashboard muito mais personalizável.

### :construction:

Toda melhoria do projeto é bem vinda, fique a vontade para me dar sugestões!
