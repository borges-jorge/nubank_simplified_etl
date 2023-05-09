import sqlalchemy
  
def configure_postgres():
    """ 
    Para fazer conecção com o banco de dados Postgresql. 
    Esta função retorna a db_engine para usar na main
    """
    connection_uri = "sua_connection_uri" # Eu ensino a criar no readme, usando elephantsql
    db_schema = 'nome_seu_schema'
    
    return sqlalchemy.create_engine(connection_uri, connect_args={'options': '-csearch_path={}'.format(db_schema)})
