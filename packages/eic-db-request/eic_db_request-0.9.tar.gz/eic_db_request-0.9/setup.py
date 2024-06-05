from setuptools import setup

setup(
    name='eic-db-request',
    version='0.9',
    packages=['eic_db_request/config', 'eic_db_request/query', 'eic_db_request/query_builder'],
    install_requires=[
         'requests',
    ],
    author='EIC',
    description='This library is used to request the API to get '
                'informations stored in the EIC database.'
)
