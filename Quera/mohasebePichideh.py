input = input().split(" ")
a = int(input[0])
x = int(input[1])
n = int(input[2])
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def c(s, t):
    return int(factorial(s) / (factorial(s-t) * factorial(t)))
sum = 0
for k in range(n+1):
    sum += c(n, k) * pow(x, k) * pow(a, n-k)
print(sum)