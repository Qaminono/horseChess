import time


#gameArr = numpy.zeros((4,3))
gameArr = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
gameArr[0][0] = 1

case = [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]

def step(y,x,case,gameArr):
    

    checkArr = []


    for i in case:
        if 0 <= x+i[1] <= 2 and 0 <= y+i[0] <= 3:
            if gameArr[y+i[0]][x+i[1]] == 0.0:
                checkArr.append([y+i[0],x+i[1]])
                print(checkArr)


    for i in checkArr:
        gameArr[i[0]][i[1]] = 1
        step(i[0],i[1],case,gameArr)
        time.sleep(1)
    
    

step(0,0,case,gameArr)


