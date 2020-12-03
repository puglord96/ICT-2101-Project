from Lecturer import Lecturer
from flask_mysqldb import MySQL #for flask-mysqldb
from flask import Flask
from Feedback import *
import csv
import os

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
    def __init__(self, UID):
        self.UID = UID

    def viewClass(self):
        studList = []
        cur = mysql.connection.cursor()

        # Get Results of Students if any
        cur.execute("SELECT RID, UID, marks, CID FROM result")
        resultdata = cur.fetchall()

        # View students that are taking the module
        #cur.execute("SELECT user.UID, user.name, user.email, module.mod_code FROM user INNER JOIN module ON user.UID = module.UID WHERE isStudent = 1;")
        #data = cur.fetchall()

        return resultdata
    def giveFb(self, FID, Ftype, FTitle, FContent, FSender, FReceiver, FMod_code ):
        try:
            cur = mysql.connection.cursor()

            # sql = "INSERT INTO feedback (FID, FType, FTitle, FContent, FSender, FReceiver, FMod_code) VALUES (\'FID\',\'Ftype\',\'FTitle\',\'FContent\', \'FSender\',\'FReceiver\', \'FMod_code\')"
            sql = "INSERT INTO feedback (FID, FType, FTitle, FContent, FSender, FReceiver, FMod_code) VALUES (%s,%s,%s,%s, %s, %s, %s);"
            cur.execute(sql, (FID, Ftype, FTitle, FContent, FSender, FReceiver, FMod_code))
            mysql.connection.commit()
            return True
        except Exception as e:
            print("Problem inserting: " + str(e))
            return False

    def uploadMark(self):
        # send marks into database

        pass

    def uploadStudent(self, csvString):
        # upload student information
        cur = mysql.connection.cursor()
        entries = csvString.split('\n')

        try:
            for entry in entries:
                part = entry.split(',')
                value = []
                for smallpart in part:
                    value.append(smallpart)
                sql = "INSERT INTO user (UID, name, isStudent, email) VALUES (%s,%s,%s, %s)"
                cur.execute(sql, value)
                print(value)
                mysql.connection.commit()

            return True
        except Exception as e:
            # print("Problem in: " + str(e))
            return False










# Feedback will be a leaf of Lecturer
# Mods_teach will be a branch of Student
# Assessment next branch
# Followed by component
# Need methods to modify variables in webpages (update/insert values into db)
class Leaf:
    def __init__(self,obj):
        self.obj = obj
        pass
