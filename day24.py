from collections import deque
f = open("d24.txt", "r")

collect = [[]]

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE
    if len(line):
        collect[-1].append(line)
    else:
        collect.append([])

    # END LINE READING
    line = f.readline()

f.close()

arr = []

dir = ["n","e","s","w"]
s = set()

for i,line in enumerate(collect[0]):
    # DO LOGIC ON FIRST PART
    i = 0
    x = 0
    y = 0
    while i < len(line):
        if line[i] == "s" or line[i] == "n":
            
            d = line[i] + line[i+1]
            if d[0] == "n":
                y += 1
            else:
                y -= 1
            
            if d[1] == "e":
                x += 0.5
            else:
                x -= 0.5

            i += 2
                
        else:
            d = line[i]
            i+= 1
            if d == "e":
                x += 1
            else:
                x -= 1


    pos = (x, y)
    print(pos)

    if pos in s:
        # print("EXISTS")
        s.discard(pos)
    else:
        # print("ADD")
        s.add(pos)

hi, lo, left, right = float("-inf"), float("inf"),float("inf"),float("-inf")
for pos in s:
    hi = max(hi, pos[0])
    lo = min(lo, pos[0])
    right = max(right, pos[1])
    left = min(left, pos[1])

nb = [(1,0),(-1,0),(-0.5,1), (0.5,1), (-0.5,-1), (0.5,-1)]

curr = s
for t in range(0,100):
    next = curr.copy()

    wcnt = {}

    for pos in curr:
        x, y = pos
        cnt = 0
        for xoff, yoff in nb:
            newx = xoff + x
            newy = yoff + y
            if (newx, newy) in curr:
                cnt += 1
            else:
                wcnt[(newx, newy)] = wcnt.get((newx, newy), 0) + 1
        if cnt == 0 or cnt > 2:
            next.discard((x,y))
    
    for key in wcnt:
        if wcnt[key] == 2:
            next.add(key)

    curr = next

print(len(curr))