def check(s):
    if len(s) != 6:
        return False
    for c in range(0, len(s)):
        if s[c:c+1] != "A" and s[c:c+1] != "T" and s[c:c+1] != "C" and s[c:c+1] != "G":
            return False
        c += 1
    else:
        return True

def is_mutant(adn, b):
    count1, count2, mut = 1,1,1
    for count1 in range(0,6):
        for count2 in range(0,6):
            if adn[count1][count2:count2+1] == adn[count1][count2+1:count2+2] and b == 1 and adn[count1][count2+1:count2+2] != "":
                mut += 1
            elif adn[count2][count1:count1+1] == adn[count2 + 1][count1:count1+1] and b == 2 and adn[count2 + 1] != "":
                mut += 1
            elif adn[count1][count2:count2+1] == adn[count1 + 1][count2+1:count2+2] and b == 3 and (adn[count1 + 1][count2+1:count2+2] != ""):
                mut += 1
            else:
                mut = 1
            if mut == 4:
                return True

