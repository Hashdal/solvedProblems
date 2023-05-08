n = int(input())
s = input()
a = ""
k = int(input())
q = []
for i in range(n):
    if s[i] == "A":
        a += "0"
    elif s[i] == "B":
        a += "1"
    elif s[i] == "C":
        a += "2"
    else:
        a += "3"

for i in range(k):
    subq = []
    for j in range(n):
        subq.append(input())
    q.append(subq)
for i in range(k):
    true = 0
    false = 0
    clear = 0
    for j in range(n):
        res = []
        checka = 0
        for z in range(4):
            if q[i][j][z] == "#":
                res.append(1)
                checka += 1
            else:
                res.append(0)
        if checka == 0:
            clear += 1
        elif checka == 1:
            if res.index(1) == int(a[j]):
                true += 1
            else:
                false += 1
        else:
            false += 1
    print(true*3 - false)