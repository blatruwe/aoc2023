f=open("day1/input.txt")
sum=0
for line in f:
    first=""
    last=""
    for c in line.strip():
        if c.isnumeric():
            if first=="":
                first=c
            last=c
    value=int(first+last)
    sum=sum+value
print(sum)


