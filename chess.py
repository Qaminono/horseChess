import time
import numpy

X, Y = 8, 8
x0, y0 = 3, 4
gameArr = numpy.zeros((Y, X))
cou = 1
gameArr[y0][x0] = cou

case = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]


def findways(coords, case, y, x):
    global gameArr
    checkarr = []
    for i in case:
        if 0 <= coords[1]+i[1] <= x-1 and 0 <= coords[0]+i[0] <= y-1:
            if gameArr[coords[0]+i[0]][coords[1]+i[1]] == 0.0:
                checkarr.append([coords[0]+i[0], coords[1]+i[1]])

    return checkarr


def countways(coords):
    checkarr = findways(coords, case, Y, X)
    return len(checkarr)


def goway(y, x, case):
    global cou
    checkarr = findways([y, x], case, Y, X)
    counts = []
    for i in checkarr:
        counts.append(countways(i))
    minimal = counts.index(min(counts))
    cou += 1
    gameArr[checkarr[minimal][0]][checkarr[minimal][1]] = cou
    time.sleep(0)
    print(gameArr)
    try:
        goway(checkarr[minimal][0], checkarr[minimal][1], case)
    except:
        print(gameArr)


goway(y0, x0, case)