from flask_mysqldb import MySQL, MySQLdb

class SQL():

    def __init__(self,user, host ,dbname ,cursor ,secretkey,pw=""):
        app.config['MYSQL_USER'] = user
        app.config['MYSQL_PASSWORD'] = pw
        app.config['MYSQL_HOST'] = host
        app.config['MYSQL_DB'] = dbname
        app.config['MYSQL_CURSORCLASS'] = cursor
        app.config['SECRET_KEY'] = secretkey
        return mySQL(app)

