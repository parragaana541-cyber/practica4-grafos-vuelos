import time

class GrafoVuelos:
    def __init__(self):
        self.grafo = {}

    def agregar_vuelo(self, origen, destino, costo):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append({"destino": destino, "costo": costo})

    def mostrar_reporte(self):
        print("--- REPORTE DE LA RED DE VUELOS ---")
        for origen, destinos in self.grafo.items():
            for v in destinos:
                print(f"Origen: {origen} ---> Destino: {v['destino']} | Costo: ${v['costo']}")
        print("-----------------------------------")

    def buscar_vuelo_mas_barato(self, actual, destino, costo_actual, visitados, ruta_actual, mejor_ruta):
        visitados.add(actual)
        ruta_actual.append(actual)

        if actual == destino:
            if costo_actual < mejor_ruta["costo"]:
                mejor_ruta["costo"] = costo_actual
                mejor_ruta["ruta"] = list(ruta_actual)
        else:
            for v in self.grafo.get(actual, []):
                if v["destino"] not in visitados:
                    if costo_actual + v["costo"] < mejor_ruta["costo"]:
                        self.buscar_vuelo_mas_barato(v["destino"], destino, costo_actual + v["costo"], visitados, ruta_actual, mejor_ruta)

        ruta_actual.pop()
        visitados.remove(actual)

# Inicialización y simulación de base de datos
g = GrafoVuelos()
g.agregar_vuelo("Quito", "Guayaquil", 50)
g.agregar_vuelo("Quito", "Cuenca", 60)
g.agregar_vuelo("Guayaquil", "Cuenca", 30)
g.agregar_vuelo("Guayaquil", "Loja", 45)
g.agregar_vuelo("Cuenca", "Loja", 25)

# Reportería y ejecución de búsqueda
g.mostrar_reporte()
inicio = time.perf_counter()
mejor = {"costo": float("inf"), "ruta": []}
g.buscar_vuelo_mas_barato("Quito", "Loja", 0, set(), [], mejor)
fin = time.perf_counter()

print(f"\nRuta más barata: {' -> '.join(mejor['ruta'])} | Costo: ${mejor['costo']}")
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")