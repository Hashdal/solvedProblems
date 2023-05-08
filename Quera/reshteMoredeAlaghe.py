word = input()
n = int(input())
counter = 0
for i in range(n):
    k = []
    counterp = 0
    string = input()
    for i in range(len(word)):
        m = string.find(word[i])
        k.append(m)
        check = False
        for i in range(len(k)):
            if k[i] > m:
                check = True
                break
        if m == -1 or check:
            break
        else:
            string.replace(word[i], "-", 1)
            counterp += 1
    if counterp == len(word):
        counter += 1
print(counter)