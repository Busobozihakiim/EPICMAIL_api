import os
class BaseConfig:
    DEBUG = False

class ProductionConfig(BaseConfig):
    DEBUG = False
    Testing = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    #DATABASE_URL = os.environ['DATABASE_URL']

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True
    #DATABASE_URL = os.environ['TEST_DB_URL']

configuration = {
    'production' : ProductionConfig,
    'development' : DevelopmentConfig,
    'testing' : TestingConfig
}