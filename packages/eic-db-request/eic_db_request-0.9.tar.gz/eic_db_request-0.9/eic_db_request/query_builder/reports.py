"""
Query Builder to make queries to the Report table in the EIC database.
"""
from eic_db_request.query_builder.query_builder import QueryBuilder


class ReportQuery(QueryBuilder):
    """
    Class to construct queries to request the Report model in the database.
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
            'id': int,
            'week_date': str,
            'is_generated': bool
        }

    def get_payload(self):
        """
        Return the payload to send with the request.
        """
        return {
            'db_model': 'Report',
            'payload': self.payload_queries
        }
