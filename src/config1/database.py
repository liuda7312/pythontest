import os
basedir=os.path.abspath(os.path.dirname(__file__))
class Config:
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG=True
    DB="mydayabase"
    USER="root"
    PASSWORD="root"
    POST="3306"
    CHARSET="utf8"
config={
    'developmet':DevelopmentConfig
}