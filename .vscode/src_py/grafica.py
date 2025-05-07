import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#crear un grafic  de lineas
plt.plot(x,y, label='linea', color='blue')

plt.title('Grafica de Lineas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y') 

plt.legend()
plt.show()