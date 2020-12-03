# from flask import *
from flask import Flask, request, render_template, session, flash
from flask_mysqldb import MySQL, MySQLdb
from LecturerController import *
from Module import *
import AccountController

app = Flask(__name__)


# Database Config

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sceptile101'
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

@app.route('/module')
def module():
    print(session.get('UID'))
    moduleArr = moduleList(session.get('UID')).fetchModules()
    # for module in moduleArr:
    #     print(module)
    return render_template('module.html', moduleArr=moduleArr)

@app.route('/assessment',methods=["GET"])
def assessment():
    # print(session.get('UID'))
    MID = int(request.args.get('MID'))
    session['MID'] = MID
    moduleArr = moduleList(session.get('UID')).fetchModules()
    assessArr = []

    for module in moduleArr:
        if module.getID() == MID:
            assessArr = module.getChildrenList()
    # for assessment in assessmentArr:
    #     print(assessment)
    return render_template('moduleAssessment.html', assessArr=assessArr, MID=MID)

@app.route('/component',methods=["GET"])
def component():
    # print(session.get('UID'))
    MID = session['MID']
    AID = int(request.args.get('AID'))
    moduleArr = moduleList(session.get('UID')).fetchModules()
    assessArr = []
    componentArr = []
    for module in moduleArr:
        if module.getID() == MID:
            assessArr = module.getChildrenList()
            for assess in assessArr:
                if assess.getID() == AID:
                    componentArr = assess.getChildrenList()
    # for assessment in assessmentArr:
    #     print(assessment)
    return render_template('component.html', componentArr=componentArr, AID=AID)

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

@app.route('/feedback')
def feedback():
    if session['role'] == 1:
        lectcon = LecturerController(session['UID'])
        data = lectcon.viewClass()
        # data = None
        return render_template('Lfeedback.html', data=data)
    elif session['role'] == 0:
        return render_template('Sfeedback.html')

@app.route('/giveFeedback' ,methods=["POST"])
def givefeedback():
    if session["role"] == 1:
        studID = int(request.form["studID"])
        if request.form["mod_code"] is not "":
            mod_code = int(request.form["mod_code"])
        else:
            #mod code 9999 means no module tagged with this feedback
            mod_code = 9999
        ftype = request.form["ftype"]
        title = request.form["title"]
        message = request.form["message"]
        lectID = int(session["UID"])

        lectcon = LecturerController(lectID)
        cur = mysql.connection.cursor()
        cur.execute("SELECT fid from feedback ORDER BY fid DESC LIMIT 1;")
        result = cur.fetchone()
        lastFID = result['fid'] + 1

        dbresult = lectcon.giveFb(lastFID, ftype, title, message, lectID, studID, mod_code)
        if dbresult is True:
            return render_template('gamification.html')
        else:
            return render_template('index.html')
    else:
        return render_template('Sfeedback.html')
if __name__ == '__main__':
    app.run(debug=True)
