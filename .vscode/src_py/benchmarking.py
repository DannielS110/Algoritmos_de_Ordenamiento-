import metodos_ordenamiento as mo
import random
import time

class Benchmarking:

    def __init__(self):
        print("Benchmarking instanciado")

        self.metodo = mo.MetodoOrdenamiento()
        arreglo = self.build_arreglo(10000)

        tiempos = {}

        print("Ejecutando método Burbuja...")
        tiempos['Burbuja'] = self.medir_tiempo(lambda: self.metodo.sort_bubble(arreglo))

        print("Ejecutando método Selección...")
        tiempos['Selección'] = self.medir_tiempo(lambda: self.metodo.sort_seleccion(arreglo))

        print("\n--- Resultados ---")
        for nombre, tiempo in tiempos.items():
            print(f"{nombre}: {tiempo:.6f} segundos")

        mejor = min(tiempos, key=tiempos.get)
        print(f"\n✅ El mejor método fue: {mejor} con {tiempos[mejor]:.6f} segundos")

    def build_arreglo(self, tamaño):
        return [random.randint(0, 99999) for _ in range(tamaño)]

    def medir_tiempo(self, funcion):
        inicio = time.time_ns()
        funcion()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0
