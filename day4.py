f = open("d4.txt", "r")

res = 0

arr = [{}]

line = f.readline()
while line:
    # TODO: do whatever you want to line

    curr = line.strip()

    if not curr:
        arr.append({})
    else:
        temparr = curr.split(" ")
        for kv in temparr:
            key, value = kv.split(":")
            arr[-1][key] = value

    line = f.readline()

f.close()

for obj in arr:
    contain = True
    for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if k not in obj:
            contain = False
            break
    if contain:
        val = obj["byr"]
        if len(val) != 4:
            continue
        val = int(val)
        if val < 1920 or val > 2002:
            continue

        val = obj["iyr"]
        if len(val) != 4:
            continue
        val = int(val)
        if val < 2010 or val > 2020:
            continue

        val = obj["eyr"]
        if len(val) != 4:
            continue
        val = int(val)
        if val < 2020 or val > 2030:
            continue

        val = obj["hgt"]
        if len(val) < 3:
            continue
        unit = val[len(val)-2:len(val)]
        height = int( val[:len(val) - 2] )
        if unit == "cm":
            if height < 150 or height > 193:
                continue
        elif unit == "in":
            if height < 59 or height > 76:
                continue
        else:
            continue

        val = obj["hcl"]
        if len(val) != 7:
            continue
        if val[0] != "#":
            continue
        for c in val:
            if c not in "0123456789abcdef":
                continue

        val = obj["ecl"]
        if val not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue

        val = obj["pid"]
        if len(val) != 9:
            continue
        for c in val:
            if c not in "0123456789":
                continue

        res += 1

print(res)
