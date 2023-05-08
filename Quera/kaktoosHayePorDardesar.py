n = int(input())
arr = input().split(" ")
for i in range(len(arr)):
    if int(arr[i]) > 3:
        print("*")
    else:
        output = ""
        for j in range(int(arr[i])):
            output += "*"
        print(output)