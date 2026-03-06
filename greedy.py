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

"""
"""
# Clase 6/03/2026

def mochila_fraccionaria(capacidad, objetos):
    objetos_con_ratio = [(p, v, p/v) for p, v in objetos]
    objetos_con_ratio.sort(key= lambda x: x[2], reverse=True)

    valor_total = 0
    objetos_almacenados = []

    for peso, valor, ratio in objetos_con_ratio:
        if capacidad >= peso:
            valor_total += valor
            capacidad -= peso
            objetos_almacenados.append((peso, valor, 1))
        elif capacidad > 0:
            fraccion = capacidad / peso
            valor_total += valor * fraccion
            objetos_almacenados.append((peso, valor, fraccion))
            break
    
    return objetos_almacenados, valor_total


peso = [20, 40]
valor = [10, 30]
capacidad = 100

objetos = list(zip(peso, valor))

resultado, valor_total = mochila_fraccionaria(capacidad, objetos)

print("Objetos almacenados:", resultado)
print("Valor total:", valor_total)

"""

distancia_total = 50
estaciones = [0, 15, 20, 40, 50]

def minimo_paradas(distancia_total, capacidad, estaciones):
    estaciones = [0] + sorted(estaciones) + [distancia_total]
    paradas = []
    combustible = capacidad 

    for i in range(1, len(estaciones)):

        distancia = estaciones[i] - estaciones[i-1]
        if distancia > capacidad:
            return -1
        
        if distancia > combustible:
            paradas.append(estaciones[i-1])
            combustible = capacidad

        combustible -= distancia
    
    return paradas

#Asignar tareas a servidores

servidores = 3
tareas = [10, 30, 20]

import heapq

def asignar_tareas(tareas, num_servidores):
    tareas_ordenadas = sorted(enumerate(tareas), key = lambda x: x[1])
    servidores = [ (0, i, []) for i in range(num_servidores)]
    heapq.heapify(servidores)

    for id, tiempo in tareas_ordenadas:
        carga, id_servidor,lista = heapq.heappop(servidores)
        lista.append(tiempo)
        heapq.heappush(servidores, (carga + tiempo, id_servidor, lista))