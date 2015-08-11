import sys
import random

roomType = {
    "classroom":[0.5,0.5],
    "lab":[0.4,0.8],
    "hall":[0.6,0.2]
    }

class Student:
   # stackable = False
    def __init__(self,interest,engagement):
        self.interest = interest
        self.engagement = engagement

class Cell:
    def __init__(self,pPosition,pObject):
        pass

class Classroom:
    #studentList = []
    #staffList = []
    #objectList = []
    def __init__(self,pSize=(10,5),pType="classroom"):
        if(type(pSize)!=tuple):
            print("pSize must be tuple")
            sys.exit()
        if(type(pType)!=tuple):
            print("pType must be tuple")
            sys.exit()
        self.roomSize = pSize
        self.roomType = pType
        self.objectList = [[None]*pSize[0]]*pSize[1]

    def AddObject(self,pObject):
        if not pObject in studentList:
            result = GetNextFreePosition(pObject)
            if result == False:
                return False
            else:
                studentList.append(student)
                return True
        else:
            return False

    def RemoveObject(self,student):
        if student in studentList:
            studentList.remove(student)
            return True
        else:
            return False

    def GetNextFreePosition(self,pObject):        
        #x = random.randint(0,self.roomSize[0])
       # y = random.randint(0,self.roomSize[1])
        maxCount = self.roomSize[0]*self.roomSize[1]
        counter = 0
        objectList = self.objectList
        
        for counter in range(0,maxCount):
            x = random.randint(0,self.roomSize[0])
            y = random.randint(0,self.roomSize[1])
            if(objectList[x][y]==None):
                objectList[x][y] = {"Objects":[pObject]}
                self.objectList = objectList
                return True
        return False

    def FreePosition(self,pPosition):
        if(type(pPosition)!=tuple):
            print("pType must be tuple")
            sys.exit()
        x = pPosition[0]
        y = pPosition[1]
        self.objectList[x][y] = None

    
