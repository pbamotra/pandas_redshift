from setuptools import setup

setup(
    name = 'pandas_redshift',
    packages = ['pandas_redshift'],
    version = '1.0.4',
    description = 'Load data from redshift into a pandas DataFrame and vice versa.',
    author = 'Aidan Gawronski',
    author_email = 'aidangawronski@gmail.com',
    # url = 'https://github.com/agawronski/pandas_redshift',
    python_requires = '>=3',
    install_requires = ['psycopg2',
                        'pandas',
                        'boto3']
)
