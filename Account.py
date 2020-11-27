# account factory need to verify user first? Actually do we really need an account factory, we not creating new classes
class AccountFactory:
    def __init__(self, id, name, rights=False):
        self._id = id
        self._name = name
        self._rights = rights
        self._idlen = len(str(self._id))

        if self._idlen != 6 and self._idlen != 7:
            raise ValueError("Invalid User ID")

    def getid(self):
        return self._id

    def getName(self):
        return self._name

    def execRights(self):
        if self._idlen == 6:
            self._rights = True


