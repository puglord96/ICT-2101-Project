class Student:
    def __init__(self, Studid, Studname, isStud=True, rights=False):
        self.Studid = Studid
        self.Studname = Studname
        self.isStud = isStud
        self.rights = rights
        # rights = permission to view lecturer's boundary classes (aka module management powers)

    def getStudid(self):
        return self.Studid

    def getStudName(self):
        return self.Studname

    def getRights(self):
        if self.isStud == True:
            self.rights = False