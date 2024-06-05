"""
Query Builder to make queries to the AttitudeFile table in the EIC database.
"""
from datetime import datetime
from eic_db_request.query_builder.query_builder import QueryBuilder


class AttitudeFileQuery(QueryBuilder):
    """
    Class to construct queries to request the AttitudeFile model in the database.
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
        }

    def get_payload(self):
        """
        Return the payload to send with the request.
        """
        return {
            'db_model': 'AttitudeFile',
            'payload': self.payload_queries
        }
