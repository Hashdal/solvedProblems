inputs = input().split(" ")
n = int(inputs[0])
p = int(inputs[1])
q = int(inputs[2])
words = []
myset = set()
for i in range(n):
    words.append(input())
for i in range(len(words)):
    qs = words[i][-q:]
    ps = words[i][:p]
    myset.add((qs,ps))
print(len(myset))