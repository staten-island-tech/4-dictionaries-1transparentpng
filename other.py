# test thingy

def findLang():
    response = input("Give me something, and i'll find what language it's written in")
    tCount = response.count("t") + response.count("T")
    sCount = response.count("s") + response.count("S")
    if tCount > sCount:
        print("English (probably)")
    else:
        print("French (probably)")

def findLangDiff(x):
    t = 0
    s = 0
    for char in x: # for every character in the given line (x var)
        if char == "t" or "T":
            t += 1
        elif char == "s" or "S":
            s += 1
    if t > s:
        print("English (prob)")
    else:
        print("French (prob)")


def parkingSpaces(spaces,yest,today):
    both = 0
    for i in range(spaces):
        if (yest[i] == "C" and today[i] == "C"):
            both += 1
    return both
print(parkingSpaces(5, "CCC..", "C.C.C"))