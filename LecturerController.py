from Lecturer import Lecturer
from flask_mysqldb import MySQL #for flask-mysqldb
from flask import Flask
from Feedback import *

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
        cur.execute("SELECT RID, r.UID, marks, c.description,m.mod_code FROM result r,component c,assessment a, module m where r.CID = c.CID AND c.AID = a.AID"
                    " and a.MID=m.MID")
        resultdata = cur.fetchall()

        # View students that are taking the module
        #cur.execute("SELECT user.UID, user.name, user.email, module.mod_code FROM user INNER JOIN module ON user.UID = module.UID WHERE isStudent = 1;")
        #data = cur.fetchall()

        return resultdata
    def giveFb(self, FID, Ftype, FTitle, FContent, FSender, FReceiver, FMod_code ):
        try:
            cur = mysql.connection.cursor()
            sql = "INSERT INTO feedback (FID, FType, FTitle, FContent, FSender, FReceiver, FMod_code) VALUES (%s,%s,%s,%s, %s, %s, %s);"
            cur.execute(sql, (FID, Ftype, FTitle, FContent, FSender, FReceiver, FMod_code))
            mysql.connection.commit()
            return True
        except Exception as e:
            print("Problem inserting: " + str(e))
            return False

    def uploadMark(self, csvString):
        # send marks into database
        cur = mysql.connection.cursor()
        # split the multiple entries
        entries = csvString.split('\r')
        print(entries)
        try:
            for entry in entries:
                part = entry.split(',')
                values = []

                for small in part:
                    values.append(small)
                sql = "INSERT INTO result (UID, marks, CID) VALUES (%s, %s, %s)"
                cur.execute(sql,values)
                # print(value)
                mysql.connection.commit()
            return True
        except Exception as e:
            # print("Error in: " + str(e))
            return False

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
                # print(value)
                mysql.connection.commit()
            return True
        except Exception as e:
            # print("Problem in: " + str(e))
            return False
    def addStudents(self, csvString):
        cur = mysql.connection.cursor()
        list = csvString.split('\n')

        try:
            for entry in list:
                part = entry.split(',')
                value = []
                for small in part:
                    value.append(small)
                    print(value)
                sql = "INSERT INTO module (mod_code, mod_name, UID) VALUES(%s,%s,%s)"
                cur.execute(sql, value)
                mysql.connection.commit()
            return True
        except Exception as e:
            print("Problem in: " + str(e))
            return False

        pass
    def getAllFeedbacks(self, type="all"):
        cur = mysql.connection.cursor()
        if type =="all":
            try:
                sql = "SELECT * FROM Feedback WHERE FSender = " + self.UID + ";"
                cur.execute(sql)
                data = cur.fetchall()
                return data
            except Exception as e:
                print("Error in: " + str(e))
        else:
            try:
                sql = "SELECT * from Feedback WHERE FSender = " + self.UID + " AND FID = " + type + ";"
                cur.execute(sql)
                data = cur.fetchall()
                return data
            except Exception as e:
                print("Error in: " + str(e))

    def updateFeedback(self, fid, ftype, ftitle, fcontent):
        cur = mysql.connection.cursor()
        try:
            sql = "UPDATE feedback SET FType = %s, FTitle = %s, FContent = %s WHERE FID = %s"
            cur.execute(sql, (ftype, ftitle, fcontent, fid))
            mysql.connection.commit()
            return True
        except Exception as e:
            print("Error in :" + str(e))
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
