"""
Query Builder to make queries to the Hk Values tables in the EIC database.
"""
from datetime import datetime
from eic_db_request.query_builder.query_builder import QueryBuilder


class HouseKeepingQuery(QueryBuilder):
    """
    Class to construct queries to request the HouseKeeping models in the database.
    """

    def __init__(self, hk_names):
        """
        Constructor
        """
        super().__init__()
        self.names = self.get_hk_names(hk_names)

    @staticmethod
    def get_hk_names(hk_names: list[str]) -> list:
        """
        Control the format of provided HK names.

        :param hk_names: The list of HK names to search in the database.
        """
        if not isinstance(hk_names, list) or not hk_names:
            raise ValueError('You must provided a list of hk names')
        for elt in hk_names:
            if not isinstance(elt, str):
                raise ValueError('There is an incorrect value in the list '
                                 'of hk names provided')
        return hk_names

    def implement_table_attr(self):
        """
        Implement the attributes.
        """
        return {
            'time': datetime,
            'band': str,
            'value': object
        }

    def get_payload(self):
        """
        Return the payload to send with the request.
        """
        return {
            'hk_names': self.names,
            'db_model': 'housekeeping',
            'payload': self.payload_queries
        }
