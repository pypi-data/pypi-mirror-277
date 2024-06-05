"""
Methods for retrieving HouseKeeping data in the eic database
"""
from datetime import datetime
from eic_db_request.query._utils import _check_time, _query_eic_db
from eic_db_request.query_builder.hk import HouseKeepingQuery
from eic_db_request.query_builder.query import Query


def get_hk_values_by_time(hk_name: str, start_datetime: datetime, end_datetime: datetime) -> list[dict]:
    """
    Queries the EIC database to get the HK with the given parameters.

    :param hk_name: The name of the HK.
    :param start_datetime: The lower bound of the date range.
    :param end_datetime: The upper bound of the date range.
    :return: List of HK as dict with 'time' and 'value' as keys to access the associated data
    ordered by time.
    """
    _check_time(start_datetime, end_datetime)
    with HouseKeepingQuery([hk_name]) as hk:
        result = hk \
            .and_([Query('time', 'le', end_datetime),
                   Query('time', 'ge', start_datetime)]) \
            .search_in_db()
    return result


def get_multiple_hks_by_time(list_hk_names: list[str], start_datetime: datetime,
                             end_datetime: datetime) -> dict[str, list]:
    """
    Queries the EIC database to get the all values in a period of time for all HouseKeepings
    names provided.

    :param list_hk_names: A list of HK names.
    :param start_datetime: The lower bound of the date range.
    :param end_datetime: The upper bound of the date range.
    :return: A dictionary with the HK name as key and a list of HK value as value.
        Each value is a dict with 'time' and 'value' as keys to access the associated data.
    """
    _check_time(start_datetime, end_datetime)
    with HouseKeepingQuery(list_hk_names) as hk:
        result = hk \
            .and_([Query('time', 'le', end_datetime),
                   Query('time', 'ge', start_datetime)]) \
            .search_in_db()
    return result


def get_inferior_hk_value_by_time(hk_name: str, start_datetime: datetime, end_datetime: datetime,
                                  value_limits: int | float) -> dict[str | list]:
    """
    Queries the EIC database to get the all values inferior to the value limits
    in a period of time for the HouseKeeping name provided.

    :param hk_name: The name of the HK.
    :param start_datetime: The lower bound of the date range.
    :param end_datetime: The upper bound of the date range.
    :param value_limits: The upper value limits.
    :return: A dictionary with the HK name as key and a list of HK value as value.
        Each value is a dict with 'time' and 'value' as keys to access the associated data
    """
    if not isinstance(hk_name, str):
        raise ValueError('You must provide a valid hk name')
    _check_time(start_datetime, end_datetime)
    with HouseKeepingQuery([hk_name]) as hk:
        result = hk \
            .and_([Query('time', 'lt', end_datetime),
                   Query('time', 'gt', start_datetime)]) \
            .filter(Query('value', 'lt', value_limits)) \
            .search_in_db()
    return result
