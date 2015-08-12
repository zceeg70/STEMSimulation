import objects
import random
import sys
import pygame
import time
import math

pygame.init()
size = width,height = 480,640
mainscreen = pygame.display.set_mode(size)
currentZoom = 10
roomList = []

def PopulateClassroom(students,classroom):
    for x in range(0,students):
        student = objects.NewStudent()
        print("Generated student ID:{}".format(student.uniqueID))
        result = classroom.AddObject(student)
        if result == False:
            return False
        
def DrawCircles(room,mainscreen,scale=10):
    objectList = room.GetObjectList()
    offsetX = width/2
    offsetY = height/2
    
    roomSize = room.GetSize()
    roomWidth = roomSize[0]*scale
    roomHeight = roomSize[1]*scale
    roomTLX = offsetX-(roomWidth/2)
    roomTLY = offsetY-(roomHeight/2)
    
    pygame.draw.rect(mainscreen,(255,0,0),(roomTLX,roomTLY,roomWidth,roomHeight),3)
    for o in objectList:
        pos = o.GetPosition()
        posX =round(roomTLX+(scale*pos[0]))
        posY = round(roomTLY+(scale*pos[1]))
        radius = round(scale/2)
        pygame.draw.circle(mainscreen,(255,0,0),(posX,posY),radius,1)

        if(o.type == "Student"):
            interest = o.interest
            steps = 30
            interestColor = (50,250,198)
            radius2 = round(radius*(interest))
            #print("radius:{}".format(radius2))
            pygame.draw.circle(mainscreen,interestColor,(posX,posY),radius2,0)
        
def DrawGrid(mainscreen,scale):
    color = (0,200,0)
    lineSpacing = 10
    numberOfLinesH = int(height / lineSpacing)
    numberOfLinesV = int(width / lineSpacing)
    for x in range(1,numberOfLinesH):
        pygame.draw.aaline(mainscreen,color,((x*lineSpacing),0),((x*lineSpacing),height))
    for y in range(1,numberOfLinesH):
        pygame.draw.aaline(mainscreen,color,(0,y*lineSpacing),(width,y*lineSpacing))
    
def Redraw():
    r1 = roomList[0]
    mainscreen.fill([0,0,200])
    DrawGrid(mainscreen,currentZoom)
    DrawCircles(r1,mainscreen,currentZoom)

def HandleChats(room):
    objectList = room.GetObjectList()
    timeNow = time.time()
    for o in objectList:
        if o.GetNextChat() < timeNow:
            if random.randint(0,10)>8:
                #print("chatting!")
                SpreadChats(objectList,o)
                o.UpdateNextChat()
        #break
    for o in objectList:
        o.updateInterest()
        

def SpreadChats(objectList,selected):
    sPosition = selected.GetPosition()
    interestInfluence = selected.interest - 0.5
    for o in objectList:
        if o == selected:
            continue
        oPosition = o.GetPosition()
        diffX = abs(sPosition[0]-oPosition[0])
        diffY = abs(sPosition[1]-oPosition[1])
        distance = round(math.sqrt(diffX**2 + diffY**2),4)
        if distance == 0:
            distance = 0.5
        dInterest = interestInfluence / distance**2
        #print("distance:{} dinterest:{}".format(distance,dInterest))
        o.setDInterest(dInterest)

        

    
                
            

def main():
    r1 = objects.Classroom(pSize = (20,10),pType="classroom")
    roomList.append(r1)
    PopulateClassroom(10,r1)
    global currentZoom
    #test = r1.GetObjectList()
##    for row_idx,row in enumerate(test):
####        print("Row:{}".format(row))
##        for col_idx,col in enumerate(test[0]):
##            print("({},{}):{}".format(row_idx,col_idx,test[row_idx][col_idx]['Objects'].uniqueID))
    #print("classroom:{}".format(test))
    r1.PrintObjects()
    screenEnabled = True
    renderRate = 1.0/10.0
    logicRate = 1.0/100.0
    print("Render rate:{}".format(renderRate))
    nextRenderUpdate = time.time() + renderRate
    nextLogic = time.time() + logicRate
##    mainscreen.fill([0,0,255])
##    DrawGrid(mainscreen,currentZoom)
##    DrawCircles(r1,mainscreen)
    Redraw()
    
    while screenEnabled:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screenEnabled = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and not currentZoom > 62:
                    currentZoom *= 1.3                    
                    Redraw()
                elif event.button == 5  and not currentZoom < 6:
                    currentZoom /= 1.3
                    Redraw()
                print("Zoom:{}".format(currentZoom))
               # print("Mouse:{}".format(pygame.mouse.get_pressed()))
        if time.time() >= nextLogic:
            nextLogic = time.time() + logicRate
            HandleChats(r1)
    
        if time.time() >= nextRenderUpdate:
            nextRenderUpdate += renderRate
            Redraw()
##            print("Updating screen: {}".format(nextRenderUpdate))
            pygame.display.flip()
        #pygame.time.delay(20)
    pygame.quit()

    
##    rs = Classroom()
##    s1 = Student(0.5,0.5)
if __name__ == "__main__":
    try:
        main()
    except:
        pygame.quit()
        raise
