f=open("day1/input.txt")

def main():
    sum=0

    for line in f:
        start=line.strip()
        first=None
        while checkstring(start) is None:
            start=start[1:]
        first=checkstring(start)
        end=line.strip()
        while checkendstring(end) is None:
            end=end[:-1]
        last=checkendstring(end)
        sum=sum+int(str(first)+str(last))
    print(sum)
    
    
def checkstring(line):
    if line[0].isnumeric():
        return int(line[0])
    if line[0:3]=="one":
        return 1
    if line[0:3]=="two":
        return 2
    if line[0:5]=="three":
        return 3
    if line[0:4]=="four":
        return 4
    if line[0:4]=="five":
        return 5
    if line[0:3]=="six":
        return 6
    if line[0:5]=="seven":
        return 7
    if line[0:5]=="eight":
        return 8
    if line[0:4]=="nine":
        return 9


def checkendstring(line):
    if line[-1].isnumeric():
        return int(line[-1])
    if line[-3:]=="one":
        return 1
    if line[-3:]=="two":
        return 2
    if line[-5:]=="three":
        return 3
    if line[-4:]=="four":
        return 4
    if line[-4:]=="five":
        return 5
    if line[-3:]=="six":
        return 6
    if line[-5:]=="seven":
        return 7
    if line[-5:]=="eight":
        return 8
    if line[-4:]=="nine":
        return 9
main()