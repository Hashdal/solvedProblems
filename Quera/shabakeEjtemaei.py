people = {}
foundCounter = 1
def find(letters):
    output = []
    for i in people:
        if i == letters:
            return i
        elif i[:len(letters)] == letters:
            output.append(i)
    if output == []:
        return False
    else:
        return output
while(True):
    command = input().split(" ")
    if command[0] == "exit":
        break
    elif command[0] == "Add":
        people[command[4]] = command[1:]
        print("User {} added successfully".format(command[4]))
    elif command[0] == "Find":
        found = find(command[1])
        if found == False:
            print(str(foundCounter) + " No user found")
            foundCounter += 1
        elif type(found) == str:
            output = str(foundCounter)
            for i in people[found]:
                output += " " + str(i)
            print(output)
            foundCounter += 1
        else:
            found.sort()
            if len(found) > 10:
                found = found[:10]
            for i in found:
                output = str(foundCounter)
                for j in people[i]:
                    output += " " + str(j)
                print(output)
            foundCounter += 1