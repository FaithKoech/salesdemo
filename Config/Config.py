import os

class Development():
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Ann@2020@127.0.0.1:5432/salesdemo'
    SECRET_KEY = '11ae8fcaceff9710e238b932e95072a1'
    DEBUG = True

class Production():
    SQLALCHEMY_DATABASE_URI = 'postgres://tjcxzfefuqnshi:ac9cf96a0c03af7cb0f75a3ec8afc60d4e1c0e3df179c44c7f9a70ffc78c096e@ec2-54-246-100-246.eu-west-1.compute.amazonaws.com:5432/de0oi93cqf9vrm'
    SECRET_KEY = '11ae8fcaceff9710e238b932e95072a1'
    DEBUG = False