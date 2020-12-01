from Lecturer import Lecturer
from flask_mysqldb import MySQL #for flask-mysqldb
import mysql.connector
from mysql.connector import errorcode
# Test DB connector
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='2101project')
cursor = cnx.cursor()

query =("SELECT * FROM user where isStudent = 0")
cursor.execute(query)

for user in cursor:
    print(user)

cursor.close()
cnx.close()


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