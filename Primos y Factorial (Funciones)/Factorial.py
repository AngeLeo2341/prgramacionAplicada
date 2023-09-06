while True:
    def fact(x):
        if x==1:
            return 1
        else:
            return x * fact(x-1)
    x=int(input('Digite el límite del rango: '))
    print(fact(x))
    y=int(input("Desea Terminar el proceso? Digite 1 para confirmar: "))
    if y==1:
        break
