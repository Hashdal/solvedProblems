n = int(input())
k = int(input())
input = input()
for i in range(k):
    changed = ""
    output = ""
    changed += input[len(input)-1] + input[0:len(input)-1]
    for j in range(len(changed)):
        if changed[j] == "z":
            output += "a"
        else:
            output += chr(ord(changed[j])+1)
    input = output
print(output)