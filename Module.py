from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from flask_mysqldb import MySQL, MySQLdb
from flask import Flask

app = Flask(__name__)

# Database Config
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sceptile101'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = '2101project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = b'6hc/_psp,./;2ZZx3c6_s,1//'

mysql = MySQL(app)







class Component(ABC):
    """
    Interface Class
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """

        pass





class Leaf(Component):
    def __init__(self, id, name, weight=0.0,mark = 0.0):
        self._id = id
        self._name = name
        self._weight = weight
        self._mark = mark


    def getMark(self):
        return self._mark

    def setMark(self, Mark):
        self._mark = Mark

    def getWeight(self):
        return self._weight

    def setWeight(self, weight):
        self._weight = weight

    def getID(self):
        return self.id

    def setID(self, id):
        self._id = id

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self,id="Master",name="Master",type="None",weight='None') -> None:
        self._children: List[Component] = []
        self._id = id
        self._name = name
        self._type = type
        self._weight = weight


    def getID(self):
        return self._id

    def setID(self, id):
        self._id = id

    def getType(self):
        return self._type

    def setType(self, type):
        self._type = type

    def getName(self):
        return self._name

    def setName(self, name):
        self.name = name

    def getWeight(self):
        return self._weight

    def setWeight(self, weight):
        self.weight = weight

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def getChildrenList(self):
        return self._children

    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Component class, the client code can work with any component, simple or
    complex, without depending on their concrete classes.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")

class componentList:
    def __init__(self, aid,uid):
        self._aid = aid
        self._uid = uid
        self._querylist = []

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("select * from component c , result r where c.cid = r.cid and r.uid = %s and c.aid = %s",(self._uid,self._aid))
        self._querylist = cur.fetchall()
        cur.close()


    def fetchModules(self):
        return self._querylist

class assessmentList:
    def __init__(self, mid):
        self._mid = mid
        self._querylist = []

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM assessment WHERE MID=" + str(self._mid))
        self._querylist = cur.fetchall()
        cur.close()


    def fetchModules(self):
        return self._querylist

class moduleList:

    def __init__(self,uid):
        self._uid = uid
        self._list = []
        self._querylist = []

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM module WHERE UID=" + str(self._uid))
        self._querylist = cur.fetchall()
        cur.close()

        for query in self._querylist:
            Module = Composite(query["MID"], str(query["mod_code"]) + " " + query["mod_name"])
            AssessmentList = assessmentList(query["MID"]).fetchModules()
            for assessment in AssessmentList:
                AssessmentObj = Composite(assessment["AID"],assessment["assessment_name"],assessment["type"],assessment["weight"])
                ComponentArr = componentList(assessment["AID"],self._uid).fetchModules()
                for component in ComponentArr:
                    componentobj = Leaf(component["CID"],component["description"],component["weight"],component["marks"])
                    AssessmentObj.add(componentobj)
                Module.add(AssessmentObj)
            self._list.append(Module)


    def fetchModules(self):
        return self._list


    def getModuleName(self,MID):
        for module in self._list:
            if module.getID() == MID:
                return module.getName()



# class assessmentForm:
#     def __init__ (self, mid, name, type, weightage):
#         self._mid = mid
#         self._name = name
#         self._type = type
#         self._weightage = weightage
#
#     def add_assessment(self):
#         cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cur.execute('INSERT INTO assessment (assessment_name, MID, type, weight) VALUES (%s, %s, %s %s)', (self._mid, self._name, self._type, self._weightage))
#         mysql.connection.commit()
#         cur.close()


#
# class componentList:
#     def __init__(self,aid):
#         self._aid = aid
#         self._querylist = []
#
#         cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cur.execute("SELECT * FROM component WHERE AID=" + str(self._aid))
#         self._querylist = cur.fetchall()
#         cur.close()
#
#     def fetchModules(self):
#         return self._querylist

if __name__ == "__main__":
    # This way the client code can support the simple leaf components...


    simple = Leaf("0010","dsds")
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as the complex composites.
    ModuleCollection = Composite()

    Module = Composite("ICT2101","Introduction to Software Engineering")
    Assessment = Composite("0001","Module Project")

    Assessment.add(Leaf("0001","Milestone 1",0.3))
    Assessment.add(Leaf("0002","Milestone 2", 0.35))

    Module.add(Assessment)
    ModuleCollection.add(Module)

    modules = moduleList(1901000)

    print(modules)
