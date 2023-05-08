k = int(input())
password = input()
arr = []
output = 0
for i in range(k):
    arr.append(input())
for i in range(k):
    if arr[i].index(password[i]) <= 4:
        output += arr[i].index(password[i])
    else:
        output -= arr[i].index(password[i]) - 9
print(output)