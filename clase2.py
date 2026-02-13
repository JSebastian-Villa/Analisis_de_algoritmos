#Ejercicio 1

#Propuesta mia
"""
def clave_candado(contraseña: str, intento: str):
    if len(contraseña) != len(intento):
        return "Las contraseñas no coinciden"

    for i in range(len(contraseña)):
        if contraseña[i] != intento[i]:
            return "Las contraseñas no coinciden"
    return "Las contraseñas coinciden"



contraseña = input("Ingrese la contraseña: ")
intento = input("Ingrese el intento: ")
print(clave_candado(contraseña, intento))
"""
#=======================================================================

#Ejercicio 1 - Propuesta del profesor
""""

clave = input("Ingrese la clave del candado: ")

intentos = 0

for i in range (0, 1000):
    clave_generada = str(i).zfill(3) # Genera un número de 3 dígitos con ceros a la izquierda
    intentos += 1
    
    if clave == clave_generada:
        print("La encontré")
        print("La clave es ", clave_generada)
        print("El numero de intentos fue: ", intentos)
        break

print("La clave tiene mas de 3 dígitos")

"""
#========================================================================

#Ejercicio 2 - El mismo pero con N dígitos (profesor, sin optimizar)
"""
clave = input("Ingrese la clave: ")
n = len(clave)

intentos = 0

for i in range(0, 10**n):
    clave_generada = str(i).zfill(n)
    intentos += 1

    if clave == clave_generada:
        print("La encontré")
        print("La clave es ", clave_generada)
        print("El numero de intentos fue: ", intentos)
        break
"""
#Ejercicio 2 - El mismo pero optimizado (lucho)

"""
clave = input("Ingrese la clave: ")
n = len(clave)

intentos = 0
prefijo = ""

for posicion in range(n):
    for digito in range(10):
        intentos += 1

        if str(digito) == clave[posicion]:
            prefijo += str(digito)
            break

print(f"Clave encontrada: {prefijo}")
print(f"Intentos realizados: {intentos}")

"""

#Ejercicio 2 - por busqueda binaria

"""

clave = input("Ingrese la clave: ")
n = len(clave)

intentos = 0
prefijo = ""

for posicion in range(n):
    minimo = 0
    maximo = 9

    objetivo = int(clave[posicion])

    while minimo <= maximo:
        medio = (minimo + maximo) // 2
        intentos += 1
        if medio == objetivo:
            prefijo += str(medio)
            break
        elif medio < objetivo:
            minimo = medio + 1
        else:
            maximo = medio - 1

print(f"Clave encontrada: {prefijo}")
print(f"Intentos realizados: {intentos}")

"""

#Busqueda binaria (profesor)

clave = input("Ingrese la clave: ")

longitud = len(clave)

menor = 0
mayor = (10**longitud) - 1

intentos = 0

while menor <= mayor:
    intentos += 1

    mitad = (menor + mayor) // 2

    if (mitad) == int(clave):
        print("La encontré")
        print(f"Número de intentos: {intentos}")
        break 
    elif mitad < int(clave):
        menor = mitad + 1
    else:
        mayor = mitad - 1