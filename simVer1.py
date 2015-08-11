import objects
import random
import sys
import pygame
import time

pygame.init()
size = width,height = 480,640
mainscreen = pygame.display.set_mode(size)

def PopulateClassroom(students,classroom):
    for x in range(0,students):
        student = objects.NewStudent()
        print("Generated student ID:{}".format(student.uniqueID))
        result = classroom.AddObject(student)
        if result == False:
            return False

def main():
    r1 = objects.Classroom(pSize = (20,6),pType="classroom")
    PopulateClassroom(10,r1)
    test = r1.GetObjectList()
##    for row_idx,row in enumerate(test):
####        print("Row:{}".format(row))
##        for col_idx,col in enumerate(test[0]):
##            print("({},{}):{}".format(row_idx,col_idx,test[row_idx][col_idx]['Objects'].uniqueID))
    #print("classroom:{}".format(test))
    r1.PrintObjects()
    screenEnabled = False
    renderRate = 1.0/10.0
    print("Render rate:{}".format(renderRate))
    nextRenderUpdate = time.time() + renderRate
    mainscreen.fill([0,0,255])    
    while screenEnabled:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screenEnabled = False
    
        if time.time() >= nextRenderUpdate:
            nextRenderUpdate += renderRate
            print("Updating screen: {}".format(nextRenderUpdate))
            #pygame.display.flip()
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
