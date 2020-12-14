f = open("d14.txt", "r")

arr = []

def getMask(s):
    orMask = 0
    andMask = 2**36 - 1
    for i in range(0, len(s)):
        ind = 35 - i
        if s[ind] == "1":
            orMask = orMask | 2**i
        elif s[ind] == "0":
            andMask = andMask ^ 2**i
    return (orMask, andMask)

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if line:
        sp = line.split(" = ")
        if sp[0] == "mask":
            arr.append([ sp[1] ])
        else:
            val = int(sp[1])
            mem = int(sp[0][4:-1])
            arr[-1].append((mem, val))

    # END LINE READING

    line = f.readline()

f.close()

# print(arr)

def applyMask(orMask, andMask, val):
    val |= orMask
    val &= andMask
    return val

def generateAllPossibleAddresses(mask, mem):
    res = []
    orMask = 0
    changingInds = []
    for i in range(0, len(mask)):
        ind = 35 - i
        if mask[ind] == "1":
            orMask = orMask | 2**i
        elif mask[ind] == "X":
            changingInds.append(i)
    
    mem = mem | orMask
    # print(changingInds)
    genHelper(mem, changingInds, 0, res)

    return res

def genHelper(currVal, inds, currInd, container):
    if currInd >= len(inds):
        container.append(currVal)
        return
    indVal = inds[currInd]
    nextVal1 = currVal | (2**indVal)
    nextVal0 = currVal & ((1 << 36) - 1 - (2**indVal))
    genHelper(nextVal1, inds, currInd + 1, container)
    genHelper(nextVal0, inds, currInd + 1, container)

memToVal = {}

for subarr in arr:
    mask = subarr[0]
    for i in range(1, len(subarr)):
        mem, val = subarr[i]

        allAdd = generateAllPossibleAddresses(mask, mem)

        for add in allAdd:
            memToVal[add] = val

# print(memToVal)

tot = 0

for key in memToVal:
    tot += memToVal[key]
print(tot)
    