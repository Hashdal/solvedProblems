n = int(input())
arr = input().split(" ")
sum = 0
maxIndex = 0
for i in range(len(arr)):
    arr[i] = int(arr[i])
for i in range(len(arr)):
    maxLeft = 0
    maxRight = 0
    j = i
    if i == 0:
        continue
    while j >= 1:
        if j == 1:
            if arr[j-1] > maxLeft and arr[j-1] > arr[i]:
                maxLeft = arr[j-1]
                j -= 1
            else:
                j -= 1
                continue
        elif arr[j-1] > arr[j] and arr[j-1] >= arr[j-2] and arr[j-1] > maxLeft and arr[j-1] > arr[i]:
            maxLeft = arr[j-1]
            j -= 1
        else:
            j -= 1
    j = i
    while j < len(arr) - 1:
        if j == len(arr) - 2:
            if arr[j+1] > maxRight and arr[j+1] > arr[i]:
                maxRight = arr[j+1]
                j += 1
            else:
                j += 1
        else:
            if arr[j+1] > arr[j] and arr[j+1] > arr[j+2] and arr[j+1] > maxRight and arr[j+1] > arr[i]:
                    maxRight = arr[j+1]
                    j += 1
            else:
                 j += 1
    if maxLeft > maxRight and maxLeft != 0 and maxRight != 0:
        sum += maxRight - arr[i]
    elif maxLeft != 0 and maxRight != 0:
        sum += maxLeft - arr[i]
print(sum)