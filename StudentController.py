from Student import Student
from flask import Flask
from flask_mysqldb import MySQL #for flask-mysqldb
#import mysql.connector
#from mysql.connector import errorcode

app = Flask(__name__)
# Database Config
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = '2101project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'

mysql = MySQL(app)
# Test DB connector
# cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='2101project')
# cursor = cnx.cursor()
#
# query =("SELECT * FROM user where isStudent = 1 AND UID = 1901000")
# cursor.execute(query)
#
# for user in cursor:
#     pass
#     #print(user)
# cursor.close()
# cnx.close()

class StudentController:
    def __init__(self, UID):
        self.UID = UID


    def viewModule(self):
        pass
        # retrieve all modules from DB

    def viewAssessment(self):
        pass
        # with the modules collected, view all assessments from DB

    def viewComponent(self):
        pass
        # with assessments collected, view all components (with weightage and grade)

    def viewFeedback(self):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM feedback WHERE FReceiver=" + self.UID)
        data = cur.fetchall()

        return data

