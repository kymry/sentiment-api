import os
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.abspath('.'), '.env'))
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DATABASE']
port = os.environ['MYSQL_PORT']


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or "6IxOGEa58UtIzWujwoTAIzzsb832OcLmr8V-mNSBoA4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
