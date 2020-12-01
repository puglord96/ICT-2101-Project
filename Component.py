class Component:
    def __init__(self, compoID, compoName, compoWeight, mark_ID, mark):
        self.compoID = compoID
        self.compoName = compoName
        self.compoWeight = compoWeight
        self.mark_ID = mark_ID
        self.mark = mark

    def getCompoWeight(self):
        return self.compoWeight

    def setCompoWeight(self, setCompoWeight):
        self.compoWeight = setCompoWeight

    def getCompoID(self):
        return self.compoID

    def setCompoID(self, setCompoID):
        self.compoID = setCompoID

    def getCompoName(self):
        return self.compoName

    def setCompoName(self, setCompoName):
        self.compoName = setCompoName

    def getMark(self):
        return self.mark

    def setMark(self, setMark):
        self.mark = setMark

