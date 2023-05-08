input = input()
changed = ""
all = []
for i in range(len(input)):
    changed = input[len(input)-1] + input[0:len(input)-1]
    input = changed
    all.append(changed)
all.sort()
print(all[len(all)-1])
print(all[len(all)-2])
print(all[0])
print(all[1])