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

arr = [] # this data structure holds the structure of our data

ruleMap = {}

# process rules
for line in collect[0]:
    
    # ADD WHAT YOU WANT TO DO TO EACH LINE HERE

    key, rule = line.split(": ")
    ruleMap[key] = []
    
    # process rule
    if rule.find("|") >= 0:
        ruleA, ruleB = rule.split(" | ")
        for r in [ruleA, ruleB]:
            ruleMap[key].append(r.split(" "))
    elif rule.find(" ") >= 0:
        ruleMap[key].append(rule.split(" "))
    else:
        ruleMap[key].append(rule[1:2])

print(ruleMap)

# return (expandedArr, True if leaf)
def expand(exp):
    rtn = []
    for key in exp:
        if key >= "a" and key <= "z":
            rtn.append(key)
        else:
            # lookup
            ruleVal = ruleMap[key]
            if rule

    return [rtn, isLeaf]

curr = ["0"]
# while True:
#     hasVars = False
#     nxt = []

#     for exp in curr:
#         expandedArr, isLeaf = expandExp(exp)
#         if isLeaf:
#             allPos.append(expandedArr[0])
#         else:
#             hasVars = True
#             nxt.extend(expandedArr)
#     # scan all, if no variables, break
#     if not hasVars:
#         break

    

# list of the rules valid messages should obey
# ist of received messages

# pipe (|). This means that at least one list of sub-rules must match.



# results = []

# def compress(stack):
#     res = 1
#     for i in stack:
#         res *= i
#     return res
    
# def evalExp(tempArr, ind):
#     res = 0
#     opStack = []
#     stack = []
#     i = ind
#     while i < len(tempArr):
#         val = tempArr[i]
#         if val == ")":
#             return (compress(stack), i + 1)
#         elif val == "(":
#             nestedVal, nxt = evalExp(tempArr, i + 1)
#             stack.append(nestedVal)
#             i = nxt
#         elif val == "+" or val == "*":
#             opStack.append(val)
#             i += 1
#             continue
#         else:
#             stack.append(val)
#             i += 1
        
#         if len(opStack) and opStack[-1] == "+":
#             op = opStack.pop()
#             a, b = stack.pop(), stack.pop()
#             stack.append(a + b)

#     return (compress(stack), i)

# for line in arr:
#     toAdd = []
#     for c in line:
#         if c == " ":
#             continue
#         if c >= "0" and c <= "9":
#             toAdd.append(int(c) )
#         else:
#             toAdd.append(c)
#     curr = evalExp(toAdd, 0)[0]
#     results.append(curr)

# print(sum(results))

