📊 Algoritmos de Ordenamiento - Análisis de Complejidad 📊

Información General

Integrantes:

Daniel Sanchez (DannielS110)    

![image](https://github.com/user-attachments/assets/ad8f5e09-5867-431e-9560-4dcf929f34a0)



Joey Diaz (LASERX22)         

![image](https://github.com/user-attachments/assets/152285df-e4ce-440f-b527-0e3b9ff8d5ba)



Docente: Ing. Pablo Torres

Ciclo: 2 Ciclo


Asignatura: Estructura de Datos

Práctica: 4.2 - Algoritmos de Ordenamiento

----------------------------------------------------------------------------------------------
🔗 Enlace al Repositorio del Proyecto

[[Enlace a GitHub/GitLab del proyecto]
](https://github.com/DannielS110/Algoritmos_de_Ordenamiento-)

----------------------------------------------------------------------------------------------

📝 Descripción

Este proyecto implementa y analiza diferentes algoritmos de ordenamiento para determinar su eficiencia en términos de tiempo de ejecución con diferentes tamaños de conjuntos de datos. Se evalúan los siguientes 

métodos de ordenamiento:

🔄 Burbuja (Bubble Sort)

🔄 Burbuja Mejorado (Optimized Bubble Sort)

🔄 Selección (Selection Sort)

🔄 Inserción (Insertion Sort)

🔄 Shell Sort

----------------------------------------------------------------------------------------------

📂 Estructura del Proyecto

app.py: Programa principal que ejecuta las pruebas y genera las gráficas

benchmarking.py: Clase para medir tiempos de ejecución y generar arreglos de prueba

metodos_ordenamiento.py: Implementación de los algoritmos de ordenamiento

graficas.py: Funciones para generar visualizaciones

----------------------------------------------------------------------------------------------

📊 Resultados Obtenidos


![code (1)](https://github.com/user-attachments/assets/e80b97f0-3433-4cc2-bfd1-2522899ee248)

----------------------------------------------------------------------------------------------


📈 Gráfica Comparativa


![Figure_1](https://github.com/user-attachments/assets/62342886-fcd1-4efc-aa3b-946955cca341)

Conclusiones
El análisis de los algoritmos de ordenamiento implementados muestra claras diferencias en su rendimiento:

Shell Sort es notablemente superior, completando el ordenamiento de 100,000 elementos en menos de 1 segundo, demostrando la eficiencia de su complejidad O(n log² n).

Los algoritmos con complejidad O(n²) (Burbuja, Burbuja Mejorado, Selección e Inserción) muestran un deterioro drástico del rendimiento a medida que aumenta el tamaño del arreglo, llegando a tardar más de 6 

minutos en los casos más lentos.

La diferencia de rendimiento es más pronunciada en arreglos grandes, donde Shell es aproximadamente 380 veces más rápido que los algoritmos de burbuja.

Estos resultados confirman la importancia de elegir algoritmos eficientes, especialmente cuando se trabaja con grandes cantidades de datos.

Esta práctica demuestra empíricamente por qué el análisis de complejidad algorítmica es fundamental en el desarrollo de software eficiente.


