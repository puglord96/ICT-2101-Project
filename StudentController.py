from Student import Student
from flask import Flask
from flask_mysqldb import MySQL #for flask-mysqldb
from Module import *
app = Flask(__name__)
# Database Config
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = '2101project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'

mysql = MySQL(app)

class StudentController:
    def __init__(self, UID):
        self.UID = UID

    def viewModule(self, type="", MID=1):
        # retrieve all modules from DB
        if type == "code":
            module = moduleList(self.UID).fetchModules()
        elif type == "name":
            module = moduleList(self.UID).getModuleName(MID)
        return module

    def viewFeedback(self):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM feedback f, user u WHERE FReceiver=" + self.UID + " AND f.FSender = u.UID;")
        data = cur.fetchall()

        return data

