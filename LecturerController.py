#from flask_mysqldb import MySQL
import mysql.connector
from mysql.connector import errorcode
# Test DB connector
cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='2x01')
cursor = cnx.cursor()

query =("SELECT * FROM user")

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
