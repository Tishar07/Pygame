import pygame
import sys
pygame.init()

#Screen definition
width = 1290
height = 720
CellSize = 30
Screen = pygame.display.set_mode((width,height))
running  = True

#Header
pygame.display.set_caption("Game of Life")
icon = pygame.image.load("big_glider.png")
pygame.display.set_icon(icon)

def round_to_nearest_Cell(num):
    return round(num // CellSize) * CellSize

def intGrid(Width,Height):
    CoordDict={}
    for x in range(Width+1):
        for y in range (Height+1):
            CoordDict[(x,y)] = False
    return CoordDict

def convertToDict(x,y):
    return (x//CellSize),(y//CellSize)

def surroundingCell(x,y):
    m,n= Gx,Gy
    neighbours=[]
    for di,dj in Directions:
        ni,nj = x+di , y+ dj
        if 0<= ni < m and 0<= nj < n:
            neighbours.append((ni,nj))
    return neighbours

def live_die(neighbours):
    life = 0 
    for i in range(len(neighbours)):
        if CoordDict[neighbours[i]] == True:
            life+=1
    if life >=2 :
        return True
    else:
        return False
    
Gx,Gy = convertToDict(width,height)
CoordDict = intGrid(Gx,Gy)
Directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
neighbours = []

#Game Run Section
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    
    #Background colour
    for x in range(0,width,CellSize):
        for y in range (0,height,CellSize):
             pygame.draw.rect(Screen,(255,255,255),(x,y,CellSize,CellSize),1)

    if event.type == pygame.MOUSEBUTTONDOWN:
            Mx ,My = pygame.mouse.get_pos()
            ClickAtColor = Screen.get_at((Mx ,My))    

    if event.type == pygame.MOUSEBUTTONDOWN and ClickAtColor == (0,0,0,255):
            
            #format to nearest and lowest cell
            Cx,Cy = round_to_nearest_Cell(Mx), round_to_nearest_Cell(My)        
            pygame.draw.rect(Screen,(255,255,0),pygame.Rect( Cx,Cy, CellSize, CellSize),0)
            #format coordinates to grid format
            Gx , Gy = convertToDict(Cx,Cy)
            CoordDict[Gx,Gy] = True
            

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
         for key in CoordDict:
            if CoordDict[key] == True:
                x,y = key
                neighbours = surroundingCell(x,y)
            if live_die(neighbours) == False:
                #CoordDict[key] =False
                Cx ,Cy = x*CellSize , y * CellSize
                pygame.draw.rect(Screen,(0,0,0),pygame.Rect( Cx,Cy, CellSize, CellSize),0)
         print(CoordDict)


                


 
 
 
 
 
 
 
    pygame.display.update()


pygame.display.quit()
sys.exit()