import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sqlv2xserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'sqlv2x'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqlv2xadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '6782166137Tom'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'utilityv2xstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'le1SYnDACUxZunqNSDF0Im0UY8x8dlDoT/kh7ZOjyZSkl+W1RYl8isothP0rz/esINAxm0C5mZo/+AStqaRGcw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'sdvreport'
