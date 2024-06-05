"""
Methods for retrieving duties data in the eic database
"""
from datetime import datetime
from eic_db_request.query._utils import _check_time, _query_eic_db


def get_shifts_by_time(start_datetime: datetime, end_datetime: datetime) -> dict[str, str | dict]:
    """
    Queries the EIC database to get the shifts between a start and end date.

    :param start_datetime: The lower bound of the date range.
    :param end_datetime: The upper bound of the date range.
    :return: List of shifts as dictionary. Each shift provide a start date, an end date,
    the main user, and the backup user information
    """
    _check_time(start_datetime, end_datetime)
    server_response = _query_eic_db(endpoint='/api/internal/shifts/list',
                                    method='GET',
                                    query_params={
                                        "from": datetime.strftime(start_datetime, '%Y-%m-%d'),
                                        "to": datetime.strftime(end_datetime, '%Y-%m-%d')})
    resp = server_response.json()
    if resp['status'] == 'error':
        raise ValueError("An error occurred on eic-website: " + resp['content'])
    return resp['content']
