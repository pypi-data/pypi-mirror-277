"""
Query Builder to make queries to the Calibration table in the EIC database.
"""
from datetime import datetime
from eic_db_request.query_builder.query_builder import QueryBuilder


class CalibrationQuery(QueryBuilder):
    """
    Class to construct queries to request the Calibration model in the database.
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def implement_table_attr(self):
        """
        Implement the attributes.
        """
        return {
            'name': str,
            'file_extension_type': str,
            'extension': str,
            'start_validity': datetime,
            'creation_date': datetime,
            'upload_date': datetime,
            'sending_date_caldb': datetime,
            'sending_date_crestdb': datetime
        }

    def get_payload(self):
        """
        Return the payload to send with the request.
        """
        return {
            'db_model': 'Calibration',
            'payload': self.payload_queries
        }
