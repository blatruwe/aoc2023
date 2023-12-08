import re
import time
import numpy as np
start_time = time.time()
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
start=[]
#search for start
for p in path:
    if re.fullmatch(r"..A",p):
        start.append(p)
steps_to_dest=[]
for s in start:
    step=0
    while s[2]!='Z':
        dir=directions[step%len(directions)]
        step+=1
        L,R=path[s]
        s=L if dir=='L' else R
    steps_to_dest.append(step)

print(np.lcm.reduce(steps_to_dest))
print("--- %s seconds ---" % (time.time() - start_time))