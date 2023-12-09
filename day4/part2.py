f=open('day4/input.txt')
games=dict()

def main():
    
    parseinput()
    scores=dict()
    counts=dict()
    for game in games:
        scores[game]=getscore(game)
        counts[game]=1
    for game in counts:
        for j in range(counts[game]):
            for i in range(scores[game]):
                if i<len(games):
                    counts[game+i+1]+=1
    sum=0
    for i in counts:
        sum+=counts[i]
    print(sum)
        



def parseinput():
    for line in f:
        gameid=int(line.split(':')[0].split()[1])
        winning=line.split(':')[1].split('|')[0].split()
        mynumbers=line.strip().split(':')[1].split('|')[1].split()
        games[gameid]=(winning,mynumbers)


    
def getscore(game):
    count=0
    winning,mynumbers=games[game]
    for number in mynumbers:
        if number in winning:
            count=count+1
    return count
main()