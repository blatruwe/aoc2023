f=open("day6/input.txt")
for line in f:
    if "Time" in line:
        time=[int(i) for i in line.strip().split(':')[1].split()]
    elif "Distance" in line:
        distance=[int(i) for i in line.strip().split(':')[1].split()]
result=1
for i in range(len(time)):
    count=0
    for btnpushed in range(time[i]):
        if btnpushed*(time[i]-btnpushed)>distance[i]: count+=1
    result=result*count
print(result)