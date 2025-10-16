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
    for i in range(spaces): # for the number of spaces specified:
        if (yest[i] == "C" and today[i] == "C"): # if the letter that i is specifying the position of is equal to "C" for both yesterday and today then
            both += 1 # add 1 to both, meaning there was 1 occupied space both today and yesterday
    return both # associates the both var with the function after loop is done



def gradeTest(n,s,a):
    correct = 0
    for i in range(n): # didn't add range, but did n(s) instead, which throws an error
        if s[i] == a[i]: # forgot to add [i] after vars
            correct += 1
    return correct
