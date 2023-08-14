#tabla de multiplicación de un valor ingresado por el usuario
numero = int(input("Ingrese un número entero:\t"))
for x in range(1,11):
    print(x , " X ", numero, " = ", x*numero)
