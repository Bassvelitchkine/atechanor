import os
from dotenv import load_dotenv
load_dotenv()


class Config():
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


class DevelopmentConfig(Config):
    DEBUG = True
    DOWNLOAD_DOMAIN = "http://192.168.99.100"


class ProductionConfig(Config):
    DOWNLOAD_DOMAIN = "http://192.168.99.100"
