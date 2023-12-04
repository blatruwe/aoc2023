f=open('input.txt')
games=dict()

def main():
    parseinput()
    sum=0
    for game in games:

        sum+=getscore(game)
    print(sum)

def parseinput():
    for line in f:
        gameid=line.split(':')[0].split()[1]
        winning=line.split(':')[1].split('|')[0].split()
        mynumbers=line.strip().split(':')[1].split('|')[1].split()
        games[gameid]=(winning,mynumbers)

    
def getscore(game):
    score=0
    winning,mynumbers=games[game]
    for number in mynumbers:
        if number in winning:
            if score==0:score=1
            else: score=score*2
    return score
main()