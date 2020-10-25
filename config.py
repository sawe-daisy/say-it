import os

class Config:
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:sawedaisy@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # @staticmethod
    # def init_app(app):
    #     pass
    

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:sawedaisy@localhost/pitches'
    DEBUG = True



config_options = {
'development':DevConfig,
'production':ProdConfig,
'test': TestConfig
}