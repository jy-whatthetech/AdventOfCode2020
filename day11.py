f = open("d11.txt", "r")

arr = []
res = 0

def cpy(mat):
    matCopy = []
    for row in mat:
        rowCopy = row[:]
        matCopy.append(rowCopy)
    return matCopy

dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)] 

def getNumChanges(mat):
    changes = 0
    m, n = len(mat), len(mat[0])

    # mutate the array
    countArr = []
    for i in range(0, m):
        countArr.append([0] * n)


    def withinBounds(x, y):
        if x < 0 or y < 0 or x >= m or y >= n:
            return False
        return True

    def helper(i, j, plusi, plusj):
        state = 0
        while withinBounds(i, j):
            if state == 1:
                countArr[i][j] += 1

            curr = mat[i][j]
            if curr == 1:
                state = 1
            elif curr == 0:
                state = 0

            i += plusi
            j += plusj

    # for each row
    for i in range(0,m):
        helper(i, 0, 0, 1) # forward
        helper(i, n-1, 0, -1) # back

    # column
    for j in range(0, n):
        helper(0, j, 1, 0) # down
        helper(m-1, j, -1, 0) # up

    # diags
    for i in range(0,m):
        helper(i, 0, 1, 1)
    for j in range(1,n):
        helper(0, j, 1, 1)
    for i in range(0,m):
        helper(i, n-1, -1, -1)
    for j in range(0,n-1):
        helper(m-1, j, -1, -1)

    for i in range(0,m):
        helper(i, 0, -1, 1)
    for j in range(1,n):
        helper(m-1, j, -1, 1)
    for i in range(0,m):
        helper(i, n-1, 1, -1)
    for j in range(0,n-1):
        helper(0, j, 1, -1)

    for i in range(0,m):
        for j in range(0,n):
            if countArr[i][j] >= 5 and mat[i][j] == 1:
                mat[i][j] = 0
                changes += 1
            elif countArr[i][j] == 0 and mat[i][j] == 0:
                mat[i][j] = 1
                changes += 1

    return (changes, mat)

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if line:
        currArr = []
        arr.append(currArr)
        val = -1
        for c in line:
            if c == ".":
                val = -1
            elif c == "L":
                val = 0
            elif c == "#":
                val = 1
            currArr.append(val)

    # END LINE READING

    line = f.readline()

f.close()

# print(arr)


numChanges, nextarr = getNumChanges(arr)
while numChanges > 0:
    numChanges, nextarr = getNumChanges(nextarr)

res = 0

# print(nextarr)

m, n = len(nextarr), len(nextarr[0])
for i in range(0, m):
    for j in range(0, n):
        val = nextarr[i][j]
        if val == 1:
            res += 1

print(res)

