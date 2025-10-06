# test thingy

def findLang():
    response = input("Give me something, and i'll find what language it's written in")
    tCount = response.count("t") + response.count("T")
    sCount = response.count("s") + response.count("S")
    if tCount > sCount:
        print("English (probably)")
    else:
        print("French (probably)")
findLang()