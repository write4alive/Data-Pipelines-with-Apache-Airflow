from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 data_quality_checks = [],
                 redshift_conn_id = "",
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params here
        self.data_quality_checks = data_quality_checks
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        self.log.info('Connection Redshift')
        redshift = PostgresHook(self.redshift_conn_id)
        cnt_err  = 0
        
        for check_step in self.data_quality_checks:
            
            check_query     = check_step.get('data_check_sql')
            expected_result = check_step.get('expected_value')
            
            result = redshift.get_records(check_query)[0]
            
            self.log.info(f"Running query   : {check_query}")
            self.log.info(f"Expected result : {expected_result}")
            self.log.info(f"Check result    : {result}")
            
            
            if result[0] != expected_result:
                cnt_err += 1
                self.log.info(f"Data quality check fails At   : {check_query}")
                
            
        if cnt_err > 0:
            self.log.info('Data quality checks - Failed !')
        else:
            self.log.info('Data quality checks - Passed !')
  
        self.log.info('Data quality checking operations completed...')
