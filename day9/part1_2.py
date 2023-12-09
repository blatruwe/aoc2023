sequences=[[int(i) for i in line.strip().split()] for line in open("day9/input.txt")]

def analyze(sequence):
    diff=getdiff(sequence)
    if diff==[0]*len(diff):
        return sequence[-1]
    return analyze(diff)+ sequence[-1]
    
def getdiff(sequence):
    return [sequence[i]-sequence[i-1] for i in range(1,len(sequence))]

print("Part1:", sum([analyze(sequence) for sequence in sequences]))
print("Part2:", sum([analyze(sequence[::-1]) for sequence in sequences]))
