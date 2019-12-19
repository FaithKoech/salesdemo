import os

class Development():
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Ann@2020@127.0.0.1:5432/salesdemo'
    SECRET_KEY = '11ae8fcaceff9710e238b932e95072a1'
    DEBUG = True