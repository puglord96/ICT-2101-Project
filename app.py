# from flask import *
from flask import Flask, request, render_template, session, flash
from flask_mysqldb import MySQL, MySQLdb

import AccountController

app = Flask(__name__)

# Database Config
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = '2101project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'

mysql = MySQL(app)


@app.route('/')
def home():
    # cur = mysql.connection.cursor()
    # cur.execute('''SELECT * FROM  user''')
    # results = cur.fetchall()
    # print(results)
    # return 'Done!'

    # authenticate
    if not (session.get('UID') or session.get('name') or session.get('role')) is None:
        return render_template('index.html')
    else:
        return render_template('authenticate.html')


@app.route('/authenticate', methods=["GET", "POST"])
def authenticate():
    if request.method == "GET":
        if not (session.get('UID') or session.get('name') or session.get('role')) is None:
            return render_template('index.html')
        else:
            return render_template('authenticate.html')

    if request.method == "POST":
        # Account Object from AccountFactory
        acc = AccountController.AccountFactory(request.form['uid'])

        # Account valid
        if acc.getValid():
            session['UID'] = acc.getuid()
            session['name'] = acc.getName()
            session['role'] = acc.getRole()  # 1 = lecturer 0 = Student
            return render_template('index.html')
        else:   # Authenticate fail
            flash('Admin Number does not exist!')
            return render_template('authenticate.html')

    #     uid = request.form['uid']
    #     cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #     cur.execute("SELECT * FROM user WHERE UID=" + uid)
    #     user = cur.fetchone()
    #     cur.close()
    #
    # if not user:
    #     # Authenticate fail
    #     flash('Admin Number does not exist!')
    #     return render_template('authenticate.html')
    #
    #
    # session['UID'] = str(user['UID'])
    # session['name'] = str(user['name'])
    # if user['isStudent'] == 0:
    #     session['role'] = 1     # Lecturer
    # else:
    #     session['role'] = 0     # Student
    # return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    return render_template('authenticate.html')


@app.route('/gamification')
def gamification():
    return render_template('gamification.html')


if __name__ == '__main__':
    app.run(debug=True)
