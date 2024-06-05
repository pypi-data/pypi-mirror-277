"""
Methods for retrieving events data in the eic database
"""
from datetime import datetime
from eic_db_request.query._utils import _check_time
from eic_db_request.query_builder.events import EventsQuery
from eic_db_request.query_builder.query import Query


def get_events_by_time(start_datetime: datetime, end_datetime: datetime) -> list[EventsQuery]:
    """
    Get all events during a period of time

    :param start_datetime: The start date of the events.
    :param end_datetime: The end date of the events.
    :return: The list of events during the date range if found, else an empty list.
    """
    _check_time(start_datetime, end_datetime)
    with EventsQuery() as events:
        result = events \
            .and_([Query('time', 'ge', start_datetime), Query('time', 'le', end_datetime)]) \
            .search_in_db()
    return result


def get_events_by_report_id(report_id: int) -> list[EventsQuery]:
    """
    Get all events for a provided report id.

    :param report_id: The report ID.
    :return: The list of events if found, else an empty list.
    """
    with EventsQuery() as events:
        result = events.filter(Query('report_id', 'eq', report_id)).search_in_db()
    return result


def get_warnings_by_time(start_datetime: datetime, end_datetime: datetime) -> list[EventsQuery]:
    """
    Get all events categorized as 'warnings' during a period of time.

    :param start_datetime: The start date of the events.
    :param end_datetime: The end date of the events.
    :return: The list of events during the date range if found, else an empty list.
    """
    _check_time(start_datetime, end_datetime)
    with EventsQuery() as events:
        result = events \
            .and_([Query('time', 'ge', start_datetime), Query('time', 'le', end_datetime)]) \
            .filter(Query('is_alarm', 'eq', False)) \
            .search_in_db()
    return result


def get_alarms_by_time(start_datetime: datetime, end_datetime: datetime) -> list[EventsQuery]:
    """
    Get all events categorized as 'alarms' during a period of time.

    :param start_datetime: The start date of the events.
    :param end_datetime: The end date of the events.
    :return: The list of events during the date range if found, else an empty list.
    """
    _check_time(start_datetime, end_datetime)
    with EventsQuery() as events:
        result = events \
            .and_([Query('time', 'ge', start_datetime), Query('time', 'le', end_datetime)]) \
            .filter(Query('is_alarm', 'eq', True)) \
            .search_in_db()
    return result
