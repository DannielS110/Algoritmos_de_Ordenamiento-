import metodos_ordenamiento as mo
import random
import time
import copy
class Benchmarking:

    def __init__(self):
        self.mO = mo.MetodoOrdenamiento()
        print("Benchmarking instanciado")

    def medir_tiempo(self, metodo, arreglo):
        arreglo = copy.deepcopy(arreglo)
        inicio = time.perf_counter()
        metodo(arreglo)
        fin = time.perf_counter()
        return fin - inicio

    def build_arreglo(self, tamano, semilla = 42):
       random.seed(semilla) 
       return [random.randint(0, 999999) for _ in range(tamano)]
       random.sedd()
       return arreglo
    
    def contar_con_current_time_milles(self, tarea):
        x = time.time()
        tarea()
        fin = time.time()
        tiempo_segundos = fin - x
        return f"Tiempo en milisegundos: {tiempo_segundos*1000}"

    def contar_con_nano_time(self, tarea):
        x = time.time_ns()
        tarea()
        fin = time.time_ns()
        tiempo_nano_segundos = (fin - x) / 1_000_000_000.0
        return f"Tiempo en nanosegundos: {tiempo_nano_segundos}"
