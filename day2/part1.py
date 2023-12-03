f=open("day2/input.txt")

def main():
    valid=[]
    for gamestring in f:
        gameid=int(gamestring.split(":")[0].split()[1])
        gamerounds=gamestring.strip().split(":")[1].split(";")
        gameispossible=True
        for round in gamerounds:
            red=0
            green=0
            blue=0
            for colors in round.split(','):
                if colors.split()[1]=='blue':
                    blue=int(colors.split()[0])
                elif colors.split()[1]=='red':
                    red=int(colors.split()[0])
                elif colors.split()[1]=='green':
                    green=int(colors.split()[0])
        
            if not ispossible(red,green,blue):
                gameispossible=False
        if (gameispossible):
            valid.append(gameid)

    print(sumarray(valid))
    
    
def sumarray(arr):
    sum=0
    for i in arr:
        sum = sum + i
 
    return(sum)
        

def ispossible(red,green,blue):
    if red>12: return False
    if green>13: return False
    if blue>14: return False
    return True
    

main()