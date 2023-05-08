a = int(input())
b = int(input())
def run(a, b):
    difOut = int((a - b) / 2)
    starLine = "*"
    for i in range(a-1):
        starLine += " *"
    for i in range(difOut):
        print(starLine)
    starLineTwo = "*"
    for i in range(difOut-1):
        starLineTwo += " *"
    starLineTwo += " "
    for i in range(b):
        starLineTwo += "  "
    starLineTwo += "*"
    for i in range(difOut-1):
        starLineTwo += " *"
    for i in range(b):
        print(starLineTwo)
    for i in range(difOut):
        print(starLine)
if b >= a:
    print("Wrong order!")
elif (a - b) % 2 != 0:
    print("Wrong difference!")
else:
    run(a, b)