# from  pymysql import connections
import os
#import boto3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return ("Hello Sanjay")
if __name__=='__main__':
        app.run(host='0.0.0.0',port=8080,debug=True)