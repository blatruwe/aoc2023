import re
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


def dostep(layout, startx, starty, dir):
    pipes.append(findstart(layout))
    step = 1
    while layout[starty][startx] != 'S':
        if (startx, starty) not in pipes:
            pipes.append((startx, starty))
        step += 1
        if dir == "R":
            if 'J' in layout[starty][startx]:
                if starty > 0:
                    starty -= 1
                    dir = 'U'
            elif '-' in layout[starty][startx]:
                if startx+1 < len(layout[0]):
                    startx += 1
                    dir = 'R'

            elif '7' in layout[starty][startx]:
                if starty+1 < len(layout):
                    starty += 1
                    dir = 'D'
        elif dir == 'L':
            if 'L' in layout[starty][startx]:
                if starty > 0:
                    starty -= 1
                    dir = 'U'
            elif '-' in layout[starty][startx]:
                if startx > 0:
                    startx -= 1
                    dir = 'L'

            elif 'F' in layout[starty][startx]:
                if starty+1 < len(layout):
                    starty += 1
                    dir = 'D'
        elif dir == 'U':
            if '7' in layout[starty][startx]:
                if startx > 0:
                    startx -= 1
                    dir = 'L'
            elif '|' in layout[starty][startx]:
                if starty > 0:
                    starty -= 1
                    dir = 'U'
            elif 'F' in layout[starty][startx]:
                if startx+1 < len(layout[0]):
                    startx += 1
                    dir = 'R'
        elif dir == 'D':
            if 'J' in layout[starty][startx]:
                if startx > 0:
                    startx -= 1
                    dir = 'L'
            elif '|' in layout[starty][startx]:
                if starty+1 < len(layout):
                    starty += 1
                    dir = 'D'
            elif 'L' in layout[starty][startx]:
                if startx+1 < len(layout[0]):
                    startx += 1
                    dir = 'R'
    if layout[starty][startx] == 'S':
        print("Part1:", int(step/2))
        return True
    return False


startisUp = False
part1solved = False

# check which way to start:
startx, starty = findstart(layout)
if starty > 0:
    if re.match(r"(7|\||F)", layout[starty-1][startx]):
        part1solved = dostep(layout, startx, starty-1, 'U')
        startisUp = part1solved
if startx > 0 and part1solved == False:
    if re.match(r"(L|\-|F)", layout[starty][startx-1]):
        part1solved = dostep(layout, startx-1, starty, 'L')
if starty < len(layout)-1 and part1solved == False:
    if re.match(r"(J|\||L)", layout[starty+1][startx]):
        part1solved = dostep(layout, startx, starty+1, 'D')
if startx < len(layout[0])-1 and part1solved == False:
    if re.match(r"(J|\-|7)", layout[starty][startx+1]):
        part1solved = dostep(layout, startx+1, starty, 'R')


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
