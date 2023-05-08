n = int(input())
strings = []
commonSubs = []
for i in range(n):
    strings.append(input())
for i in range(len(strings[0])):
    j = len(strings[0]) - 1
    while j > i:
        check = True
        for z in range(n):
        
            if strings[z].find(strings[0][i:j+1]) == -1 and strings[z].find(strings[0][i:j+1][::-1]) == -1:

                check = False
                break

        if check:
            commonSubs.append(strings[0][i:j+1])
        j -=  1
print(commonSubs)