# ---------------------------------------------------------
# SISTEMA DE OPTIMIZACIÓN DE RUTAS EN ENVÍOS - VERSIÓN FINAL
# Implementación con Grafos
# Integrantes del grupo:
# - Juan David Ortiz Ochoa (2242038)
# - Juan Esteban Gomez Ayala (2243465)
# - Ángel Sierra (2242007)
# Profesora: Nury Farelo
# Fecha: 17/11/2025
# ---------------------------------------------------------

import heapq

class GrafoRutas:
    #Constructor
    def __init__(self):
        self.grafo = {}

    def esta_vacia(self):
        return len(self.grafo) == 0

    def contar_ubicaciones(self):
        return len(self.grafo)

    def mostrar_red(self):
        if self.esta_vacia():
            print("La red de rutas está vacía.")
            return

        print("\n--- Red de Rutas (Grafo) ---")
        for origen, rutas in self.grafo.items():
            print(f"Ubicación: {origen}")
            if rutas:
                for destino, distancia in rutas:
                    print(f"  → {destino} ({distancia} Km)")
            else:
                print("  (Sin conexiones)")
            print()
        print("-------------------------------\n")

    def agregar_ubicacion(self, nombre):
        if nombre in self.grafo:
            print(f"La ubicación '{nombre}' ya existe.")
        else:
            self.grafo[nombre] = []
            print(f"Ubicación '{nombre}' agregada.")

    def agregar_ruta(self, origen, destino, distancia):
        if origen not in self.grafo:
            print(f"No existe la ubicación de origen '{origen}'.")
            return
        if destino not in self.grafo:
            print(f"No existe la ubicación de destino '{destino}'.")
            return
        
        self.grafo[origen].append((destino, distancia))
        print(f"Ruta agregada: {origen} → {destino} ({distancia} Km)")

    def buscar_ubicacion(self, nombre):
        if nombre in self.grafo:
            print(f"Ubicación encontrada: {nombre}")
            print("Conexiones:")
            for destino, distancia in self.grafo[nombre]:
                print(f"  → {destino} ({distancia} Km)")
        else:
            print("Ubicación no encontrada.")

    def ordenar_ubicaciones(self):
        print("\nUbicaciones ordenadas alfabéticamente:")
        for nombre in sorted(self.grafo.keys()):
            print(f" - {nombre}")
        print()

    def ruta_mas_corta(self, origen, destino):
        if origen not in self.grafo or destino not in self.grafo:
            print("Una o ambas ubicaciones no existen.")
            return

        dist = {n: float("inf") for n in self.grafo}
        dist[origen] = 0

        prev = {}
        pq = [(0, origen)]

        while pq:
            distancia_actual, nodo = heapq.heappop(pq)

            if distancia_actual > dist[nodo]:
                continue

            for vecino, peso in self.grafo[nodo]:
                nueva_dist = distancia_actual + peso
                if nueva_dist < dist[vecino]:
                    dist[vecino] = nueva_dist
                    prev[vecino] = nodo
                    heapq.heappush(pq, (nueva_dist, vecino))

        if dist[destino] == float("inf"):
            print("No existe ruta disponible entre las ubicaciones.")
            return

        camino = []
        actual = destino
        while actual in prev:
            camino.append(actual)
            actual = prev[actual]
        camino.append(origen)
        camino.reverse()

        print("\nRuta más corta encontrada:")
        print(" → ".join(camino))
        print(f"Distancia total: {dist[destino]} Km\n")


# ---------------------------------------------------------
# MENÚ DEL USUARIO
# ---------------------------------------------------------

def menu():
    red = GrafoRutas()

    while True:
        print("""\
--- Sistema de Rutas de Envío (Versión Final - Grafos) ---
1. Agregar ubicación
2. Agregar ruta entre ubicaciones
3. Mostrar red de rutas
4. Verificar si la red está vacía
5. Contar ubicaciones
6. Buscar ubicación
7. Mostrar ubicaciones ordenadas
8. Calcular ruta más corta
9. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la nueva ubicación: ")
            red.agregar_ubicacion(nombre)

        elif opcion == "2":
            origen = input("Origen: ")
            destino = input("Destino: ")
            try:
                distancia = float(input("Distancia (Km): "))
            except:
                print("Distancia inválida.")
                continue
            red.agregar_ruta(origen, destino, distancia)

        elif opcion == "3":
            red.mostrar_red()

        elif opcion == "4":
            print("La red está vacía." if red.esta_vacia() else "La red contiene ubicaciones.")

        elif opcion == "5":
            print(f"Cantidad de ubicaciones: {red.contar_ubicaciones()}")

        elif opcion == "6":
            nombre = input("Nombre de la ubicación: ")
            red.buscar_ubicacion(nombre)

        elif opcion == "7":
            red.ordenar_ubicaciones()

        elif opcion == "8":
            origen = input("Origen: ")
            destino = input("Destino: ")
            red.ruta_mas_corta(origen, destino)

        elif opcion == "9":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.\n")


if __name__ == "__main__":
    menu()
