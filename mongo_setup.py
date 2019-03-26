from mongoengine import register_connection

HOST = 'mongodb+srv://fantaso:cmmaran1986@fantasocluster-rjehl.mongodb.net/test?retryWrites=true'


def database_init():
    register_connection(alias='main', host=HOST)
