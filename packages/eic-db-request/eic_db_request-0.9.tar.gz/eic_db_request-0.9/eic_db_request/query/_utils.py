"""
Common methods useful in multiple packages. Should not be called directly.
"""
from datetime import datetime
import requests
from requests import Response
from ..config.config_eic import ConfigEic


def _query_eic_db(endpoint: str, method: str, query_params: dict = None) -> Response:
    """
    Generic method to query the EIC database.

    :param endpoint: The endpoint of the URL.
    :param method: The HTTP method to use ('GET' or 'POST')
    :param query_params: The parameters to pass to the request.
    :return: The response of the request.
    """
    token = ConfigEic.get_instance().get_token()
    url = ConfigEic.get_instance().get_url() + endpoint
    if method == 'POST':
        response = requests.post(url=url,
                                 headers={"AUTHORIZATION": token},
                                 json=query_params,
                                 allow_redirects=True)
    else:  # GET
        response = requests.get(url=url,
                                headers={"AUTHORIZATION": token},
                                params=query_params,
                                allow_redirects=True)
    if response.ok:
        return response
    else:
        raise requests.HTTPError(f"HTTP error: {response.status_code} - {response.content}")


def _check_time(start_time: datetime, end_time: datetime):
    """
    Checks validity of start time and end time of the interval.
    Raise ValueError if end time < start time.

    :param start_time: The start time of the date range.
    :param end_time: The end time of the date range.
    :return: Nothing.
    """
    if not isinstance(start_time, datetime) or not isinstance(end_time, datetime):
        raise ValueError("Error: The start_time and end_time must be a datetime.datetime object")
    if end_time < start_time:
        raise ValueError("Error: start_time should be lower than end_time.")
