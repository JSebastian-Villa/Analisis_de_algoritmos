#Leer el elemento es O(1), sacar o insertar o(Log(n))

import heapq
"""
datos = [5, 3, 8, 1, 2, 9, 4]

heapq.heapify(datos) # Garantiza que los padres son menores que sus hijos
print("")
print(datos)
heapq.heappush(datos, 0) #Insertar
print("Push 0 al heap") 
print(datos)
minimo = heapq.heappop(datos)
print("Valor extraido con pop")
print(minimo)
print("Heap despues de pop")

resultado = heapq.heappushpop(datos, 10)
print(resultado)
print(datos)

"""
"""
#Ejercicios heap

#1: 
urgencias = []
orden = 0

def agregar_paciente(nombre, prioridad, orden):
    orden += 1
    heapq.heappush(urgencias, (prioridad, orden, nombre))
    print("Paciente agregado")
    return orden

def atender_paciente():
    if urgencias:
        prioridad, _, nombre = heapq.heappop(urgencias)
        print(f"Paciente atendido es {nombre} con prioridad {prioridad}")
    else:
        print("No hay pacientes en la sala de espera")


orden = agregar_paciente("Jacob", 2, orden)
print(urgencias)
orden = agregar_paciente("Blast", 1, orden)
print(urgencias)
orden = agregar_paciente("Lucho", 2, orden)
print(urgencias)

atender_paciente()
atender_paciente()
atender_paciente()
atender_paciente()

"""

# Ejercicios de Greedy


eventos = [(3,5),(1,4),(5,7),(8,11),(6,10),(0,6)]

def seleccion_eventos(eventos):
    if not eventos:
        return None

    eventos = sorted(eventos, key=lambda x: x[1])   
    seleccionados = []
    fin_ultimo = 0
    
    for inicio, fin in eventos:
        if inicio >= fin_ultimo:
            seleccionados.append((inicio, fin))
            fin_ultimo = fin
    
    return seleccionados


resultado = seleccion_eventos(eventos)

print("Eventos seleccionados:", resultado)
print("Cantidad máxima:", len(resultado))
