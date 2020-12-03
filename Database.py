
class SQL():

    def __init__(self,user, host ,dbname ,cursor ,pw=""):
        app.config['MYSQL_USER'] = user
        app.config['MYSQL_PASSWORD'] = pw
        app.config['MYSQL_HOST'] = host
        app.config['MYSQL_DB'] = dbname
        app.config['MYSQL_CURSORCLASS'] = cursor
        app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'
        return mySQL(app)