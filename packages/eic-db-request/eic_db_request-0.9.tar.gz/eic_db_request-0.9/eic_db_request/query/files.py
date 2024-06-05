"""
Utils methods to handle svo-orb, svo-att and calibration files
"""
import os.path
from datetime import datetime
from typing import Any
from eic_db_request.query._utils import _check_time, _query_eic_db
from eic_db_request.query_builder.calibration import CalibrationQuery
from eic_db_request.query_builder.orbito_file import OrbitoFileQuery
from eic_db_request.query_builder.query import Query


def _check_filetype(file_type: str):
    """
    Verify that the file type provided match handled file type for the API.

    :param file_type: The file type to check.
    """
    available_types = ('calibration', 'svo')
    if file_type not in available_types:
        raise ValueError(f'The file must be one of this type: {available_types}')


def get_available_svo_files(start_datetime: datetime, end_datetime: datetime, filetype: str) \
        -> list[dict]:
    """
    Queries the EIC database to get the available files between a start and end date and for a type.

    :param start_datetime: The lower bound of the date range.
    :param end_datetime: The upper bound of the date range.
    :param filetype: The type of the file, 'svo-orb' or 'svo-att'.
    :return: List of files as dictionary.
    """
    if filetype not in ('svo-orb', 'svo-att'):
        raise ValueError('You must provide the type of the file: svo-orb or svo-att')
    _check_time(start_datetime, end_datetime)
    server_response = _query_eic_db(endpoint='/api/internal/file/available_files',
                                    method='POST',
                                    query_params={
                                        'filetype': filetype,
                                        'from': start_datetime.isoformat(),
                                        'to': end_datetime.isoformat()})
    resp = server_response.json()
    if resp['status'] == 'error':
        raise ValueError(resp['content'])
    return resp['content']


def get_available_calibration_files(start_validity: datetime = None, creation_date: datetime = None,
                                    upload_date: datetime = None, extension: str = None,
                                    file_extension_type: str = None) \
        -> list[dict]:
    """
    Make a query to the eic-website to search for calibration files.
    All parameters are optionals but at least, one of them must be provided.

    :param start_validity: The minimum date of validity of the calibration file.
    :param creation_date: The minimum creation date of the file.
    :param upload_date: The minimum upload date of the file.
    :param extension: The calibration file extension, yml or fits.
    :param file_extension_type: The file extension ('yml', 'fits', 'jttc' or 'xml').
    """
    if (file_extension_type is not None and
            file_extension_type not in ('yml', 'fits', 'jttc', 'xml')):
        raise ValueError('The extension provided is not correct. Must be yml or fits')
    provided_params = {arg_name: _iso_date(value) for arg_name, value in locals().items() if
                       value is not None}
    if not provided_params:
        raise ValueError('You must set at least one parameter to search for calibration files')
    server_response = _query_eic_db(endpoint='/api/internal/calibration/available_files',
                                    method='POST',
                                    query_params=provided_params)
    resp = server_response.json()
    if resp['status'] == 'error':
        raise ValueError(resp['content'])
    return resp['content']


def download_file(file_type: str, filename: str, save_filepath: str) -> str:
    """
    Download the file from eic-website and save it into the filepath provided.

    :param file_type: The type of the file, 'calibration' or 'svo'.
    :param filename: The name of the file to download.
    :param save_filepath: The filepath where to save the file.
    :return: The filepath of the saved file.
    """
    if not os.path.exists(save_filepath):
        raise OSError('The filepath provided doesn\'t exist. Please, '
                      'create it before call this method')
    _check_filetype(file_type)
    endpoint_file = {
        'calibration': '/api/internal/calibration/download',
        'svo': '/api/internal/file/download'}.get(file_type)
    server_response = _query_eic_db(endpoint=endpoint_file,
                                    method='GET',
                                    query_params={'filename': filename})
    if 'json' in server_response.headers.get('Content-Type'):
        resp = server_response.json()
        raise ValueError(resp['content'])
    destination = os.path.join(save_filepath, filename)
    with open(destination, 'wb') as file:
        file.write(server_response.content)
    return destination


def get_orbito_files_min_max_orbit(min_orbit_number: int, max_orbit_number: int) -> list:
    """
    Queries the EIC database to get the available orthography files between an orbit range.

    :param min_orbit_number: The lower bound of the orbit range.
    :param max_orbit_number: The upper bound of the orbit range.
    :return: List of files as dictionary.
    """
    with OrbitoFileQuery() as orbito:
        result = orbito.and_([Query('min_orbit', 'ge', min_orbit_number),
                              Query('max_orbit', 'le', max_orbit_number)]).search_in_db()

    return result


def get_calibration_files_sending_crestdb_between(start_datetime: datetime, end_datetime: datetime) \
        -> list[dict]:
    """
    Get all calibration with a send date to the CrestDB between a start and an end date.

    :param start_datetime: The lower bound of the date range.
    :param end_datetime: The upper bound of the date range.
    :return: A list of calibration files as dictionaries.
    """
    with CalibrationQuery() as calibration:
        result = calibration.and_([Query('sending_date_crestdb', 'ge', start_datetime),
                                   Query('sending_date_crestdb', 'le', end_datetime)]).search_in_db()
    return result


def get_calibration_files_sending_caldb_between(start_datetime: datetime, end_datetime: datetime) \
        -> list[dict]:
    """
    Get all calibration with a send date to the CalDB between a start and an end date.

    :param start_datetime: The lower bound of the date range.
    :param end_datetime: The upper bound of the date range.
    :return: A list of calibration files as dictionaries.
    """
    with CalibrationQuery() as calibration:
        result = calibration.and_([Query('sending_date_caldb', 'ge', start_datetime),
                                   Query('sending_date_caldb', 'le', end_datetime)]).search_in_db()
    return result


def _iso_date(value: Any) -> str:
    """
    If the value is a datetime object, convert it in iso format.

    :param value: The date value to test.
    :return: The date value in string iso format.
    """
    if isinstance(value, datetime):
        value = value.isoformat()
    return value
