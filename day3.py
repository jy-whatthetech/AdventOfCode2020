

sofar = 1

right = 3
down = 1

for right, down in ([3,1], [1,1], [5,1], [7,1], [1,2]):
    f = open("d3.txt", "r")

    for i in range(0, down):
        f.readline()
    line = f.readline()
    width = len(line.strip())

    offset = right
    res = 0

    while line and len(line) > 0:
        ind = offset % width
        c = line[ind]
        # print(c)
        if c == "#":
            res += 1
        
        normal = True
        for i in range(1, down):
            temp = f.readline()
            if not temp or not len(temp):
                normal = False
                break

        if not normal:
            break

        line = f.readline()
        offset += right

    f.close()

    sofar *= res

print(sofar)

