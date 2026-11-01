import pgzrun
import random
HEIGHT=600
WIDTH=800

level=1
Actorlist=[]
finalitems=["paperimg.png"]
nonr=["bagimg.png","batteryimg.png","bottleimg.png","chipsimg.png"]

for i in range(level):
    variable=random.choice(nonr)
    finalitems.append(variable)

for i in finalitems:
    temp=Actor(i)
    Actorlist.append(temp)

def draw():
    screen.blit("sky.png",(0,0))





pgzrun.go()