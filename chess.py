import time
# import numpy


# gameArr = numpy.zeros((4, 3))
gameArr = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
gameArr[0][0] = 1

case = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]


def findways(coords, case):
    global gameArr
    checkarr = []
    for i in case:
        if 0 <= coords[1]+i[1] <= 2 and 0 <= coords[0]+i[0] <= 3:
            if gameArr[coords[0]+i[0]][coords[1]+i[1]] == 0.0:
                checkarr.append([coords[0]+i[0], coords[1]+i[1]])

    return checkarr


def countways(coords):
    checkarr = findways(coords, case)
    return len(checkarr)


def goway(y, x, case):

    checkarr = findways([y, x], case)
    counts = []
    for i in checkarr:
        counts.append(countways(i))
    minimal = counts.index(min(counts))
    gameArr[checkarr[minimal][0]][checkarr[minimal][1]] = 1
    time.sleep(1)
    print(gameArr)
    try:
        goway(checkarr[minimal][0], checkarr[minimal][1], case)
    except:
        print(gameArr)


goway(0, 0, case)