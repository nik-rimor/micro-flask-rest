# services/users/project/config.py


import os


class BaseConfig:
    """Base Configuration."""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'


class DevelopmentConfig(BaseConfig):
    """Development Configuaration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(BaseConfig):
    """Development Configuaration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """Development Configuaration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
