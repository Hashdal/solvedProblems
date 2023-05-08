n = int(input())
input = input()
check = "YES"
for i in range(n):
    if input[i] == input[i+n]:
        check = "NO"
print(check)
