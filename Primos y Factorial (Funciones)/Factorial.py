while True:
    x = int(input('Inserte su número factorial: '))
    y = 1
    for i in range(1, x+1):
       y*= i
    print(x)
    print("El Factorial es: ")
    print(y)
    z=int(input("¿Desea continuar con el programa? Digite 1 para confirmar: " ))
    if z != 1:
        break
