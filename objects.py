import sys
import random

roomType = {
    "classroom":[0.5,0.5],
    "lab":[0.4,0.8],
    "hall":[0.6,0.2]
    }

IDList = []
StudentList = []
def NewStudent():
    current_id = 0
    interest = random.randint(1,9)/10
    engagement = random.randint(1,9)/10
    newStudent = Student(interest,engagement)
    for item in IDList:
        if item[0] == current_id:
            current_id+=1
    newStudent.setID(current_id)
    IDList.append([current_id,newStudent])
    return newStudent

class Vector:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.dx = 0
        self.dy = 0
        #print("Vector inited")
        
    def SetPosition(self,x,y,dx=0,dy=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        
    def SetSpeed(self,dx,dy):
        self.dx = dx
        self.dy = dy

    def GetPosition(self):
       # print("GP Called")
        return (self.x,self.y)

    def GetSpeed(self):
        return (self.dx,self.dy)

    def UpdatePos(self,times=1):
        self.x += self.dx*times
        self.y += self.dy*times

class Student(Vector):
    def __init__(self,interest,engagement,uniqueID="unassigned"):
        super().__init__()
        self.interest = interest
        self.engagement = engagement
        self.uniqueID = uniqueID
        self.type = "Student"
        
    def setID(self,ID):
        self.uniqueID = ID
    

class Cell:
    def __init__(self,pPosition,pObject):
        pass

class Classroom:
    #objectList = []
    def __init__(self,pSize=(10,5),pType="classroom"):
        if(type(pSize)!=tuple):
            print("pSize must be tuple")
            sys.exit()
        self.roomSize = pSize
        self.roomType = pType
##        objectList = self.objectList
##        for x in range(0,pSize[0]):
##            row = []
##            for y in range(0,pSize[1]):
##                row.append({"Objects":[]})
##                #self.objectList[x][y] = {"Objects":[]}
##            objectList.append(row)
        self.objectList = []
    def GetSize(self):
        return self.roomSize
    
    def AddObject(self,pObject):
        #if not pObject in studentList: #<--TODO
        
        result = self.GetNextFreePosition(pObject)
        ID = pObject.uniqueID
        #FindID
        #IsPositionFree( foundID.x-1 | foundID.x+1)
        
        if result == False:
            return False
        else:
            print("Student added")
            return True
        #else:
        #    return False

    def RemoveObject(self,student):
        if student in studentList:
            studentList.remove(student)
            return True
        else:
            return False

    def GetObjectList(self):
        return self.objectList
    
    def GetObjects(self,objectType):
        pass

    def PrintObjects(self):
        objectList = self.objectList
        for o in objectList:
            print("({}):{}".format(o.GetPosition(),o.type))
##        for row_idx,row in enumerate(objectList):
####        print("Row:{}".format(row))
##            for col_idx,col in enumerate(objectList[0]):
##                objectSing = objectList[row_idx][col_idx]["Objects"]
##                if(len(objectSing)>0):
##                    print("({},{}):{}".format(row_idx,col_idx,objectSing[0].uniqueID))
                    
    def IsPositionFree(self,position):
        x = position[0]
        y = position[1]
        if(len(self.objectList[x][y]["Objects"])==0):
            return True
        else:
            return False
    
    def GetNextFreePosition(self,pObject):        
        maxCount = self.roomSize[0]*self.roomSize[1]
        counter = 0
        objectList = self.objectList
##        positionList = [i.GetPosition()  for i in objectList]
        positionList = lambda i:i.GetPosition(),objectList
        for counter in range(0,maxCount):
            x = random.randint(2,(self.roomSize[0]-1))
            y = random.randint(2,(self.roomSize[1]-1))
            #print("len(OL):{} Len(OL[0]):{} X:{} Y:{}".format(len(objectList),len(objectList[0]),x,y))
            if((x,y) not in positionList):
                print("Objected added at x:{},y:{}".format(x,y))
                pObject.SetPosition(x,y)
                objectList.append(pObject)
                self.objectList = objectList
                #self.PrintObjects()
                return True
        print("Failed to find position")
        return False

    
