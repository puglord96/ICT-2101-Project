# from flask import *
from flask import Flask, request, render_template, session, flash
from flask_mysqldb import MySQL, MySQLdb
from LecturerController import *
from StudentController import *
from Module import *
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

@app.route('/module')
def module():
    if session['role'] == 1:
        moduleArr = moduleList(session.get('UID')).fetchModules()
    else:
        studID = session['UID']
        studcon = StudentController(studID)
        moduleArr = studcon.viewModule("code")
    return render_template('module.html', moduleArr=moduleArr)

@app.route('/assessment',methods=["GET"])
def assessment():
    # print(session.get('UID'))
    MID = int(request.args.get('MID'))
    session['MID'] = MID
    if session['role'] == 0:
        studID = session['UID']
        studcon = StudentController(studID)
        moduleArr = studcon.viewModule("code")
        moduleName = studcon.viewModule("name", MID)
    else:
        moduleArr = moduleList(session['UID']).fetchModules()
        moduleName = moduleList(session.get('UID')).getModuleName(MID)
    assessArr = []

    for module in moduleArr:
        if module.getID() == MID:
            assessArr = module.getChildrenList()

    # for assessment in assessmentArr:
    #     print(assessment)
    return render_template('moduleAssessment.html', assessArr=assessArr, MID=MID,moduleName = moduleName)

@app.route('/component',methods=["GET"])
def component():
    # print(session.get('UID'))
    MID = session['MID']
    AID = request.args.get('AID')
    print(AID)
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

@app.route('/logout')
def logout():
    session.clear()
    return render_template('authenticate.html')


@app.route('/gamification')
def gamification():
    return render_template('gamification.html')

@app.route('/add_assessment')
def addAssessment():
    return render_template('add_assessment.html')

@app.route('/add_component')
def addComponent():
    return render_template('add_component.html')

@app.route('/edit_component')
def editComponent():
    return render_template('edit_component.html')

@app.route('/feedback')
def feedback():
    if session['role'] == 1:
        lectcon = LecturerController(session['UID'])
        data = lectcon.viewClass()
        # data = None
        return render_template('Lfeedback.html', data=data)
    elif session['role'] == 0:
        studcon = StudentController(session['UID'])
        data = studcon.viewFeedback()
        return render_template('Sfeedback.html',  data=data)

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

@app.route('/add_assessment', methods=["GET","POST"])
def add_assessment():
    # print(session.get('UID'))
    MID = request.args.get('MID')
    if request.method == "POST":
        details = request.form
        ass_name = details["Assessment_name"]
        ass_type = details["type"]
        ass_weightage = details["weightage"]
        ass_mid = MID
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO assessment (assessment_name, MID, type, weight) VALUES (%s, %s, %s ,%s)', (ass_name, ass_mid, ass_type, ass_weightage))
        mysql.connection.commit()
        cur.close()
        return render_template('add_assessment.html', MID=MID)
    # moduleArr = moduleList(session.get('UID')).fetchModules()
    # for assessment in assessmentArr:
    return render_template('add_assessment.html', MID=MID)

@app.route('/add_component', methods=["GET","POST"])
def add_component():
    # print(session.get('UID'))
    AID = request.args.get('AID')
    if request.method == "POST":
        details = request.form
        com_name = details["Component_name"]
        com_weightage = details["weightage"]
        com_aid = details["AID"]
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO component (description, AID, weight) VALUES (%s, %s, %s)', (com_name, com_aid, com_weightage))
        mysql.connection.commit()
        cur.close()
        return render_template('add_component.html', AID=AID)
    # moduleArr = moduleList(session.get('UID')).fetchModules()
    # for assessment in assessmentArr:
    return render_template('add_component.html', AID=AID)

@app.route('/viewFeedback' ,methods=["GET"])
def viewfeedback():
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



@app.route('/uploadStudents', methods=["POST"])
def uploadStudents():
    if session['role'] == 1:
        lectID = int(session["UID"])
        lectcon = LecturerController(lectID)

        file = request.files["studFile"]
        fstring = file.read().decode("utf-8-sig")
        result = lectcon.uploadStudent(fstring)
        if result is True:
            return render_template("gamification.html")
        else:
            return render_template("module.html")
    else:
        return render_template("index.html")

@app.route('/uploadMarks', methods=['POST'])
def uploadMarks():
    if session['role'] == 1:
        lectID = int(session["UID"])
        lectcon = LecturerController(lectID)

        file = request.files["marksFile"]
        filestr = file.read().decode("utf-8")
        result = lectcon.uploadMark(filestr)
        if result is True:
            return render_template("module.html")
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")
@app.route('/addStuds', methods=['POST', 'GET'])
def addStudents():
    if session['role'] == 1:
        lectID = int(session["UID"])
        lectcon = LecturerController(lectID)
        file = request.files["addFile"]
        addStr = file.read().decode("utf-8-sig")

        result = lectcon.addStudents(addStr)
        if result is True:
            return render_template("module.html")
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")

@app.route('/AllFeed', methods=['POST', 'GET'])
def LAllfeedback():
    if session['role']==1:
        lectID = session['UID']
        if request.method== "GET":
            lectcon = LecturerController(lectID)
            data = lectcon.getAllFeedbacks()
            return render_template("LAllFeedbacks.html", data=data)
        else:
            lectcon = LecturerController(lectID)

    else:
        return render_template("index.html")
@app.route('/editFb', methods=["POST", "GET"])
def editFb():
    if session['role']==1:
        lectID = session['UID']
        lectcon = LecturerController(lectID)
        if request.method == "POST":

            ftype = request.form['type']
            ftitle = request.form['title']
            fcontent = request.form['message']
            fid = request.form['fid']
            success = lectcon.updateFeedback(fid, ftype, ftitle, fcontent)
            if success == 1:
                return render_template("editFeedback.html")
            else:
                return render_template("Lfeedback.html")
        elif request.method == "GET":
            fid = request.args.get('fid')
            data = lectcon.getAllFeedbacks(fid)

            return render_template("editFeedback.html", data=data)
    else:
        return render_template("index.html")

@app.route('/viewModule',methods=["GET"])
def viewmod():
    # print(session.get('UID'))
    MID = int(request.args.get('MID'))
    session['MID'] = MID
    moduleArr = moduleList(session.get('UID')).fetchModules()
    moduleName = moduleList(session.get('UID')).getModuleName(MID)
    assessArr = []

    for module in moduleArr:
        if module.getID() == MID:
            assessArr = module.getChildrenList()

    # for assessment in assessmentArr:
    #     print(assessment)
    return render_template('moduleAssessment.html', assessArr=assessArr, MID=MID,moduleName = moduleName)
if __name__ == '__main__':
    app.run(debug=True)
