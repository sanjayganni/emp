#from pymysql import connections
import os
#import boto3
#from config import *
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('Home.html')
if __name__ =='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)