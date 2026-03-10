
# RETO 1: Máximo número de reuniones
# ─────────────────────────────────────────────────────────────────────────────
# Eres un gerente y tienes varias reuniones propuestas para hoy.
# Cada reunión tiene una hora de inicio y fin.
# Quieres asistir al MÁXIMO número de reuniones posible.

def max_reuniones(reuniones):

    reuniones_ordenadas = sorted(reuniones, key = lambda x: x[1])
    seleccionadas = []
    fin_actual = 0

    for inicio, fin in reuniones_ordenadas:
        if inicio >= fin_actual:
            seleccionadas.append((inicio, fin))
            fin_actual = fin
    return seleccionadas

print("\n1. MÁXIMO REUNIONES")
reuniones = [(9, 10), (9, 12), (10, 11), (11, 13), (12, 14)]
print(f"   Reuniones: {reuniones}")
print(f"   Seleccionadas: {max_reuniones(reuniones)}")
    

# RETO 2: Llenar camión con cajas
# ─────────────────────────────────────────────────────────────────────────────
# Tienes un camión con capacidad máxima de peso.
# Hay varias cajas, cada una con un peso y un valor.
# NO puedes partir las cajas (a diferencia de la mochila fraccionaria).
# Maximiza el valor total que puedes cargar.


def llenar_camion(capacidad, cajas):
    
    cajas_con_ratio = [(p, v, v/p, i) for i, (p,v) in enumerate(cajas)]
    cajas_con_ratio.sort(key = lambda x: x[2], reverse = True)

    valor_total = 0
    seleccionadas = []

    for peso, valor, ratio, idx in cajas_con_ratio:
        if peso <= capacidad:
            seleccionadas.append((peso, valor))
            valor_total += valor
            capacidad -= peso
    
    return valor_total, seleccionadas

print("\n2. LLENAR CAMIÓN")
cajas = [(5, 10), (4, 40), (6, 30), (3, 50)]
valor, selec = llenar_camion(10, cajas)
print(f"   Cajas (peso, valor): {cajas}")
print(f"   Capacidad: 10")
print(f"   Valor obtenido: {valor}, Cajas: {selec}")

# SOLUCIÓN RETO 3: Estaciones de gasolina
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Ir lo más lejos posible antes de parar. Cuando ya no puedas
# llegar a la siguiente estación, para en la última que podías alcanzar.
#
# Complejidad Temporal: O(n) recorrido lineal de estaciones
# Complejidad Espacial: O(n) para almacenar paradas
# ¿Greedy es óptimo? SÍ

def solucion_min_paradas(distancia_total, capacidad, estaciones):
    estaciones = [0] + sorted(estaciones) + [distancia_total]
    paradas = []
    combustible = capacidad

    for i in range(1, len(estaciones)):
        distancia = estaciones[i] - estaciones[i-1]

        if distancia > capacidad:
            return -1 #Imposible
        
        if distancia > combustible: #Parar en la anterior
            paradas.append(estaciones[i-1])
            combustible = capacidad
        
        combustible -= distancia
    
    return paradas

# Reto 3
print("\n3. ESTACIONES DE GASOLINA")
paradas = solucion_min_paradas(25, 10, [5, 8, 15, 22])
print(f"   Distancia: 25, Tanque: 10km, Estaciones: [5, 8, 15, 22]")
print(f"   Paradas necesarias: {paradas}")

# SOLUCIÓN RETO 4: Asignar tareas a servidores
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Ordenar tareas de mayor a menor. Asignar cada tarea al
# servidor menos cargado (usando un heap).
#
# Complejidad Temporal: O(n log n + n log m) donde n=tareas, m=servidores
#   - O(n log n) para ordenar tareas
#   - O(n log m) para n inserciones en heap de m servidores
# Complejidad Espacial: O(m) para el heap de servidores
# ¿Greedy es óptimo? NO siempre, pero da buena aproximación.


