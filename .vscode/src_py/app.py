import benchmarking as bm
import metodos_ordenamiento as mo

if __name__ == "__main__":
    print("Hola Mundo")
    bench = bm.Benchmarking()
    metodos = mo.MetodoOrdenamiento()

    tamanos = [5000, 10000, 20000]
    resultados = []

    for tam in tamanos:
        print(f"\n--- Ejecutando para tamaño {tam} ---")
        arreglo_base = bench.build_arreglo(tam)

        metodos_dic = {
            "Burbuja": metodos.sort_bubble,
            "Burbuja Mejorado": metodos.burbujaMejorado,
            "Seleccion": metodos.sort_seleccion,
            "Insercion": metodos.sort_insercion,
            "Shell": metodos.sort_shell
        }

        tiempos_tamano = []

        for nombre, metodo in metodos_dic.items():
            print(f"Ejecutando {nombre}...")
            tiempo_resultado = bench.medir_tiempo(metodo, arreglo_base)
            resultados.append((tam, nombre, tiempo_resultado))
            tiempos_tamano.append((nombre, tiempo_resultado))

        mejor = min(tiempos_tamano, key=lambda x: x[1])
        print(f"\n✅ El mejor método para tamaño {tam} fue: {mejor[0]} con {mejor[1]:.6f} segundos")

    print("\n--- Resumen General ---")
    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, Método: {nombre}, Tiempo: {tiempo:.6f} segundos")
