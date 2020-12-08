f = open("d8.txt", "r")

arr = []

line = f.readline()
while line:
    line = line.strip()

    if line:

        temparr = line.split(" ")
        numstr = temparr[1]
        if numstr[0] == "+":
            numstr = numstr[1:]
        # print(numstr)
        numval = int(numstr)
        # print(numval)

    arr.append([temparr[0], numval])

    line = f.readline()

f.close()

old_arr = arr[:]
# print(old_arr)

for i in range(0, len(old_arr)):
    operator, value = old_arr[i]
    if operator == "acc":
        continue

    arr = old_arr[:]
    if operator == "nop":
        arr[i] = ["jmp", value]
    else:
        arr[i] = ["nop", value]

    res = 0
    seen = set()

    ind = 0
    while ind not in seen:
        if ind < 0:
            ind = 0

        if ind >= len(arr):
            break

        seen.add(ind)
        op, val = arr[ind]
        if op == "nop":
            ind += 1
        elif op == "acc":
            res += val
            ind += 1
        elif op == "jmp":
            ind += val

    if ind >= len(arr):
        print(res)


# print(res)

# print(arr)

# res = 0
# for s in arr:
#     res += len(s)
# print(res)