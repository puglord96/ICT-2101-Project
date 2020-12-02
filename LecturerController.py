from Lecturer import Lecturer
from flask_mysqldb import MySQL #for flask-mysqldb
from flask import Flask

app = Flask(__name__)

# Database Config
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = '2101project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'

mysql = MySQL(app)


class LecturerController:
    def viewClass(self):
        pass
    def uploadStudent(self):
       pass

    def uploadMark(self):
        pass

    def viewStudentMark(self):
        pass

# Feedback will be a leaf of Lecturer
# Mods_teach will be a branch of Student
# Assessment next branch
# Followed by component
# Need methods to modify variables in webpages (update/insert values into db)
class Leaf:
    def __init__(self,obj):
        self.obj = obj
        pass