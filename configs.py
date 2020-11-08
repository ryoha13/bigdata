

class Config(object):
    SECRET_KEY = 'a random string'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class ProConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
    TESTING = True


configs = {
    'dev': DevConfig,
    'pro': ProConfig,
    'test': TestConfig,
    'default': DevConfig
}