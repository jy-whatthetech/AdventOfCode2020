from collections import deque
f = open("d23.txt", "r")

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

class MyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

valToNode = {}

head = MyNode(-1)
tail = head

arr = []

for i,line in enumerate(collect[0]):
    # DO LOGIC ON FIRST PART
    for i, c in enumerate(line):
        val = int(c)
        nd = MyNode(val)
        valToNode[val] = nd

        tail.next = nd
        nd.prev = tail

        tail = tail.next

head = head.next

print(head.val)
print(tail.val)

curr = head


MAX = 1000000

# TODO: PART 2
for val in range(10, MAX + 1):
    nd = MyNode(val)
    valToNode[val] = nd

    tail.next = nd
    nd.prev = tail

    tail = tail.next

tail.next = head
head.prev = tail

for x in range(0, 10000000):
    removedNums = set()
    
    removedNums.add(curr.next.val)
    removedNums.add(curr.next.next.val)
    removedNums.add(curr.next.next.next.val)

    removeStart = curr.next
    removeEnd = curr.next.next.next

    targetVal = curr.val - 1
    if targetVal == 0:
        targetVal = MAX
    while targetVal in removedNums:
        targetVal -= 1
        if targetVal <= 0:
            targetVal = MAX

    targetNode = valToNode[targetVal]
    
    aStart = curr
    aEnd = removeEnd.next

    aStart.next = aEnd
    aEnd.prev = aStart

    bStart = targetNode
    bEnd = targetNode.next

    bStart.next = removeStart
    removeStart.prev = bStart
    removeEnd.next = bEnd
    bEnd.prev = removeEnd

    curr = aEnd

res = []
res1 = valToNode[1].next
res2 = valToNode[1].next.next
print(res1.val * res2.val)


    

# for i,line in enumerate(collect[1]):
#     # DO LOGIC ON SECOND PART


# res = 0
# for i, val in enumerate(arr):
#     # DO SOMETHING WITH RES
# print(res)

# circle, labeld clockwise
# circular array
# 100 moves
# remove 3 cups to right (loop over)
# dest cup: label = currVal - 1
# keep subtracting one until it finds a cup that wasn't just picked up