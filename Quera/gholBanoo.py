s = input()
i = len(s) - 1 
revs = ""
while i >= 0:
    revs += s[i]
    i -= 1
print(revs)