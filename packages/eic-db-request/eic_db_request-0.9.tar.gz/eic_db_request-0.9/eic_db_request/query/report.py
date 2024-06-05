"""
Methods for retrieving report data in the eic database
"""
from eic_db_request.query_builder.query import Query
from eic_db_request.query_builder.reports import ReportQuery


def get_report_week_date(week_date: str) -> list[dict]:
    """
    Get report information from a provided week date.

    :param week_date: The week date of the report in format 'YYYY-WW' with WW for the week number.
    :return: A list with a report as dictionary.
    """
    with ReportQuery() as report:
        result = report.filter(Query('week_date', 'eq', week_date)).search_in_db()
    return result


def get_multiple_reports(week_dates: list[str]):
    """
    Get reports information for a given list of week dates.

    :param week_dates: A list of week dates of reports in format 'YYYY-WW'
    with WW for the week number.
    :return: A list of reports as dictionary.
    """
    with ReportQuery() as report:
        result = report.filter(Query('week_date', 'in', week_dates)).search_in_db()
    return result


def get_reports_between_period(start_week_date: str, end_week_date: str):
    """
    # TODO: is this really useful?
    Get report information for a provided week date range.

    :param start_week_date: The start week date in format 'YYYY-WW'
    with WW for the week number.
    :param end_week_date: The end week date in format 'YYYY-WW'
    with WW for the week number.
    :return: a list with report as dictionary
    """
    week_dates = [str(value) for value in range(int(start_week_date), int(end_week_date)+1)]
    with ReportQuery() as report:
        result = report.filter(Query('week_date', 'in', week_dates)) \
            .search_in_db()
    return result
