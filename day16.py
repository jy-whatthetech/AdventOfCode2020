f = open("d16.txt", "r")

arr = [[]]

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if line:
        arr[-1].append( line )
    else:
        arr.append([])

    # END LINE READING

    line = f.readline()

f.close()

# CLASS TO RANGE
classToRange = {}
validRanges = []
for row in arr[0]:
    key, textRange = row.split(":")
    r1, r2 = textRange.split(" or ")
    
    r1sp = [int(x) for x in r1.split("-")]
    r2sp = [int(x) for x in r2.split("-")]

    # print(key)
    # print(r1sp)
    # print(r2sp)

    classToRange[key] = (r1sp, r2sp)

    validRanges.append(r1sp)
    validRanges.append(r2sp)

# YOUR TICKET
myTicket = []
sp = arr[1][1].split(",")
for s in sp:
    myTicket.append(int(s))

# NEARBY TICKETS
nearbyTickets = []
for i in range(1, len(arr[2])):
    toAdd = []
    nearbyTickets.append(toAdd)
    sp = arr[2][i].split(",")
    for s in sp:
        toAdd.append(int(s))
# print(nearbyTickets)


# num of invalid
validTickets = []
res = 0
for ticket in nearbyTickets:
    tValid = True
    for n in ticket:
        isValid = False
        for a, b in validRanges:
            if n >= a and n <= b:
                isValid = True
                break
        if not isValid:
            res += n
            tValid = False
            break
    if tValid:
        validTickets.append(ticket)

# normalize
valueSets = []
for i in range(0, len(myTicket)):
    toAdd = [myTicket[i]]
    valueSets.append(toAdd)
    
    for ticket in validTickets:
        toAdd.append(ticket[i])

# for each range, list the indexes of the valueSets that satisfy this range
classToIndexes = {}
for key in classToRange:
    toAdd = []
    classToIndexes[key] = toAdd
    r1, r2 = classToRange[key]
    a, b = r1
    c, d = r2

    for i, valueList in enumerate(valueSets):
        r1satisfied = False
        r2satisfied = False
        isValid = True

        for n in valueList:
            if n >= a and n <= b:
                r1satisfied = True
            elif n >= c and n <= d:
                r2satisfied = True
            else:
                isValid = False
                break

        if isValid and r1satisfied and r2satisfied:
            toAdd.append(i)

print(classToIndexes)

keySet = set(classToIndexes.keys())
results = {}

occupied = [0] * len(myTicket)

while len(keySet):

    for key in keySet:
        possibleCount = 0
        possIndex = -1

        inds = classToIndexes[key]
        for currInd in inds:
            if not occupied[currInd]:
                possibleCount += 1
                possIndex = currInd

        if possibleCount == 1:
            occupied[possIndex] = 1
            results[key] = possIndex
            break
    
    for key in results:
        keySet.discard(key)

print(results)

res = 1

for key in results:
    if key.find('departure') == 0:
        res *= myTicket[results[key]]

print(res)