f = open("d1.txt", "r")

arr = []

line = f.readline().strip()
while line:
    ival = int(line)
    arr.append(ival)
    line = f.readline().strip()

for i in range(0, len(arr) - 2):
    a = arr[i]
    for j in range(i + 1, len(arr) - 1):
        b = arr[j]
        for k in range(i + 2, len(arr)):
            c = arr[k]
            if a + b + c == 2020:
                print(a * b * c)
            

f.close()