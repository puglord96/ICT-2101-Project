from flask import Flask
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

# Database Config
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sceptile101'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = '2101project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'


from Database import *
from flask import *
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sceptile101'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = '2101project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'

mysql = MySQL(app)


# account factory need to verify user first? Actually do we really need an account factory, we not creating new classes
class AccountFactory:
    def __init__(self, uid):
        self.uid = uid
        self.valid = None

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM user WHERE UID=" + self.uid)
        user = cur.fetchone()
        cur.close()

        if user:
            self.valid = 1
            self.name = str(user['name'])
            if user['isStudent'] == 0:
                self.role = 1  # Lecturer
            else:
                self.role = 0  # Student

    def getuid(self):
        return self.uid

    def getName(self):
        return self.name

    def getRole(self):
        return self.role

    def getValid(self):
        return self.valid
