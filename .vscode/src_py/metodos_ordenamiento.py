class MetodoOrdenamiento:

    def sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo

    def burbujaMejorado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            intercambio = False
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    intercambio = True
            if not intercambio:
                break
        return arreglo

    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_idx]:
                    min_idx = j
            arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
        return arreglo

    def sort_insercion(self, array):
        arreglo = array.copy()
        for i in range(1, len(arreglo)):
            key = arreglo[i]
            j = i - 1
            while j >= 0 and key < arreglo[j]:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = key
        return arreglo

    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo
