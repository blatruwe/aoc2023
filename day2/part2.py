f=open("day2/input.txt")

def main():
    sum=0
    for gamestring in f:
        gamerounds=gamestring.strip().split(":")[1].split(";")
        min_red=0
        min_blue=0
        min_green=0
        for round in gamerounds:
            for colors in round.split(','):
                if colors.split()[1]=='blue':
                    blue=int(colors.split()[0])
                    if blue>min_blue:
                        min_blue=blue
                elif colors.split()[1]=='red':
                    red=int(colors.split()[0])
                    if red>min_red:
                        min_red=red
                elif colors.split()[1]=='green':
                    green=int(colors.split()[0])
                    if green>min_green:
                        min_green=green
        power=min_red*min_green*min_blue
        sum=sum+power 
            
    print(sum)


    
 

main()