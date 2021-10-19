import itertools

def LCM(x, y):
    if x > y:
       greater = x
    else:
       greater = y

    for i in itertools.count(start=1):
       if ((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater+=1
    return lcm


def GCD(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

while True:
    print("Choose one")
    print("1-LCM/Least common Multiple")
    print("2-GCD/Greatest common divisor")
    user_input= int(input())
    if user_input==1:
        x,y = map(int, input("Enter the two numbers you wanna compute LCM").split())
        results=LCM(x,y)
        print("LCM of",x,"and",y,"is",results)
        break
    elif user_input==2:
        x, y = map(int, input("Enter the two numbers you wanna compute GCD").split())
        results2 = GCD(x, y)
        print("LCM of", x, "and", y, "is", results2)
        break
    else:
        print("invalid input try again")


