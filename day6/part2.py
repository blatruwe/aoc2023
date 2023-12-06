f=open("day6/input.txt")
for line in f:
    if "Time" in line:
        time=int(line.strip().split(":")[1].replace(' ',''))
    elif "Distance" in line:
        distance=int(line.strip().split(":")[1].replace(' ',''))

print(sum(1 for btnpushed in range(time) if btnpushed*(time-btnpushed)>distance))
