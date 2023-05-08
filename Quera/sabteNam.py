n = int(input())
users = {}
for i in range(n):
    user = input().split(" ")
    name = user[0]
    name = name.lower()
    if name.find("user") != -1 or name.find("admin") != -1:
        continue
    if len(user[0]) < 4:
        continue
    if len(user[1]) < 6 or user[1].isdigit():
        continue
    if user[2][:2] != "09" or not user[2].isdigit() or len(user[2]) != 11:
        continue
    users[user[0]] = user
signedUpUsers = []
for i in users:
    string = ""
    string += users[i][2][9:12]
    string += i
    signedUpUsers.append(string)
signedUpUsers.sort()
for i in range(len(signedUpUsers)):
    print(signedUpUsers[i][2:], end=" ")