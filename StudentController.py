from Student import Student
from flask_mysqldb import MySQL #for flask-mysqldb
import mysql.connector
from mysql.connector import errorcode

# Test DB connector
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='2101project')
cursor = cnx.cursor()

query =("SELECT * FROM user where isStudent = 1 AND UID = 1901000")
cursor.execute(query)

for user in cursor:
    pass
    #print(user)
cursor.close()
cnx.close()

class StudentController:
    def viewModule(self):
        pass
        # retrieve all modules from DB

    def viewAssessment(self):
        pass
        # with the modules collected, view all assessments from DB

    def viewComponent(self):
        pass
        # with assessments collected, view all components (with weightage and grade)


