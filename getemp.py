from flask import Flask, render_template, request
from pymysql import connections
import os
#import boto3
from config import *
app = Flask(__name__)

db_conn = connections.Connection(
host=customhost,
port=3306,
user=customuser,
password=custompass,
db=customdb
)
cursor = db_conn.cursor()

#output = {}

@app.route("/",methods=['GET','POST'])
def home():
    return render_template('Home.html')

@app.route("/Getemp",methods=['POST'])
def Getemp():
    cursor.execute("select * from employee")
    value = cursor.fetchall()
    return render_template('Output.html',data=value,name='All')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)












