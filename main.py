import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    x = -c / b
    print(" x = ", x)
else:
    discrminant = b ** 2 - 4 * a * c
    print("D = ", discrminant)
    if discrminant > 0:
        x1 = (-b + math.sqrt(discrminant)) / ( 2 * a)
        x2 = (-b - math.sqrt(discrminant)) / (2 * a)
        print ("x1 =", x1, "; ", "x2 =", x2)
    elif discrminant == 0:
        x = -b / (2* a)
        print ("x =", x )
    else:
        print("Коренів немає")
