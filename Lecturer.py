class Lecturer:
    def __init__(self, Lectid, Lectname, isStud=False, rights=True):
        self.Lectid = Lectid
        self.Lectname = Lectname
        self.isStud = isStud
        self.rights = rights
        self.children = []
        # rights = permission to view lecturer's boundary classes (aka module management powers)

    def getLectid(self):
        return self.Lectid

    def getLectName(self):
        return self.Lectname

    def getRights(self):
        if self.isStud == False:
            self.rights = True

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        pass


