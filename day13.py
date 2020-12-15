import math

f = open("d13.txt", "r")

arr = []

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if line:
        arr.append(line)

    # END LINE READING

    line = f.readline()

f.close()

target = int(arr[0])
arr = arr[1].split(",")

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def lcm(x, y):
   return (x*y)//gcd(x,y)

nums = []
for i in range(0, len(arr)):
    if arr[i] != "x":
        nums.append((i, int(arr[i])))

sofar = nums[0][1]
sofarlcm = nums[0][1]
for i in range(1, len(nums)):
    curr = nums[i]
    b = curr[1]
    prev = nums[i-1]
    offset = curr[0] - prev[0]
    
    temp = sofar
    inc = 0
    while (temp + offset) % b != 0 and inc < 1000000:
        temp += sofarlcm
        inc += 1
    
    sofarlcm = lcm(temp, temp + offset)
    sofar = temp


print(sofar)
print(sofarlcm)


    