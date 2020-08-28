from flask import Flask
import mysql.connector
import os
import config


app=Flask(__name__)
app.config['SECRET_KEY']=config.key['FLASK_SECRET_KEY']


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9990)