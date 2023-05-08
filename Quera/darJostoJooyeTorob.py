a = int(input())
b = int(input())
c = int(input())
d = int(input())
if b == d:
    print("WAIT WAIT")
elif b * d > 0:
    if b < 0:
        if b < d and a > c:
            print("SEE YOU")
        elif b < d and a < c:
            print("BORO BORO")
        elif b > d and a > c:
            print("BORO BORO")
        elif b > d and a < c:
            print("SEE YOU")
    elif b > 0:
        if b > d and a < c:
            print("SEE YOU")
        elif b > d and a > c:
            print("BORO BORO")
        elif b < d and a < c:
            print("BORO BORO")
        elif b < d and a > c:
            print("SEE YOU")
elif b * d < 0:
    if b < 0 and a > c:
        print("SEE YOU")
    elif b < 0 and a < c:
        print("BORO BORO")
    elif d < 0 and a > c:
        print("BORO BORO")
    else:
        print("SEE YOU")
elif b * d == 0:
    if b == 0 and d > 0:
        if c < a:
            print("SEE YOU")
        else:
            print("BORO BORO")
    elif b == 0 and d < 0:
        if c < a:
            print("BORO BORO")
        else:
            print("SEE YOU")
    elif d == 0 and b > 0:
        if a > c:
            print("BORO BORO")
        else:
            print("SEE YOU")
    elif d == 0 and b < 0:
        if a > c:
            print("SEE YOU")
        else:
            print("BORO BORO")
