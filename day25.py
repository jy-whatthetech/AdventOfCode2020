f = open("d25.txt", "r")
lineArr = f.read().strip().split("\n")
f.close()

pubKey1, pubKey2 = [int(x) for x in lineArr]


def getLoopSize(subject, pubKey):
    loop = 0
    curr = 1
    while True:
        if curr == pubKey:
            return loop
        loop += 1
        curr = (curr * subject) % 20201227


def getEncKey(subject, loopSize):
    curr = 1
    for x in range(0, loopSize):
        curr = (curr * subject) % 20201227
    return curr


part1 = getEncKey(pubKey2, getLoopSize(7, pubKey1))

print(part1)
