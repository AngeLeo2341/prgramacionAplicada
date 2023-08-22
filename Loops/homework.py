while True:

    print("Por favor digite un numero")
    a = input(" ")
    a = int(a)
    print("Por favor digite otro numero")
    b = input(" ")
    b = float(b)
    c = a+b
    print(c)

    if a == b:
        print("equal")
    else:
        print("Different")

    print("Type of a is: ", type(a))
    print("Type of b is: ", type(b))
    print("c = ", type(c))

    if type(a) == type(b):
        print("a and b are of the same type")
    else:
        print("a and b are of different type")