def reVal(num):
	if (num >= 0 and num <= 9):
		return chr(num + ord('0'))
	else:
		return chr(num - 10 + ord('A'))

def strev(str):
	len = len(str)
	for i in range(int(len / 2)):
		temp = str[i]
		str[i] = str[len - i - 1]
		str[len - i - 1] = temp

def fromDeci(res, base, inputNum):
	index = 0
	while (inputNum > 0):
		res+= reVal(inputNum % base)
		inputNum = int(inputNum / base)
	res = res[::-1]
	return res

a = input()
b = int(input())
c = int(input())
num = int(a, b)
i = str(fromDeci("", c, num))
j = 0
z = len(i) - 1
check = True
if a == "0":
    print("YES")
else:
    while(j != z and z > j):
        if i[z] != i[j]:
            check = False
            break
        j += 1
        z -= 1
    if check:
        print("YES")
    else:
        print("NO") 