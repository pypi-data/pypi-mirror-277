"""
Query Builder to make queries to the Shift table in the EIC database.
"""
from datetime import datetime
from eic_db_request.query_builder.query_builder import QueryBuilder


class ShiftQuery(QueryBuilder):
    """
    Class to construct queries to request the Duty model in the database.
    """

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()

    def implement_table_attr(self):
        """
        Implement the attributes.
        """
        return {
            'start_date': datetime,
            'end_date': datetime,
            'main_account_id': int,
            'backup_account_id': int
        }

    def get_payload(self):
        """
        Return the payload to send with the request.
        """
        return {
            'db_model': 'Duty',
            'payload': self.payload_queries
        }
