import re
import sys
sys.setrecursionlimit(1000000)
layout = []
f = open("day10/input.txt")
pipes = []
for line in f:
    temp = []
    for c in line.strip():
        temp.append(c)
    layout.append(temp)


def findstart(layout):
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] == 'S':
                return (x, y)

def dostep(layout,startx,starty,dir,step):
    step+=1
    if (startx, starty) not in pipes:
        pipes.append((startx, starty))
    if layout[starty][startx]=='S':
        print("Part1:",int(step/2))
        return True
    
    if dir =="R":
        if  'J' in layout[starty][startx]:
            if starty>0:
                return dostep(layout,startx,starty-1,'U',step)
        elif  '-' in layout[starty][startx]:
            if startx+1<len(layout[0]):
                return dostep(layout,startx+1,starty,'R',step)
        elif '7' in layout[starty][startx]:
            if starty+1<len(layout):
                return dostep(layout,startx,starty+1,'D',step)
    elif dir=='L':
        if 'L' in layout[starty][startx]:
            if starty>0:
                return dostep(layout,startx,starty-1,'U',step)
        elif '-' in layout[starty][startx]:
            if startx>0:
                return dostep(layout,startx-1,starty,'L',step)
            
        elif 'F' in layout[starty][startx]:
            if starty+1<len(layout):
                return dostep(layout,startx,starty+1,'D',step)
            #goto down
            
    elif dir=='U':
        if '7' in layout[starty][startx] :
            if startx>0:
                return dostep(layout,startx-1,starty,'L',step)
        elif '|' in layout[starty][startx]:
            if starty>0:
                return dostep(layout,startx,starty-1,'U',step)
        elif 'F' in layout[starty][startx]:
            if startx+1<len(layout[0]):
                return dostep(layout,startx+1,starty,'R',step)
    elif dir=='D':
        if 'J' in layout[starty][startx] :
            if startx>0:
                return dostep(layout,startx-1,starty,'L',step)
        elif '|' in layout[starty][startx]:
            if starty+1<len(layout):
                return dostep(layout,startx,starty+1,'D',step)
        elif 'L' in layout[starty][startx]:
            if startx+1<len(layout[0]):
                return dostep(layout,startx+1,starty,'R',step)


startisUp = False
part1solved = False

# check which way to start:
startx, starty = findstart(layout)
if starty > 0:
    if re.match(r"(7|\||F)", layout[starty-1][startx]):
        part1solved = dostep(layout, startx, starty-1, 'U',1)
        startisUp = part1solved
if startx > 0 and part1solved == False:
    if re.match(r"(L|\-|F)", layout[starty][startx-1]):
        part1solved = dostep(layout, startx-1, starty, 'L',1)
if starty < len(layout)-1 and part1solved == False:
    if re.match(r"(J|\||L)", layout[starty+1][startx]):
        part1solved = dostep(layout, startx, starty+1, 'D',1)
if startx < len(layout[0])-1 and part1solved == False:
    if re.match(r"(J|\-|7)", layout[starty][startx+1]):
        part1solved = dostep(layout, startx+1, starty, 'R',1)


count = 0
for y in range(len(layout)):
    inside = False
    for x in range(len(layout[0])):
        if (x, y) in pipes:
            if startisUp:
                if re.match(r'(J|\||L|S)', layout[y][x]):
                    inside = not inside
            else:
                if re.match(r'(J|\||L)', layout[y][x]):
                    inside = not inside
        else:
            if inside:
                count += 1


print("Part2:", count)
