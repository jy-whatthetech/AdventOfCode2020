f = open("d2.txt", "r")

res = 0

line = f.readline().strip()
while line:
    arr = line.split(":")
    # print(arr)
    s = arr[1].strip()

    arr2 = arr[0].split(" ")
    # print(arr2)
    lohi = arr2[0].split("-")
    c = arr2[1]

    lo = int(lohi[0]) - 1
    hi = int(lohi[1]) - 1

    cnt = 0

    if lo < len(s) and s[lo] == c:
        cnt += 1
    if hi < len(s) and s[hi] == c:
        cnt += 1

    if cnt == 1:
        res += 1

    line = f.readline().strip()

f.close()

print(res)