a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())
sum = 0
if a1 >= b1:
    sum += b1
else:
    sum += a1
if a2 >= b2:
    sum += b2
else:
    sum += a2
if a3 >= b3:
    sum += b3
else:
    sum += a3
print(sum)