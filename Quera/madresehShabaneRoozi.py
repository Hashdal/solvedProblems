def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
n = int(input())
fr = []
for i in range(n):
    fr.append(int(input()))
res = 1
for i in range(n):
    res = lcm(res, fr[i])
res += 1
print(res%30)