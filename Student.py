from Feedback import *
from Module import *

class Student:
    def __init__(self, Studid, Studname, isStud=True, rights=False):
        self.Studid = Studid
        self.Studname = Studname
        self.isStud = isStud
        self.rights = rights
        self.children =[]
        # rights = permission to view lecturer's boundary classes (aka module management powers)

    def getStudid(self):
        return self.Studid

    def getStudName(self):
        return self.Studname

    def getRights(self):
        if self.isStud == True:
            self.rights = False
    def add(self,child):
        self.children.append(child)
    def remove(self,child):
        self.children.remove(child)

    def showDetails(self):
        print(self.Studname +"\t"+ self.Studid)
        for child in self.children:
            if isinstance(child, Feedback):
                print("Type: " + child.getFeedbackType())
                print("Title: " + child.getFeedbackTitle())
                print("Content: "+ child.getFeedbackContent())
                print("Relation: ", end='')
                print(child.getFeedbackRelation())

# Feedback will be a leaf of Student
# Mods_taken will be a leaf of Student
# Results will be a leaf of Student
# Students will have its own method to only view results (retrieve from db)
class Branch():
    def __initi__(self, obj):
        self.obj = obj
        self.children = []
    def getObj(self):
        return self.obj
    def add(self, child):
        self.children.append(child)
    def remove(self,child):
        self.children.remove(child)
class Leaf():
    def __init__(self,obj):
        self.obj = obj
    def getObj(self):
        return self.obj



if __name__ == "__main__":
    studmod = Module()
    # feedbackID should be automatic and not shown to users. Autoincremented on database)
    studfb1 = Feedback(1,"Feedback", "Good job", "You did well overall for this module", "100123", "190000")
    stud1 = Student("190000", "John Lim Ko Pi")
    stud1.add(studfb1)

    studfb2 = Feedback(2,"Feedback", "Bad job", "You did bad for this module", "100123","190000")
    stud1.add(studfb2)
    stud1.showDetails()

