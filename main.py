#
import os
from terminaldisplay import window

def checkpos(avpos):
    copavpos = avpos.copy()
    for pos in avpos:
        for obpos in mapObstacles:
            if pos== obpos:
                copavpos.remove(pos)
        if pos[0] < 0 or pos[0] > 9 or pos[1] < 0 or pos[1] > 9:
            copavpos.remove(pos)
    return copavpos

mapSize = (10, 10)

mapObstacles = [] # list of 2d pos

# mapObstacles
mapObstacles.append([3,0])
mapObstacles.append([7,1])
mapObstacles.append([2,3])
mapObstacles.append([7,3])
mapObstacles.append([4,5])
mapObstacles.append([6,6])
mapObstacles.append([3,8])
mapObstacles.append([7,8])


moves = []
allpos = []
for y in range(0,10):
    for x in range(0,10):
        allpos.append([x,y])


# DISPLAY   ᐁ
mainwin = window(mapSize)


while True:
    allpos = checkpos(allpos)
    mainwin.clearbuffer("〜")
    for i in mapObstacles:
        mainwin.setpixel(i,"██")
    for i in allpos:
        mainwin.setpixel(i,"[]")


    mainwin.drawscreen()
    dir = input("nesw : ").lower()
    moves.append(dir)
    if dir == "n":
        dir = (0,-1)
    elif dir == "e":
        dir = (1,0)
    elif dir == "s":
        dir = (0,1)
    elif dir == "w":
        dir = (-1,0)

    for i in range(len(allpos)):
        allpos[i][0] += dir[0]
        allpos[i][1] += dir[1]
