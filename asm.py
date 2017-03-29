f = open("invader.asm")
lines = f.readlines()
f.close()

opcodes = ["mul", "seti", "set", "mov", "add", "jumpe", "sub", "jump", "jumpg"]

labels = {}
opcounter = 1

lines = [[line] for line in lines]
for row in lines:
    line = row[0]
    clean = line.strip().lower()
    if ";" in clean:
        clean = clean[:clean.find(";")]

    row.append(clean)

    opline = clean.split(" ")
    row.append(opline)

    if len(opline) == 1 and opline[0].endswith(":"):
        labels[opline[0][:-1]] = opcounter
        ignore = True
    elif opline[0] in opcodes:
        opcounter += 1
        ignore = False
    elif opline[0]:
        raise Exception("Invalid symbol:", opline[0])
    else:
        ignore = True

    row.append(ignore)

#print("Labels", labels)
varindex = opcounter + 1#XXX
var = {}

def addvar(name):
    global varindex
    var[name] = varindex
    varindex += 1

def intorvar(opn, reg=False):
    if opn is None:
        return 0
    try:
        return int(opn)
    except ValueError:
        if reg and not opn in var:
            addvar(opn)
        return var[opn]

def intorlabel(opn):
    try:
        return int(opn) * 4
    except ValueError:
        return labels[opn] * 4

code = [4, 0, 0, 0]
for row in lines:
    #print(row)
    if row[3]:
        continue
    line = row[2]
    op = line[0]
    op1 = line[1]
    op2 = line[2] if len(line)>2 else None
    op3 = line[3] if len(line)>3 else None

    if op == "mov":
        code += [2, intorvar(op1), intorvar(op2)]
    elif op == "add":
        if len(line) == 3:
            code += [3, intorvar(op1), intorvar(op1), intorvar(op2)]
        else:
            code += [3, intorvar(op1), intorvar(op2), intorvar(op3)]
    elif op == "jumpe":
        code += [5, intorvar(op1), intorvar(op2), intorlabel(op3)]
    elif op == "jump":
        code += [7, intorlabel(op1)]
    elif op == "sub":
        if len(line) == 3:
            code += [11, intorvar(op1), intorvar(op1), intorvar(op2)]
        else:
            code += [11, intorvar(op1), intorvar(op2), intorvar(op3)]
    elif op == "set":
        code += [13, intorvar(op1, reg=True), int(op2)]
    elif op == "seti":
        code += [17, intorvar(op1), int(op2)]
    elif op == "mul":
        if len(line) == 3:
            code += [19, intorvar(op1), intorvar(op1), intorvar(op2)]
        else:
            code += [19, intorvar(op1), intorvar(op2), intorvar(op3)]
    elif op == "jumpg":
        code += [23, intorvar(op1), intorvar(op2), intorlabel(op3)]
    elif op == "jumpn":
        code += [29, intorvar(op1), intorvar(op2), intorlabel(op3)]
    else:
        raise Exception("Unknown opcode")

    code += [0 for i in range((4-len(code)%4)%4)]

print(code)

bfile = open("bytecode.js", "w+")
bfile.write("var code = "+str(code))
bfile.close()
