f=open("day7/input.txt")



def gethandtype(cards):
    """
    1=high card
    2=one pair
    3=two pair
    4=three of a kind
    5=full house
    6=four of a kind
    7=five of a kind
    """
    count_occurence=[]
    J_occurence=0
    for i in range(len(cards)):
        #check same cards
        count_occurence.append(cards.count(cards[i]))
        if cards[i]=='J': J_occurence+=1
    if 5 in count_occurence: return 7
    elif 4 in count_occurence:
        if J_occurence>0: return 7 # AAAAJ -> AAAAA | JJJJA -> AAAAA
        return 6
    elif 3 in count_occurence:
        if 2 in count_occurence: 
            if J_occurence>0: return 7 # JJJAA -> AAAAA of JJAAA -> AAAAA
            return 5
        if J_occurence>0: return 6 #JAAA2 -> AAAA2
        return 4
    elif 2 in count_occurence:
        if count_occurence.count(2)==4:
            if J_occurence==2: return 6 #JJAA2 -> AAAA2
            elif J_occurence==1: return 5 #AAJ22 -> AAA22
            return 3
        if J_occurence>0: return 4 #AAJ23 -> AAA23 of JJ234 -> 22234
        return 2
    if J_occurence==1: return 2
    return 1

 
hands=[]
for line in f:
    cards=line.strip().split()[0]
    handType=gethandtype(cards)
    card_value=[]
    for card in cards:
        if card=='A':
            card_value.append(14)
        elif card=='K':
            card_value.append(13)
        elif card=='Q':
            card_value.append(12)
        elif card=='J':
            card_value.append(1)
        elif card=='T':
            card_value.append(10)
        else:
            card_value.append(int(card))
    hands.append((handType,card_value,int(line.strip().split()[1])))


rank=0
total=0
for hand in sorted(hands):
    rank+=1
    total+=rank*hand[2]
print(total)