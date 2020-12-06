f = open("d5.txt", "r")

res = 0

# seat id: multiply the row by 8, then add the column

ids = set()

line = f.readline().strip()
while line:
    curr = 0
    for i in range(0, 7):
        val = line[i]
        if val == "B":
            curr += 2 ** (6 - i)
    
    col = 0
    for i in range(0, 3):
        reali = 7 + i
        val = line[reali]
        if val == "R":
            col += 2 ** (2 - i)

    ans = curr * 8 + col

    if ans > res:
        res = ans
        # print(line)
        # print(curr)
        # print(col)

    ids.add(ans)

    line = f.readline().strip()

f.close()

lo, hi = min(ids), max(ids)
for i in range(lo, hi):
    if i not in ids:
        print(i)