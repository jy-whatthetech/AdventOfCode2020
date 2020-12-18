f = open("d17.txt", "r")

arr = []

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    arr.append(line)

    # END LINE READING

    line = f.readline()

f.close()

a = len(arr[0])
b = len(arr)

# get coords, put in set
# if not in set, inactive
activeSet = set()

z = 0
y = 0
t = 0
for l in arr:
    for x in range(0, len(l)):
        val = l[x]
        if val == "#":
            activeSet.add( (x, y, z, t) )
    y += 1

print(activeSet)

allPoss = []
for t in (-1,0,1):
    for u in (-1,0,1):
        for v in (-1,0,1):
            for w in (-1,0,1):
                if t == 0 and u == 0 and v == 0 and w == 0:
                    continue
                allPoss.append( [t,u,v, w] )

# bfs
curr = activeSet
for n in range(0, 6):
    nxt = set()
    for x in range(-1 - n, a + 1 + n):
        for y in range(-1 - n, b + 1 + n):
            for z in range(-1 - n, 2 + n):
                for t in range(-1 - n, 2 + n):
                    isActive = False
                    myP = (x,y,z, t)
                    if myP in curr:
                        isActive = True

                    aCnt = 0
                    for xo,yo,zo,to in allPoss:
                        neighbor = (xo + x, yo+y, zo+z, t + to)
                        if neighbor in curr:
                            aCnt += 1
                    if aCnt == 3:
                        nxt.add(myP)
                    elif aCnt == 2 and isActive:
                        nxt.add(myP)


    curr = nxt

print(len(curr))

