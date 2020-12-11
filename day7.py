f = open("d7.txt", "r")

arr = [0]
res = 0

m = {}
backlink = {}

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if line:
        sp = line.split(" ")
        src = sp[0] + " " + sp[1]

        i = 4
        while i < len(sp):
            if i + 3 >= len(sp):
                break
            currCnt = int(sp[i])
            currColor = sp[i + 1] + " " + sp[i + 2]

            pair = (currColor, currCnt)
            if src not in m:
                m[src] = []
            m[src].append(pair)

            if currColor not in backlink:
                backlink[currColor] = []
            backlink[currColor].append(src)

            i += 4

    # END LINE READING

    line = f.readline()

f.close()

# print(backlink)

# allParents = set()
# curr = set()
# curr.add("shiny gold")
# while len(curr):
#     next = set()

#     for color in curr:
#         if color in backlink:
#             for b in backlink[color]:
#                 next.add(b)
#                 allParents.add(b)

#     curr = next

print(m)

# part 2
def dfs(color):
    if color not in m:
        return 0
    children = m[color]
    res = 0
    for childColor, count in children:
        res += count
        res += count * dfs(childColor)
    return res


print(dfs("shiny gold"))
