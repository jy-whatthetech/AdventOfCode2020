f = open("d3.txt", "r")

f.readline()
line = f.readline()
width = len(line)

offset = 3
res = 0

while line and len(line) > 0:
    ind = offset % width
    c = line[ind]
    # print(c)
    res += 1 if c == "#" else 0
    line = f.readline()
    offset += 3

f.close()

print(res)

