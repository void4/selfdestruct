f = open("invader.asm")
lines = f.readlines()
f.close()

labels = {}
varindex = 400
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
"""
2:MOV OP1 <- OP2
3:ADD OP1 <- OP2 + OP3
5:JUMPI (OP1) -> OP2
7:JUMP -> OP1
11:SUB OP1 <- OP2 - OP3
13:SET OP1 <- [OP2]
"""
index = 0
code = [4, 0, 0, 0]
for line in lines:
    line = line.strip().lower()
    if not line:
        continue
    if line.endswith(":"):
        labels[line[:-1]] = index
        continue
    print(line)
    line = line.split(" ")
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
    elif op == "jumpi":
        code += [5, intorvar(op1), intorlabel(op2)]
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
    else:
        print("AHSAH)DA)HFE UNKNOWN OPCODE1111")
        exit(1)

    code += [0 for i in range((4-len(code)%4)%4)]

    index += 1

print(code)
if len(code) > varindex:
    print(len(code) + "> varindex:", varindex, "aborting!")
    exit(1)

bfile = open("bytecode.js", "w+")
bfile.write("var code = "+str(code))
bfile.close()
