f = open("d20.txt", "r")

collect = [[]]

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE
    if not line:
        collect.append([])
    else:
        collect[-1].append(line)

    # END LINE READING
    line = f.readline()

f.close()

idToAllOrientations = {}

def rotateClockwise(grid):
    m, n = len(grid), len(grid[0])
    ret = []
    for i in range(0, m):
        ret.append([0] * n)
    
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            ret[j][n - 1 - i] = val
    return ret

def getAllOrientations(grid, container):
    container.append(grid)
    nxt = rotateClockwise(grid)
    container.append(nxt)
    nxt = rotateClockwise(nxt)
    container.append(nxt)
    nxt = rotateClockwise(nxt)
    container.append(nxt)

def flip(grid):
    ret = []
    for row in grid:
        rev = row[::-1]
        ret.append(rev)
    return ret

for group in collect:
    num = -1
    grid = []
    orientations = []
    for i, line in enumerate(group):
        if i == 0:
            sp = line.split(" ")
            num = int(sp[1][:-1])
        else:
            tempArr = []
            grid.append(tempArr)
            for c in line:
                tempArr.append(c)
    
    getAllOrientations(grid, orientations)
    grid = flip(grid)
    getAllOrientations(grid, orientations)
            
    idToAllOrientations[num] = orientations

def printGrid(grid):
    for row in grid:
        print(row)

def convertToNum(grid):
    m, n = len(grid), len(grid[0])
    sides = [0,0,0,0] # top, bottom, left, right
    for j in range(0, n):
        if grid[0][j] == "#":
            sides[0] += 1 << j
        if grid[m - 1][j] == "#":
            sides[1] += 1 << j
    
    for i in range(0, m):
        if grid[i][0] == "#":
            sides[2] += 1 << i
        if grid[i][n - 1] == "#":
            sides[3] += 1 << i

    return sides

possTops = [[] for x in range(0, 1024)]
possBottoms = [[] for x in range(0, 1024)]
possLefts = [[] for x in range(0, 1024)]
possRights = [[] for x in range(0, 1024)]

for id in idToAllOrientations:
    numReps = []
    for orientation in idToAllOrientations[id]:
        numRep = convertToNum(orientation)
        numRep.append(id)
        numRep.append(orientation) # TOGGLE
        numReps.append(numRep)
    
        possTops[numRep[0]].append(numRep)
        possBottoms[numRep[1]].append(numRep)
        possLefts[numRep[2]].append(numRep)
        possRights[numRep[3]].append(numRep)

    idToAllOrientations[id] = numReps

cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
uniques = set()
for i, l in enumerate(possTops):
    if len(l) == 1:
        uniques.add(i)
        cnt1 += 1
    if len(l) == 2:
        cnt2 += 1
    if len(l) == 3:
        cnt3 += 1
    if len(l) == 4:
        cnt4 += 1

idToNumMatches = {}
uCntToIds = {}
for id in idToAllOrientations:
    numUniq = 0
    for ornt in idToAllOrientations[id]:
        for x in range(0, 4):
            if ornt[x] in uniques:
                numUniq += 1
    if numUniq not in uCntToIds:
        uCntToIds[numUniq] = []
    uCntToIds[numUniq].append(id)

res = 1
for id in uCntToIds[16]:
    res *= id
# print(res)

SOLVED = False

anchor = idToAllOrientations[uCntToIds[16][0]][0]
# ANCHOR IS TOP LEFT

grid = [[] for x in range(0, 12)]

row = grid[0]
row.append(anchor)
rightEdge = anchor[3]
while len(possLefts[rightEdge]) > 1:
    for arr in possLefts[rightEdge]:
        if arr[4] != row[-1][4]:
            row.append(arr)
            break
    rightEdge = row[-1][3]

bottomEdge = anchor[1]
ind = 1
while len(possTops[bottomEdge]) > 1:
    for arr in possTops[bottomEdge]:
        if arr[4] != grid[ind - 1][0][4]:
            grid[ind].append(arr)
            break
    bottomEdge = grid[ind][-1][1]
    ind += 1

for i in range(1, 12):
    row = grid[i]
    for j in range(1, 12):
        rightEdge = row[-1][3]

        for arr in possLefts[rightEdge]:
            if arr[4] != row[-1][4]:
                row.append(arr)
                break

actualGrid = []
for i in range(0, 96):
    actualGrid.append([0] * 96)

for i in range(0, 12):
    for j in range(0, 12):
        val = grid[i][j]
        picGrid = val[-1]
        
        ioffset = i * 8
        joffset = j * 8

        for pi in range(1,9):
            for pj in range(1,9):
                actuali = ioffset + pi - 1
                actualj = joffset + pj - 1
                
                actualGrid[actuali][actualj] = picGrid[pi][pj]

smOffsets = [(0, 18)]
for x in [0,5,6,11,12,17,18,19]:
    smOffsets.append( (1, x) )

for x in [1,4,7,10,13,16]:
    smOffsets.append( (2, x) )

def findSM(grid):
    print("Calculating new orientation...")
    smFound = False
    for i in range(0, 96 - 3):
        for j in range(0, 96 - 20):
            isSM = True
            for xoff, yoff in smOffsets:
                x = xoff + i
                y = yoff + j
                if grid[x][y] != "#":
                    isSM = False
                    break

            if isSM:
                smFound = True
                print("SM FOUND!!!")
                for xoff, yoff in smOffsets:
                    x = xoff + i
                    y = yoff + j
                    grid[x][y] = "O"
    
    if smFound:
        res = 0
        for i in range(0,96):
            for j in range(0, 96):
                if grid[i][j] == "#":
                    res += 1
        print(res)


container = []

getAllOrientations(actualGrid, container)
actualGrid = flip(actualGrid)
getAllOrientations(actualGrid, container)

for ornt in container:
    findSM(ornt)

# print(row)
# test
# for poss in idToAllOrientations[3169]:
#     printGrid(poss)
#     print(" ")