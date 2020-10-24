import os

class Config:
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:sawedaisy@localhost/pitches'
   
    

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