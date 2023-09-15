print("Rango de Números Primos")

while True:   
    def primo(x):
        print('1 primo')
        for i in range(2,x+1):
            conta = 0
            for n in range(2, x):
                residue = i%n
                if residue == 0:
                    conta = conta + 1
            if conta == 1:
                        print(f'{i} primo')
            else:
                        print(f'{i} no primo')
        return "Rango completo"
    x=int(input('Ingrese el límite del rango: '))
    print(primo(x))
    y=int(input("Desea Terminar el proceso? Digite 1 para confirmar: "))
    if y==1:
        break
