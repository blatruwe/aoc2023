
f=open("day8/input.txt")
directions=""
path=dict()
for line in f:
    if directions=="":
        directions=line.strip()
    elif "=" in line:
        L,R=line.strip().split('=')[1].replace('(','').replace(')','').split(",")
        src=line.split('=')[0]
        path[src.strip()]=(L.strip(),R.strip())





step=0
start="AAA"
while start!='ZZZ':
    dir=directions[step%len(directions)]
    step+=1
    src=path[start]
    if dir=='L':
        start=src[0]
    else:
        start=src[1]

print(step)
