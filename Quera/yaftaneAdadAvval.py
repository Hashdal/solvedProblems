def ifPrime(n):
    counter = 0
    for i in range(1, n):
        if n % i == 0:
            counter += 1
    if counter == 1:
        return True
    else:
        return False
number = input()
sum = 0
for i in range(len(number)):
    sum += int(number[i])
i = 0
number = int(number)
while(i < sum):
    number += 1
    if ifPrime(number):
        i += 1
print(number)
