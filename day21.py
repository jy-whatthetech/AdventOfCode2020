f = open("d21.txt", "r")

collect = []

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE
    collect.append(line)

    # END LINE READING
    line = f.readline()

f.close()

arr = []

allgToIng = {}

for line in collect:
    sp = line.split(" ")
    ing = set()
    start = -1
    for i, word in enumerate(sp):
        if word[0] == "(":
            start = i
            break
        ing.add(word)
    allg = []
    for i in range(start + 1, len(sp)):
        word = sp[i]
        allg.append(word[:-1])

    arr.append((ing, allg))

    # for each allergen, point to set
    for g in allg:
        if g not in allgToIng:
            allgToIng[g] = []
        allgToIng[g].append(ing)

gSet = set()
for g in allgToIng:
    listOfSets = allgToIng[g]
    base = listOfSets[0].copy()
    for i, s in enumerate(listOfSets):
        if i > 0:
            base = base.intersection(s)
    print(g)
    print(base)

    gSet = gSet.union(base)

res = 0

for line in collect:
    sp = line.split(" ")
    for i, word in enumerate(sp):
        if word[0] == "(":
            break
        if word not in gSet:
            res += 1
# print(res)


