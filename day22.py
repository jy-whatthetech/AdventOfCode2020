from collections import deque
f = open("d22.txt", "r")

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

arr1 = []
arr2 = []

for i,line in enumerate(collect[0]):
    if i> 0:
        arr1.append(int(line))
for i,line in enumerate(collect[1]):
    if i> 0:
        arr2.append(int(line))

def ser(dq1, dq2):
    temp = []
    for n in dq1:
        temp.append(str(n) + ",")
    temp.append("--")
    for n in dq2:
        temp.append(str(n) + ",")
    return "".join(temp)

def rc(dq1, dq2):
    seen = set()
    while len(dq1) and len(dq2):
        strRep = ser(dq1, dq2)
        if strRep in seen:
            return (dq1, 1)
        seen.add(strRep)

        # play game
        a, b = dq1.popleft(), dq2.popleft()

        rem1, rem2 = len(dq1), len(dq2)
        if rem1 >= a and rem2 >= b:
            # RECURSE
            ra = deque([])
            rb = deque([])
            for i in range(0, a):
                ra.append(dq1[i])
            for i in range(0, b):
                rb.append(dq2[i])
            winDQ, winPlayer = rc(ra, rb)
            if winPlayer == 1:
                dq1.append(a)
                dq1.append(b)
            else:
                dq2.append(b)
                dq2.append(a)
        else:
            if a > b:
                # 1 wins
                dq1.append(a)
                dq1.append(b)
            else:
                dq2.append(b)
                dq2.append(a)

    if len(dq1):
        return (dq1, 1)
    else:
        return (dq2, 2)

winner, player = rc(deque(arr1), deque(arr2))

res = 0
mult = 1
for i in range(len(winner) - 1, -1, -1):
    res += mult * winner[i]
    mult += 1
print(res)

