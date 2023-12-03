f=open("day3/input.txt")

enginemap=[]


def main():

    for line in f:
        temp=[]
        for c in line.strip():
            temp.append(c)
        enginemap.append(temp)
    print_engine()

    sum=0
    line=0
    while line<len(enginemap):
        index=0
        number=False
        detectednumber=""
        while index<len(enginemap[0]):
            if enginemap[line][index].isnumeric():
                detectednumber=enginemap[line][index]
                number=True
                while number:
                    index=index+1
                    if index<len(enginemap) and enginemap[line][index].isnumeric():
                        detectednumber=detectednumber+enginemap[line][index]
                    else:
                        number=False
                        if checkadjacent(index-1,line,detectednumber):
                            sum=sum+int(detectednumber)
                        #print(int(detectednumber),checkadjacent(index-1,line,detectednumber))
                        
                #print(enginemap[line][index])
            index=index+1
        line=line+1
    print(sum)
        
        
        
def checkadjacent(index,line,detectednumber):
    startindex=index-len(detectednumber)
    adjacent=[]
    #start scan
    scanstart=(startindex if startindex>0 else 0)
    scanend=(index+1 if index+1<len(enginemap[0]) else len(enginemap[0])-1)
    linestart=(line-1 if line>0 else 0)
    lineend=(line+1 if line+1<len(enginemap) else len(enginemap)-1)
    for y in range(linestart,lineend+1):
        for x in range(scanstart,scanend+1):
            if not enginemap[y][x].isnumeric():
                adjacent.append(enginemap[y][x])
    for char in adjacent:
        if char!='.':
            return True
    return False



def print_engine():
    for y in enginemap:
        for x in y:
            print(x,end='')
        print()



main()