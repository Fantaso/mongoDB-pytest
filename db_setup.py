from os import environ

from mongoengine import register_connection

hosts = dict(
    prod=environ.get('MONGO_DB_PROD'),
    test=environ.get('MONGO_DB_TEST'),
)


def db_init(db_tag):
    if db_tag == 'prod':
        return register_connection(alias='main', host=hosts.get('prod'))
    elif db_tag == 'test':
        return register_connection(alias='main', host=hosts.get('test'))
