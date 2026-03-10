import heapq

# Max de peliculas

def max_peliculas(peliculas):

    peliculas_ordenadas = sorted(peliculas, key = lambda x: x[1])
    seleccionadas = []
    fin_actual = 0

    for inicio, fin in peliculas_ordenadas:
        if inicio >= fin_actual:
            seleccionadas.append((inicio, fin))
            fin_actual = fin
    
    return seleccionadas

print("\n1. MÁXIMO REUNIONES")
peliculas = [(13,15),(14,16),(15,17),(16,18),(17,19)]
print(f"   Reuniones: {peliculas}")
print(f"   Seleccionadas: {max_peliculas(peliculas)}")


#2 Camion con cajas, pero no se pueden repartir cajas

def cargar_camion(capacidad, cajas):

    cajas_seleccionadas = [(p, v, i) for i,(p,v) in enumerate(cajas)]
    cajas_seleccionadas.sort(key = lambda x: x[1], reverse = True)

    valor_total = 0
    seleccionadas = []

    for peso, valor, idx in cajas_seleccionadas:
        if peso <= capacidad:
            seleccionadas.append((peso, valor))
            valor_total += valor
            capacidad -= peso
    
    return valor_total, seleccionadas

print("\n2. LLENAR CAMIÓN")

cajas = [(10,60),(20,100),(30,120)]
valor, selec = cargar_camion(50, cajas)

print(f"   Cajas (peso, valor): {cajas}")
print(f"   Capacidad: 50")
print(f"   Valor obtenido: {valor}, Cajas: {selec}")

# 4 Asignar tareas a servidores

def asignar_tareas(tareas, num_servidores):
    if not tareas:
        return 0, [[] for _ in range(num_servidores)]
    tareas_ordenadas = sorted(enumerate(tareas), key = lambda x: -x[1])

    servidores = [(0, i, [] ) for i in range(num_servidores)]
    heapq.heapify(servidores)

    for idx_original, tiempo in tareas_ordenadas:
        carga, id_servidor, lista = heapq.heappop(servidores)
        lista.append(tiempo)
        heapq.heappush(servidores, (carga + tiempo, id_servidor, lista))
    
    tiempo_total = max(s[0] for s in servidores)
    asignacion = [s[2] for s in sorted(servidores, key = lambda x: x[1])]

    return tiempo_total, asignacion
    
    
# Reto 4
print("\n4. ASIGNAR TAREAS")
tiempo, asig = asignar_tareas([2, 14, 4, 16, 6, 5], 3)
print(f"   Tareas: [2, 14, 4, 16, 6, 5], Servidores: 3")
print(f"   Tiempo total: {tiempo}")
print(f"   Asignación: {asig}")