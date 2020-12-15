f = open("d15.txt", "r")

arr = []

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if line:
        arr.append( line )

    # END LINE READING

    line = f.readline()

f.close()

sp = arr[0].split(",")
nums = []
for s in sp:
    nums.append(int(s))

print(nums)

numToInd = {}
for i in range(0, len(nums)):
    val = nums[i]
    if val not in numToInd:
        numToInd[val] = []
    numToInd[val].append(i)
    
currsize = len(nums)
for i in range(currsize, 30000000):
    prev = nums[-1]
    inds = numToInd[prev]
    newval = 0
    if len(inds) >= 2:
        newval = inds[-1] - inds[-2]
    nums.append(newval)
    if newval not in numToInd:
        numToInd[newval] = []
    numToInd[newval].append(i)

print(nums[-1])


