f = open("d18.txt", "r")

arr = []

line = f.readline()
while line:
    line = line.strip()

    # ADD LOGIC HERE

    arr.append(line)

    # END LINE READING

    line = f.readline()

f.close()

results = []

def compress(stack):
    res = 1
    for i in stack:
        res *= i
    return res
    
def evalExp(tempArr, ind):
    res = 0
    opStack = []
    stack = []
    i = ind
    while i < len(tempArr):
        val = tempArr[i]
        if val == ")":
            return (compress(stack), i + 1)
        elif val == "(":
            nestedVal, nxt = evalExp(tempArr, i + 1)
            stack.append(nestedVal)
            i = nxt
        elif val == "+" or val == "*":
            opStack.append(val)
            i += 1
            continue
        else:
            stack.append(val)
            i += 1
        
        if len(opStack) and opStack[-1] == "+":
            op = opStack.pop()
            a, b = stack.pop(), stack.pop()
            stack.append(a + b)

    return (compress(stack), i)

for line in arr:
    toAdd = []
    for c in line:
        if c == " ":
            continue
        if c >= "0" and c <= "9":
            toAdd.append(int(c) )
        else:
            toAdd.append(c)
    curr = evalExp(toAdd, 0)[0]
    results.append(curr)

print(sum(results))

