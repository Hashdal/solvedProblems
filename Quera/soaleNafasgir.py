n = int(input())
q = input().split(" ")
a = input().split(" ")
res = 0
for i in range(n):
    res += int(q[i]) * int(a[i])
print(res)