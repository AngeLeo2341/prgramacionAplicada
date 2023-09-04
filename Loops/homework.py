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

    print("a es de tipo: ", type(a))
    print("a es de tipo: ", type(b))
    print("c = ", type(c))

    if type(a) == type(b):
        print("a y b son del mismo tipo")
    else:
        print("a y b no son del mismo tipo")
