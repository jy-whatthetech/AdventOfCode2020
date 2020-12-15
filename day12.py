f = open("d12.txt", "r")

arr = []

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if line:
        arr.append( (line[0], int(line[1:]) ) )

    # END LINE READING

    line = f.readline()

f.close()

# print(arr)

d = 1
wp = [10, 1]
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
pos = [0,0]
dirMap = {"N": 0, "E": 1, "S": 2, "W": 3}


for i in range(0, len(arr)):
    c, mag = arr[i]
    if c in dirMap:
        xoff, yoff = dirs[dirMap[c]]
        wp[0] += xoff * mag
        wp[1] += yoff * mag
    elif c == "F":
        pos[0] += (wp[0] * mag)
        pos[1] += (wp[1] * mag)
    else: # L or R
        rot = mag // 90
        if c == "L":
            rot = 4 - rot
        if rot == 2:
            wp[0] *= -1
            wp[1] *= -1
        elif rot == 1:
            temp = wp[0]
            wp[0] = wp[1]
            wp[1] = -temp
        elif rot == 3:
            temp = wp[0]
            wp[0] = -wp[1]
            wp[1] = temp

print(abs(pos[0]) + abs(pos[1]))


# # one = 0
# # three = 1
# dp = [1]
# for i in range(1, len(arr)):
#     curr = 0
#     for j in [-1, -2, -3]:
#         prevind = j + i
#         if prevind < 0 or arr[i] - arr[prevind] > 3:
#             break
#         curr += dp[prevind]
#     dp.append(curr)

# print(dp[-1])
# # print(one * three)