
from flask_mysqldb import MySQL, MySQLdb
# from flask import Flask
# app = Flask(__name__)
class SQL():
# class SQL():
#
#
#     def __init__(self):

# from flask_mysqldb import MySQL, MySQLdb
# from flask import Flask
# app = Flask(__name__)
#
# class SQL():
#
#
#     def __init__(sel):

#         app.config['MYSQL_USER'] = 'root'
#         app.config['MYSQL_PASSWORD'] = 'sceptile101'
#         app.config['MYSQL_HOST'] = '127.0.0.1'
#         app.config['MYSQL_DB'] = '2101project'
#         app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#         app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'
#
#     def startConnection(self):

#         return MySQL(app)

    def __init__(self,user, host ,dbname ,cursor ,pw=""):
        app.config['MYSQL_USER'] = user
        app.config['MYSQL_PASSWORD'] = pw
        app.config['MYSQL_HOST'] = host
        app.config['MYSQL_DB'] = dbname
        app.config['MYSQL_CURSORCLASS'] = cursor
        app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'
        return mySQL(app)

#         return MySQL(app)

