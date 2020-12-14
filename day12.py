f = open("d12.txt", "r")

arr = []

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if line:
        arr.append( (line[0], int(line[1:]) ) )
        if line[0] == "R" or line[0] == "L":
            print(int(line[1:]))

    # END LINE READING

    line = f.readline()

f.close()

print(arr)

d = 0
dirMap = {}

# for i in range(0, len(arr)):
    



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
