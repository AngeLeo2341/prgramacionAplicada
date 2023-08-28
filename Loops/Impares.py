times = input("Enter a number of times: ")
times = float(times)
times = int(times)
residual = times%2 #Determinar si es Par o Impar dividiendo entre dos
if residual == 0:
    print(f'{times} is even') #Si el residuo es igual a Cero el número es Par
else:
    print(f'{times} is odd') #Si el residuo no es igual a Cero el número es Impar
    print(str(times) + ' is odd')

print(type(times))
    

if times == 0:
    print("Don't do anything")
else:
    for i in range(1,times+1):
        print("i = ", i)