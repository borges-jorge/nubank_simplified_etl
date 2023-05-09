from postgresql_auth import configure_postgres
import pandas as pd

class Loader:
    """
    A class for uploading Pandas dataframes to a PostgreSQL database.

    Attributes:
        db_engine (sqlalchemy.engine.base.Engine): The database engine used for connecting to PostgreSQL.
        

        def configure_postgres():
            
            connection_uri = "your_connection_uri"
            db_schema = 'your_schema'
            
            db_engine = sqlalchemy.create_engine(connection_uri, connect_args={'options': '-csearch_path={}'.format(db_schema)})
            return db_engine

        

    Methods:
        upload_to_postgres(dataframe, table_name):
            Uploads a Pandas dataframe to the specified table in the PostgreSQL database.
    """

    def __init__(self, db_engine=None):
        if db_engine is None:
            db_engine = configure_postgres()

        self.db_engine = db_engine

    # Loading raw and silver data into postgresql

    def upload_to_postgres(self, dataframe: pd.DataFrame, table_name: str) -> None:
        print("Subindo para o PostgreSQL")

        try:
            dataframe.to_sql(str(table_name), self.db_engine, if_exists="replace")

        except Exception as e:
            print("Erro ao fazer upload para o PostgreSQL: ", e)
        finally:
            self.db_engine.dispose()

    def read_from_postgres(self, query):
        df = pd.read_sql(query, self.db_engine)
        return df
