"""
Query Builder to make queries to the Event table in the EIC database.
"""
from datetime import datetime
from eic_db_request.query_builder.query_builder import QueryBuilder


class EventsQuery(QueryBuilder):
    """
    Class to construct queries to request the Event model in the database.
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
            'hk_definition_id': int,
            'report_id': int,
            'handled_by_account_id': int,
            'band_id': int,
            'is_alarm': bool,
            'status': str,
            'time': datetime,
            'value': str
        }

    def get_payload(self):
        """
        Return the payload to send with the request.
        """
        return {
            'db_model': 'Event',
            'payload': self.payload_queries
        }
