inf = []
while(True):
    inp = input()
    if inp == ".":
        break
    else:
        inf.append(inp.split("-"))
outInf = []
while(True):
    inp = input()
    if inp == ".":
        break
    else:
        outInf.append(inp)
print("Saved information")
found = False
for i in range(len(outInf)):
    found = False
    for j in range(len(inf)):
        if outInf[i] == inf[j][0]:
            print(inf[j][1])
            found = True
        elif outInf[i] == inf[j][1]:
            print(inf[j][0])
            found = True
    if not found:
        print("NOT FOUND")
print("End")