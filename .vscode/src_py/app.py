import benchmarking as bm
import metodos_ordenamiento as mo
import matplotlib.pyplot as plt
import copy
import datetime

if __name__ == "__main__":
    bench = bm.Benchmarking()
    metodos = mo.MetodoOrdenamiento()
    
    tamanos = [5000, 10000, 30000, 50000, 100000]
    resultados = []
    
    metodos_dic = {
        "burbuja": metodos.sort_bubble,
        "burbuja_mejorado": metodos.burbujaMejorado,
        "seleccion": metodos.sort_seleccion,
        "insercion": metodos.sort_insercion,
        "shell": metodos.sort_shell
    }
    
    arreglo_base_grande = bench.build_arreglo(max(tamanos))
    for tam in tamanos:
        print(f"\n--- Ejecutando para tamaño {tam} ---")
        arreglo_base = arreglo_base_grande[:(tam)]
        for nombre, metodo in metodos_dic.items():
            print(f"Ejecutando {nombre}...")
            tiempo_resultado = bench.medir_tiempo(metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo_resultado))
    
    for tam, nombre, tiempo in resultados:
        print(f"Tamano: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")

    tiempos_by_metodo = {nombre: [] for nombre in metodos_dic}
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append((tam, tiempo))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    fig.suptitle("DANIEL SÁNCHEZ, JOEY DIAZ – 06/05/2025 19:43:21", fontsize=14, fontweight='bold')

    for nombre, datos in tiempos_by_metodo.items():
        x = [tam for tam, _ in datos]
        y = [tiempo for _, tiempo in datos]
        ax1.plot(x, y, label=nombre, marker='o')

    ax1.set_title("Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento")
    ax1.set_xlabel("Tamaño del arreglo")
    ax1.set_ylabel("Tiempo de ejecución (segundos)")
    ax1.grid(True)
    ax1.legend()

    
    for nombre, datos in tiempos_by_metodo.items():
        x = [tam for tam, _ in datos]
        y = [tiempo for _, tiempo in datos]
        ax2.plot(x, y, label=nombre, marker='o')
    
    ax2.set_title("Comparación de algoritmos de ordenamiento")
    ax2.set_xlabel("Tamaño del arreglo")
    ax2.set_ylabel("Tiempo de ejecución (segundos)")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig("figura_comparativa.png", dpi=300)
    plt.show()


