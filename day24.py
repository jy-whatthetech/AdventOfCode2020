f = open("d24.txt", "r")
lineArr = f.read().strip().split("\n")
f.close()

blackCoords = set()

for i, line in enumerate(lineArr):
    ind = 0
    x, y = 0, 0
    while ind < len(line):
        if line[ind] == "s" or line[ind] == "n":
            y += 1 if line[ind] == "n" else -1
            x += 0.5 if line[ind + 1] == "e" else -0.5
            ind += 2
        else:
            x += 1 if line[ind] == "e" else -1
            ind += 1

    pos = (x, y)

    if pos in blackCoords:
        blackCoords.discard(pos)
    else:
        blackCoords.add(pos)

neighbors = [(1, 0), (-1, 0), (-0.5, 1), (0.5, 1), (-0.5, -1), (0.5, -1)]

curr = blackCoords
for t in range(0, 100):
    next = curr.copy()

    whiteToBlackNeighbors = {} # map of white tiles to how many neighbors are black tiles

    for pos in curr:
        x, y = pos
        cnt = 0 # count of black neighbors
        for xoff, yoff in neighbors:
            neighbor = (xoff + x, yoff + y)
            if neighbor in curr:
                cnt += 1
            else:
                whiteToBlackNeighbors[neighbor] = whiteToBlackNeighbors.get(neighbor, 0) + 1
        if cnt == 0 or cnt > 2:
            next.discard(pos)

    for key in whiteToBlackNeighbors:
        if whiteToBlackNeighbors[key] == 2:
            next.add(key)

    curr = next

print(len(curr))
