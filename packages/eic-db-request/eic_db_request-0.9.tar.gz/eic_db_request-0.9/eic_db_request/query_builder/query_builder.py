"""
Abstract class for queryBuilder.
"""
from abc import ABCMeta, abstractmethod
import requests
from eic_db_request.config.config_eic import ConfigEic
from eic_db_request.query_builder.query import Query


class QueryBuilder(metaclass=ABCMeta):
    """
    Abstract class.
    """

    def __init__(self):
        """
        Constructor.
        """
        self.endpoint = '/api/internal/db_query'
        self.table_attr = self.implement_table_attr()
        self.payload_queries = []
        self._filters = []
        self._or_queries = []
        self._and_queries = []

    def __enter__(self):
        """
        Use a context manager.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit method of the context manager.
        """
        self.payload_queries = []
        self._filters = []
        self._or_queries = []
        self._and_queries = []

    def filter(self, query: Query):
        """
        Chain method that return the instance and add a new query tuple in the query filters.

        :param query: A Query object.
        :return: The object instance.
        """
        if not isinstance(query, Query):
            raise ValueError('Not a Query object.')
        query.valid_operator(self.table_attr)
        query.valid_prop_name(self.table_attr)
        self.property_already_used(query.prop_name)
        query_tuple = query.to_tuple()
        self._filters.append(query_tuple)
        self.payload_queries.append(('filter', query_tuple))
        return self

    def or_(self, queries: list[Query]):
        """
        Generate an "or" query to indicate multiple filter conditions.
        Chain method that return the instance and add a new list of queries in the "or" query.

        :param queries: A list of Query object.
        :return: The object instance.
        """
        for query in queries:
            if not isinstance(query, Query):
                raise ValueError('Not a Query object.')
            query.valid_prop_name(self.table_attr)
            query.valid_operator(self.table_attr)
            self.property_already_used(query.prop_name)
        or_tuple = [query.to_tuple() for query in queries]
        self._or_queries.append(or_tuple)
        self.payload_queries.append(('or', or_tuple))
        return self

    def and_(self, queries: list[Query]):
        """
        Generate an "and" query to indicate multiple filter conditions.
        Chain method that return the instance and add a new list of queries in the "and" query

        :param queries: A list of Query object.
        :return: The object instance.
        """
        for query in queries:
            if not isinstance(query, Query):
                raise ValueError('Not a Query object.')
            query.valid_prop_name(self.table_attr)
            query.valid_operator(self.table_attr)
            self.property_already_used(query.prop_name)
        and_tuple = [query.to_tuple() for query in queries]
        self._and_queries.append(and_tuple)
        self.payload_queries.append(('and', and_tuple))
        return self

    def property_already_used(self, property_name: str):
        """
        Check the consistency of the query chain.
        A model property can not be used in multiple queries.

        :param property_name: The name of the property to check.
        """
        # in filters
        if property_name in [query[0] for query in self._filters]:
            raise ValueError(f'The property "{property_name}" has already been used in a '
                             f'filter query')
        # in or queries
        flat_or_query = [query[0] for or_query in self._or_queries for query in or_query]
        if property_name in flat_or_query:
            raise ValueError(f'The property "{property_name}" has already been used in a '
                             f'"or" query')

        # in and queries
        flat_or_query = [query[0] for and_query in self._and_queries for query in and_query]
        if property_name in flat_or_query:
            raise ValueError(f'The property "{property_name}" has already been used in a '
                             f'"and" query')

    def search_in_db(self):
        """
        Make a request to search in the EIC database.
        """
        token = ConfigEic.get_instance().get_token()
        url = ConfigEic.get_instance().get_url() + self.endpoint
        response = requests.post(url=url,
                                 headers={"AUTHORIZATION": token},
                                 json=self.get_payload(),
                                 allow_redirects=True)
        # clean previous filters in case the context manager is not used.
        self.payload_queries = []
        self._filters = []
        self._or_queries = []
        self._and_queries = []
        if response.ok:
            resp = response.json()
            if resp['status'] == 'error':
                raise ValueError("An error occurred during the database searching: "
                                 + resp['content'])
            return resp['content']
        else:
            raise requests.HTTPError(f"HTTP error: {response.status_code} - {response.content}")

    @abstractmethod
    def get_payload(self):
        """
        Format the payload to send with the request.
        """

    @abstractmethod
    def implement_table_attr(self):
        """
        Indicates attributes of the model in self.attr.
        """
