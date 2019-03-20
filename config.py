import os

class BaseConfig:
    DEBUG = False
    JWT_SECRET_KEY = os.environ['SECRET-KEY']

class ProductionConfig(BaseConfig):
    DEBUG = False
    Testing = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True

configuration = {
    'production' : ProductionConfig,
    'development' : DevelopmentConfig,
    'testing' : TestingConfig
}