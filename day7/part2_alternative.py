f=open("day7/input.txt")

hands=[]


def gethandtype(cards):
    maximum=1
    for c in ["A","K","Q","T","9","8","7","6","5","4","3","2"]:
        r=gethandtype_replaced(cards.replace('J',c))
        if r>maximum:
            maximum=r
    return maximum

def gethandtype_replaced(cards):
    """
    1=high card
    2=one pair
    3=two pair
    4=three of a kind
    5=full house
    6=four of a kind
    7=full house
    """
    count_occurence=[]
    for i in range(len(cards)):
        #check same cards
        count_occurence.append(cards.count(cards[i]))
    if 5 in count_occurence: return 7
    elif 4 in count_occurence: return 6
    elif 3 in count_occurence:
        if 2 in count_occurence: return 5
        return 4
    elif 2 in count_occurence:
        if count_occurence.count(2)==4:
            return 3
        return 2
    return 1
    




for line in f:
    cards=line.strip().split()[0]
    bid=line.strip().split()[1]
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
    hands.append((handType,card_value,int(bid)))


rank=0
total=0
for hand in sorted(hands):
    rank+=1
    total+=rank*hand[2]
print(total)