# Presentation
This project contains the *eic-db-request* library, used to perform data retrieval queries on the EIC database.
In particular, it allows you to retrieve events, shifts and HKs data, as well as stored files (reports, fits calibration, orbito).
It has been developed in Python 3.10.

# Installation
You can install the library directly from the PyPi repository with:
```bash
pip install eic-db-request
```

Or you can install it from the cloned repository:
```
git clone git@gitlab1.irap.omp.eu:EIC/eic-db-request.git
pip install -e the/path/to/the/project
```

# Usage
Before you can use the library, you must first initialize the configuration with *ConfigEic.init(use_env=True, token: str, url: str)*.
This function contains 3 parameters:
- *use_env*: Specifies whether to use the environment variable for the token.
- *token*: The token value used for authorization.
- *url*: The URL of the eic-website to do the query. Do not include the /api part.

If the parameter *use_env* is set to True, it will search to the **EIC_TOKEN** variable in your environment and so you don't have to specify the token manually.

In this example, we don't use environment variables and to specify the token manually, directing our requests to the development website and database:
```
from eic_db_request.config.config_eic import ConfigEic
ConfigEic.init(use_env=False, token='your_personal_token', url='https://eic-dev.irap.omp.eu')
```

## Events
```
from eic_db_request.query import events
```

After initializing the configuration and importing the *events* module (see above), the events can be extracted with 4 functions;

- *get_events_by_time(start_datetime: datetime, end_datetime: datetime)* retrieves a list of events within a date range.

```
from datetime import datetime
events_list = events.get_events_by_time(start_datetime=datetime(2024, 1, 1, 12, 30, 0), end_datetime=datetime(2024, 1, 1, 12, 30, 0))
```

- *get_events_by_report_id(report_id: int)* retrieves the list of events associated with a report ID.

```
events_list = events.get_events_by_report_id(report_id=1)
```

- *get_warnings_by_time(start_datetime: datetime, end_datetime: datetime)* retrieves all events classified as "warnings" within a date range.

```
events_list = events.get_warnings_by_time(start_datetime=datetime(2024, 1, 1, 12, 30, 0), end_datetime=datetime(2024, 1, 1, 12, 30, 0))
```

- *get_alarms_by_time(start_datetime: datetime, end_datetime: datetime)* retrieves all events classified as "alarms" within a date range.

```
events_list = events.get_alarms_by_time(start_datetime=datetime(2024, 1, 1, 12, 30, 0), end_datetime=datetime(2024, 1, 1, 12, 30, 0))
```

All results returned will be in the form of a list of dictionaries:
```
>>> print(events_list)
[{'alarm_value': 'ALARM', 'band_name': 'VHF', 'handled_by_user': {'email': None, 'firstname': None, 'lastname': None}, 'hk_name': 'ECL_VP_NREC1CATIPIX', 'id': 5480950, 'report_id': None, 'status': 'new', 'time': '2024-03-18T04:37:57', 'value': '58'}, 
 {'alarm_value': 'ALARM', 'band_name': 'VHF', 'handled_by_user': {'email': None, 'firstname': None, 'lastname': None}, 'hk_name': 'ECL_VP_NREC1CATJPIX', 'id': 5480951, 'report_id': None, 'status': 'new', 'time': '2024-03-18T04:37:57', 'value': '142'}]
```


## Files
```
from eic_db_request.query import files
```
After initializing the configuration and importing the *files* module (see above), files can be listed with 5 different functions;

- *get_available_svo_files(start_datetime: datetime, end_datetime: datetime, filetype: str)* extracts orbitography or attitude files for a date range.
The parameter *filetype* must be 'svo-orb' or 'svo-att'.

```
files_list = files.get_available_svo_files(start_datetime=datetime(2023, 1, 1), end_datetime=datetime(2024, 1, 2), filetype='svo-att')
```

Output example:
```
>>> print(att_files_list)
[{'from': '2024-03-20', 'name': 'SVO-ATT-CNV_2024-03-20T00:59:28.000_2024-03-20T01:39:19.000.csv', 'to': '2024-03-20'}, 
 {'from': '2024-03-15', 'name': 'SVO-ATT-CNV_2024-03-15T00:59:27.000_2024-03-15T01:39:18.000.csv', 'to': '2024-03-15'}, 
 {'from': '2024-03-08', 'name': 'SVO-ATT-CNV_2024-03-08T00:59:28.000_2024-03-08T01:39:19.000.csv', 'to': '2024-03-08'}]
```
---

- *get_available_calibration_files(start_validity: datetime = None, creation_date: datetime = None, upload_date: datetime = None, extension: str = None)* extracts calibration files depending on various parameters.
*start_validity* refers to the TSTART value, *upload_date* to its upload on the eic-website, *extension* to the EXTNAME keyword value and *file_extension_type* is the file extension type ('yml', 'fits', 'jttc' or 'xml').

```
files_list = files.get_available_calibration_files(start_validity=datetime(2024, 1, 2), extension='AUX-ECL-SAA-DEF', file_extension_type='fits')
```

Output example:
```
>>> print(files_list)
[{'creation_date': '2022-11-15', 'description': 'ECL FLIGHT LIMITS OF ENERGY BAND', 'extension': 'AUX-ECL-BND-CAL', 'file_extension_type': 'fits', 'name': 'AUX-ECL-BND-CAL-20221011F01.fits', 'start_validity': '2022-10-11T12:00:00', 'upload_date': '2024-02-14T16:47:53'}, 
 {'creation_date': '2022-11-15', 'description': 'ECL GROUND GAIN/OFFSET', 'extension': 'AUX-ECL-PIX-CAL', 'file_extension_type': 'fits', 'name': 'AUX-ECL-PIX-CAL-20221011F01.fits', 'start_validity': '2022-10-11T12:00:00', 'upload_date': '2024-03-20T16:28:07'}]
```

---

- *get_orbito_files_min_max_orbit(min_orbit_number: int, max_orbit_number: int)* lists orbitography files for a given orbit numbers range.

```
files_list = files.get_orbito_files_min_max_orbit(min_orbit_number=1, max_orbit_number=10)
```
Output example:
```
>>> print(files_list)
[{'id': 1, 'max_orbit': 12, 'min_orbit': 12, 'mjd_ref': 57754.0, 'name': 'SVO-ORB-CNV_2024-03-20T00:59:28.000_2024-03-20T01:39:19.000.csv', 'tstart': '2024-03-20'}, 
 {'id': 2, 'max_orbit': 12, 'min_orbit': 12, 'mjd_ref': 57754.0, 'name': 'SVO-ORB-CNV_2024-03-15T00:59:27.000_2024-03-15T01:39:18.000.csv', 'tstart': '2024-03-15'}]
```

---

- *get_calibration_files_sending_crestdb_between(start_datetime: datetime, end_datetime: datetime)* extracts all the calibration files sent to the CrestDB between a date range.

```
files_list = files.get_calibration_files_sending_crestdb_between(start_datetime=datetime(2024, 1, 1), end_datetime=datetime(2024, 1, 2))
```

Output example:
```
>>> print(files_list)
[{'creation_date': '2024-02-14', 'description': 'A DPIX_EBANDS JTTC file generated from the DPIX_EBANDS-V24021401.yml file.', 'extension': 'DPIX_EBANDS', 'file_extension_type': 'jttc', 'id': 19, 'name': 'DPIX_EBANDS-V2402141.jttc', 'sending_date_caldb': None, 'sending_date_crestdb': '2023-03-01', 'start_validity': '2024-02-14T17:46:10.828577', 'upload_date': '2024-02-14T17:46:13'}]
```

- *get_calibration_files_sending_caldb_between(start_datetime: datetime, end_datetime: datetime)* extracts all the calibration files sent to the CalDB between a date range.

```
files_list = files.get_calibration_files_sending_caldb_between(start_datetime=datetime(2024, 1, 1), end_datetime=datetime(2024, 1, 2))
```

Output example:
```
>>> print(files_list)
[{'creation_date': '2022-11-15', 'description': 'ECL GROUND GAIN/OFFSET', 'extension': 'AUX-ECL-PIX-CAL', 'file_extension_type': 'fits', 'id': 34, 'name': 'AUX-ECL-PIX-CAL-20221011F01.fits', 'sending_date_caldb': '2023-03-01', 'sending_date_crestdb': None, 'start_validity': '2022-10-11T12:00:00', 'upload_date': '2024-03-20T16:28:07'}]
```

All results returned will be in the form of a list of dictionaries.

To download on your computer the files listed previously, you can use the *download_file(file_type: str, filename: str, save_filepath: str)* function. It allows to retrieve and save the file on a given path.
*file_type* refers to the type of the file ('calibration' or 'svo'), *filename* to the name given to the downloaded file and *save_filepath* the filepath where save the file.
```
for file in files_list:
    download_file(file_type='calibration', filename=file.filename, save_filepath='/home/me/%s' % file.filename)
```


## HKs
```
from eic_db_request.query import hk
```
After initializing the configuration and importing the *hk* module (see above), HKs can be extracted with 3 different functions;

- *get_hk_values_by_time(hk_name: str, start_datetime: datetime, end_datetime: datetime)* extracts data of an HK for a date range.

```
hks = hk.get_hk_values_by_time(hk_name='ECL_CBNRI', start_datetime=datetime(2024, 1, 1), end_datetime=datetime(2024, 1, 2))
```
Output example:
```
>>> print(hks)
{'ECL_CBNRI': 
 [{'time': 'Tue, 02 Jan 2024 03:59:58 GMT', 'value': 0.0, 'band': 'X band'}, 
 {'time': 'Tue, 02 Jan 2024 03:59:59 GMT', 'value': 0.0, 'band': 'X band'}, 
 {'time': 'Tue, 02 Jan 2024 04:00:00 GMT', 'value': 0.0, 'band': 'X band'}, 
 {'time': 'Tue, 02 Jan 2024 04:00:01 GMT', 'value': 0.0, 'band': 'X band'}]
}
```

---

- *get_multiple_hks_by_time(list_hk_names: list[str], start_time: datetime, end_time: datetime)* extracts date of multiples HKs for a date range.

```
hks = hk.get_multiple_hks_by_time(list_hk_names=['DPIX_VCTRLHVELS6', 'DPIX_VCTRLHVELS7'], start_datetime=datetime(2024, 1, 1), end_datetime=datetime(2024, 1, 2))
```
Output example:
```
>>> print(hks)
{'DPIX_VCTRLHVELS6':
 [{'band': 'Band X', 'time': '2022-01-02T03:59:52.101000', 'value': 1.0}, 
 {'band': 'Band X', 'time': '2022-01-02T03:59:54.101000', 'value': 0.3}],
'DPIX_VCTRLHVELS7':
 [{'band': 'Band X', 'time': '2022-01-02T03:59:56.101000', 'value': 1.0}, 
 {'band': 'Band X', 'time': '2022-01-02T03:59:58.101000', 'value': 0.1}]
}
```

---

- *get_inferior_hk_value_by_time(hk_name: str, start_datetime: datetime, end_datetime: datetime, value_limits: int | float)* extracts data of an HK for a date range and an upper threshold value.

```
hks = hk.get_inferior_hk_value_by_time(hk_name='ECL_TEMPTH01', start_datetime=datetime(2024, 1, 1), end_datetime=datetime(2024, 1, 2), value_limits=100)
```
Output example:
```
>>> print(hks)
{'ECL_TEMPTH01': 
 [{'time': 'Mon, 01 Jan 2024 03:59:58 GMT', 'value': 25.0, 'band': 'X band'}, 
 {'time': 'Mon, 01 Jan 2024 03:59:59 GMT', 'value': 25.1, 'band': 'X band'}, 
 {'time': 'Mon, 01 Jan 2024 04:00:00 GMT', 'value': 25.7, 'band': 'X band'}, 
 {'time': 'Mon, 01 Jan 2024 04:00:01 GMT', 'value': 26.0, 'band': 'X band'}]
}
```


## Report
```
from eic_db_request.query import report
```

After initializing the configuration and importing the *report* module (see above), reports can be extracted with 3 functions;

- *get_report_week_date(week_date: str)* returns the report for a given week date.
The *week_date* refers to the year and week number in the 'YYYY-WW' format.

```
reports = report.get_report_week_date(week_date='2024-02')
```
Output example:
```
>>> print(reports)
[{'comment_friday': None, 'comment_monday': None, 'comment_saturday': None, 'comment_sunday': None, 'comment_thursday': None, 'comment_tuesday': None, 'comment_wednesday': None, 'global_comment': None, 'id': 1, 'is_generated': False, 'week_date': '2024-02'}]
```

---

- *get_multiple_reports(week_dates: list[str])* returns a list of reports for a given list of week dates.
The week_date refers to the year and week number in the 'YYYY-WW' format.

```
reports = report.get_multiple_reports(week_dates=['2024-01', '2024-02'])
```
Output example:
```
>>> print(reports)
[{'comment_friday': None, 'comment_monday': None, 'comment_saturday': None, 'comment_sunday': None, 'comment_thursday': None, 'comment_tuesday': None, 'comment_wednesday': None, 'global_comment': None, 'id': 1, 'is_generated': False, 'week_date': '2024-02'}, 
{'comment_friday': None, 'comment_monday': None, 'comment_saturday': None, 'comment_sunday': None, 'comment_thursday': None, 'comment_tuesday': None, 'comment_wednesday': None, 'global_comment': None, 'id': 2, 'is_generated': False, 'week_date': '2024-01'}]
```

---

- *get_reports_between_period(start_week_date: str, end_week_date: str)* returns a list of reports for a given date range.

```
reports = report.get_reports_between_period(start_week_date='2024-01', end_week_date='2024-02')
```
Output example:
```
>>> print(reports)
[{'comment_friday': None, 'comment_monday': None, 'comment_saturday': None, 'comment_sunday': None, 'comment_thursday': None, 'comment_tuesday': None, 'comment_wednesday': None, 'global_comment': None, 'id': 1, 'is_generated': False, 'week_date': '2024-02'}, 
{'comment_friday': None, 'comment_monday': None, 'comment_saturday': None, 'comment_sunday': None, 'comment_thursday': None, 'comment_tuesday': None, 'comment_wednesday': None, 'global_comment': None, 'id': 2, 'is_generated': False, 'week_date': '2024-01'}]
```

## Shifts
```
from eic_db_request.query import shifts
```
After initializing the configuration and importing the *shifts* module (see above), shifts can be extracted with a function:

*get_shifts_by_time(start_datetime: datetime, end_datetime: datetime)* extracts shifts for a given date range.

```
shifts_list = shifts.get_shifts_by_time(start_datetime=datetime(2024, 1, 1), end_datetime=datetime(2024, 2, 1))```
```

All results returned will be in the form of a list of dictionaries:
```
>>> print(shifts_list)
[{'backup': {'email': 'ba@eic.org', 'firstname': 'Burst', 'lastname': 'Advocate', 'status': 'dev'}, 'from': '2024-01-01', 'main': {'email': 'is@eic.org', 'firstname': 'Instrument', 'lastname': 'Scientist', 'status': 'dev'}, 'to': '2024-01-07'}, 
{'backup': {'email': 'adm_sys@eic.org', 'firstname': 'System', 'lastname': 'Administrator', 'status': 'dev'}, 'from': '2024-01-08', 'main': {'email': 'ba@eic.org', 'firstname': 'Burst', 'lastname': 'Advocate', 'status': 'dev'}, 'to': '2024-01-14'}]
```
