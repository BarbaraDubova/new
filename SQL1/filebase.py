import mysql.connector

try:
    config = {
        'host' : 'localhost',
        'user' : 'barbaradub',
        'password': '10AGETTTlflflf',
        'database': 'barbaradub'
    }
    print('successfully connected...')
except Exception as ex:
    print('connection refused')
    print(ex)


