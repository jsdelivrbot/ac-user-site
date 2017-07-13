class Config(object):
    DEBUG = False
    SECRET_KEY = 'secret'


class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True