nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])
matrix = []
for i in range(n):
    matrix.append(input().split(" "))
sum = 0
for i in range(n):
    for j in range(m):
        sum += float(matrix[i][j])
print(round(sum/n, 5))
print(round(sum/m, 5))
print(round(sum/(m*n), 5))