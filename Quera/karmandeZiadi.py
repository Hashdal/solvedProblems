n = int(input())
nums = []
names = []
for i in range (n):
    names.append(input().split(" ")[0])
names.sort()
counter = 0
for i in range(n):
    if i == n-1:
        nums.append(counter+1)
    else:
        if names[i] != names[i+1]:
            nums.append(counter+1)
            counter = 0
        else:
            counter += 1
nums.sort()
print(nums[len(nums)-1])