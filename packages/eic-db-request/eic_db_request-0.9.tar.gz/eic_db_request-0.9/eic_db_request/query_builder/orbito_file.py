"""
Query Builder to make queries to the OrbitoFile table in the EIC database.
"""
from datetime import datetime
from eic_db_request.query_builder.query_builder import QueryBuilder


class OrbitoFileQuery(QueryBuilder):
    """
    Class to construct queries to request the OrbitoFile model in the database.
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
            'name': str,
            'tstart': datetime,
            'tstop': datetime,
            'min_orbit': int,
            'max_orbit': int
        }

    def get_payload(self):
        """
        Return the payload to send with the request.
        """
        return {
            'db_model': 'OrbitoFile',
            'payload': self.payload_queries
        }
