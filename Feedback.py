class Feedback:
    def __init__(self, fid, ftype, ftitle, fcontent, fsender, freceiver):
        self.fid = fid
        self.ftype = ftype
        self.ftitle = ftitle
        self.fcontent = fcontent
        self.fsender = fsender
        self.freceiver = freceiver
        self.frelation = []

    def getFeedbackID(self):
        return self.fid
    def getFeedbackType(self):
        return self.ftype
    def setFeedbackType(self, setFtype):
        self.ftype = setFtype
    def getFeedbakTitle(self):
        return self.ftitle
    def setFeedbackTitle(self, setFtitle):
        self.ftitle = setFtitle
    def getFeedbackContent(self):
        return self.fcontent
    def setFeedbackContent(self, setFcontent):
        self.fcontent = setFcontent
    def getFeedbackRelation(self):
        return self.frelation
    def setFeedbackRelation(self, fsender, freceiver):
        self.frelation.append(fsender+"," +freceiver)

        
