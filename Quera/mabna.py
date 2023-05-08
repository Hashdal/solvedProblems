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
input = input().split(" ")
a = int(input[0])
b = int(input[1])
res = ""
number = fromDeci(res, b, a)
number = str(number)
sum1 = 0
sum2 = 0
for i in range(0, len(number), 2):
    sum1 += int(number[i])
for i in range(1, len(number), 2):
    sum2 += int(number[i])
if sum1 == sum2:
    print("Yes")
else:
    print("No")