import re

f = open("d19.txt", "r")

collect = [[]]

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    if not line:
        collect.append([])
    collect[-1].append(line)

    # END LINE READING

    line = f.readline()

f.close()

ruleMap = {}

# process rules
for line in collect[0]:
    toAdd = []
    # ADD WHAT YOU WANT TO DO TO EACH LINE HERE
    key, rules = line.split(": ")
    rulesp = rules.split(" ")
    if rules.find("|") >= 0:
        # add paren
        toAdd.append("(")
        toAdd.append("?")
        toAdd.append(":")
        toAdd.extend(rulesp)
        toAdd.append(")")
    else:
        if rulesp[0].find('"') >= 0:
            toAdd.append(rulesp[0][1:2])
        else:
            toAdd.extend(rulesp)

    # print(toAdd)

    ruleMap[key] = toAdd

s8 = "(?:(?:(?:(?:b(?:b(?:b(?:aa|bb)|a(?:aa|b(?:b|a)))|a(?:b(?:aa|bb)|aba))|a(?:b(?:b(?:ba|aa)|aab)|a(?:b|a)(?:aa|b(?:b|a))))a|(?:a(?:b(?:aba|(?:a(?:b|a)|ba)b)|a(?:bba|a(?:aa|b(?:b|a))))|b(?:(?:a(?:aa|bb)|b(?:aa|b(?:b|a)))a|(?:aba|(?:a(?:b|a)|ba)b)b))b)a|(?:(?:b(?:(?:bba|a(?:bb|ab))b|(?:aba|(?:a(?:b|a)|ba)b)a)|a(?:b(?:(?:ba|bb)b|(?:bb|ab)a)|a(?:(?:ba|ab)a|(?:ba|aa)b)))b|(?:a(?:a(?:(?:a(?:b|a)|bb)b|baa)|b(?:(?:a(?:b|a)|bb)a|(?:a(?:b|a)|ba)b))|b(?:a(?:b(?:a(?:b|a)|ba)|a(?:aa|b(?:b|a)))|b(?:(?:bb|ab)b|aba)))a)b)a|(?:a(?:(?:(?:a(?:(?:aa|ab)b|(?:ba|ab)a)|b(?:ba|ab)b)a|(?:babb|(?:(?:ba|bb)b|bba)a)b)a|(?:(?:a(?:aba|b(?:aa|b(?:b|a)))|b(?:bbb|bba))b|(?:a(?:b(?:a(?:b|a)|ba)|a(?:bb|ab))|b(?:b(?:aa|bb)|a(?:a(?:b|a)|ba)))a)b)|b(?:a(?:a(?:b(?:b(?:bb|ab)|a(?:b|a)(?:b|a))|a(?:abb|b(?:ab|b(?:b|a))))|b(?:(?:b(?:a(?:b|a)|ba)|a(?:bb|ab))a|(?:b(?:aa|bb)|a(?:aa|b(?:b|a)))b))|b(?:(?:(?:b(?:a(?:b|a)|ba)|a(?:aa|ab))b|(?:(?:a(?:b|a)|bb)b|baa)a)a|(?:b(?:(?:ba|ab)b|bba)|a(?:bab|aba))b)))b)+"
s8arr = []
for c in s8:
    s8arr.append(c)
ruleMap["8"] = s8arr

curr = ruleMap["0"]
print(curr)

found = True
while found:
    found = False
    nxt = []
    for word in curr:
        if word in ruleMap:
            found = True
            nxt.extend(ruleMap[word])
        else:
            nxt.append(word)
    curr = nxt

rstring = "^" + "".join(curr) + "$"

print(rstring)

res = 0
for s in collect[1]:
    searchResult = re.search(rstring, s)
    if searchResult != None:
        res += 1
print(res)