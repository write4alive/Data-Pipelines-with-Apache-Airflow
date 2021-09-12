from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    
    insert_sql = """
        insert into {}
        {};
    """

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 redshift_conn_id = "",
                 table = "",
                 sql = "",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql = sql
        

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        load_sql = LoadDimensionOperator.insert_sql.format(
            self.table,
            self.sql
        )
        self.log.info(f"Inserting Data - to {self.table} ")
        redshift.run(load_sql)
