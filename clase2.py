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

#Ejercicio 2 - El mismo pero optimizado