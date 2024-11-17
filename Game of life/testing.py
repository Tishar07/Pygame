def intGrid(Width,Height):
    CoordDict={}
    for x in range(Width+1):
        for y in range (Height+1):
            CoordDict[(x,y)] = False
    return CoordDict

CoordDict = intGrid(20,15)

# convert mouse click to cell pos format
def round_to_nearest_Cell(num):
    return round(num // 40) * 40

#convert pos format in (x,y) cell
def convertToDict(x,y):
    return (x//40),(y//40)

CoordDict[(5,6)]= True
Directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

x,y= 0,0
#Check surrounding cell location
def surroundingCell(x,y):
    m,n= 20,15
    neighbours=[]
    for di,dj in Directions:
        ni,nj = x+di , y+ dj
        if 0<= ni < m and 0<= nj < n:
            neighbours.append((ni,nj))
    return neighbours

#Rules of life 
#CoordDict[(0,0)]= True
#CoordDict[(0,1)] =True
CoordDict[(1,1)] = True

CoordDict[(7,10)] =True

def live_die(neighbours):
    life = 0 
    for i in range(len(neighbours)):
        if CoordDict[neighbours[i]] == True:
            life+=1
    if life >=2 :
        return True
    else:
        return False

def Birth (neighbours):
    life = 0 
    for i in neighbours:
        if CoordDict[neighbours[i]] == True:
            life+=1
    if life == 3:
        return True
    else:
        return False

def checkGrid():
    for key in CoordDict:
         if CoordDict[key] == True:
            x,y = key
            neighbours = surroundingCell(x,y)
            if live_die(neighbours) == False:
                CoordDict[key] =False
                return "death"
            else:
                return "live"
            

print(checkGrid())








    



    





