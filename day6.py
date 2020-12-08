f = open("d6.txt", "r")

res = 0

# seat id: multiply the row by 8, then add the column

arr = []
arr.append(set())

isnew = True

line = f.readline()
while line:
    line = line.strip()
    if len(line) == 0:
        s = set()
        arr.append(s)
        line = f.readline()
        isnew = True
        continue

    s = arr[-1]

    if isnew:
        for c in line:
            s.add(c)
        isnew = False
    else:
        toRemove = []
        temps = set()
        for c in line:
            temps.add(c)
        for c in s:
            if c not in temps:
                toRemove.append(c)
        for c in toRemove:
            s.discard(c)

    line = f.readline()

f.close()

res = 0
for s in arr:
    res += len(s)
print(res)