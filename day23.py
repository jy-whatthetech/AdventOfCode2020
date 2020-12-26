f = open("d23.txt", "r")
lineArr = f.read().strip().split("\n")
f.close()

MAX = 1000000  # number of iterations (moves)


class MyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


valToNode = {}

head = MyNode(-1)
tail = head

for i, line in enumerate(lineArr):
    for c in line:
        val = int(c)
        nd = MyNode(val)
        valToNode[val] = nd

        tail.next = nd
        nd.prev = tail

        tail = tail.next

head = head.next

for val in range(10, MAX + 1):
    nd = MyNode(val)
    valToNode[val] = nd

    tail.next = nd
    nd.prev = tail

    tail = tail.next

tail.next = head
head.prev = tail

curr = head
for x in range(0, 10000000):
    removedNums = set()

    removedNums.add(curr.next.val)
    removedNums.add(curr.next.next.val)
    removedNums.add(curr.next.next.next.val)

    removeStart = curr.next
    removeEnd = curr.next.next.next

    targetVal = curr.val
    while True:
        targetVal -= 1
        if targetVal == 0:
            targetVal = MAX
        if targetVal not in removedNums:
            break

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

print(valToNode[1].next.val * valToNode[1].next.next.val)
