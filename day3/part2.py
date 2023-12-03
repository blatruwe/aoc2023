f=open("day3/input.txt")

enginemap=[]


def main():
    results=[]
    for line in f:
        enginemap.append(line.strip())
    print_engine()

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
                        sterretje=checkadjacent(index-1,line,detectednumber)
                        if sterretje is not None:
                            results.append((detectednumber,sterretje))
            index=index+1
        line=line+1
    listofstars=[]
    for number,ster in results:

        if ster not in listofstars:
            listofstars.append(ster)
    sum=0
    #count number of results:
    for ster in listofstars:
        ratio=1
        count=0
        for number,sterresult in results:
            if ster==sterresult:
                count=count+1
                ratio=int(number)*int(ratio)
        if count==2:
            sum=sum+ratio
    
    print(sum)
        
        
def checkadjacent(index,line,detectednumber):
    startindex=index-len(detectednumber)
    #start scan
    scanstart=(startindex if startindex>0 else 0)
    scanend=(index+1 if index+1<len(enginemap[0]) else len(enginemap[0])-1)
    linestart=(line-1 if line>0 else 0)
    lineend=(line+1 if line+1<len(enginemap) else len(enginemap)-1)
    for y in range(linestart,lineend+1):
        for x in range(scanstart,scanend+1):
            if not enginemap[y][x].isnumeric():
                if enginemap[y][x] == '*':
                    return (x,y)
    return None



def print_engine():
    for y in enginemap:
        for x in y:
            print(x,end='')
        print()



main()