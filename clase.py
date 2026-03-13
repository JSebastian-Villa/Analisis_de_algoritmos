# Posibles soluciones de los exámenes

#Examen A

pedidos = [("Pedido A", 4, 6), ("Pedido B", 2, 4), ("Pedido C", 3, 8), ("Pedido D", 1, 2)]

def despacho_pedido(pedidos):

    pedidos_ordenados = sorted(pedidos, key = lambda x: x[2])
    orden = []
    multas = 0
    tiempo = 0

    for nombre, inicio, fin in pedidos_ordenados:
        tiempo += inicio
        retraso = max(9, inicio - fin)
        multas += retraso 
        orden.append(nombre)
    
    return orden, multas

#Examen B 

conductores = [1, 5, 8]
solicitudes = [2, 6, 9]

def asignar(conductores, solicitudes):
    
    conductores_ordenados = sorted(conductores)
    solicitudes_ordenadas = sorted(solicitudes)

    asignaciones = 0
    distancia_total = 0

    for i in range(len(conductores_ordenados)):
        distancia = abs(solicitudes_ordenadas[i]- conductores_ordenados[i])
        asignaciones.append(distancia, conductores_ordenados[i], solicitudes_ordenadas[i])
        distancia_total += distancia
    
    return asignaciones, distancia_total

