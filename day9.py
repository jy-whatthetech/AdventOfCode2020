f = open("d8.txt", "r")

arr = []

line = f.readline()
while line:
    line = line.strip()

    if line:
        arr.append(int(line))

    line = f.readline()

f.close()

for i in range(25, len(arr)):
    s = set()
    for j in range(i - 25, i - 1):
        for k in range(j + 1, i):
            s.add(arr[j] + arr[k])
    
    if arr[i] not in s:
        print(arr[i])
        break

target = 41682220

for i in range(0, len(arr)):
    sofar = 0
    s = set()
    for j in range(i, len(arr)):
        sofar += arr[j]
        s.add(arr[j])

        if sofar >= target:
            break
    if sofar == target:
        print(min(s))
        print(max(s) + min(s))

        break
