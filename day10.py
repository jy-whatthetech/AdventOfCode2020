f = open("d10.txt", "r")

arr = [0]
res = 0

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if line:
        arr.append(int(line))

    # END LINE READING

    line = f.readline()

f.close()

arr.sort()

# one = 0
# three = 1
dp = [1]
for i in range(1, len(arr)):
    curr = 0
    for j in [-1, -2, -3]:
        prevind = j + i
        if prevind < 0 or arr[i] - arr[prevind] > 3:
            break
        curr += dp[prevind]
    dp.append(curr)

print(dp[-1])
# print(one * three)
