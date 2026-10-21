import numpy as np

print("---- llenar matrz de ceros ----")
matriz=np.zeros([3,5]) # 3 filas x 5 columnas 
print(matriz)
print("---- llenar matrz de unos ----")
matriz=np.ones([3,5])
print(matriz)
print("---- llenar matriz vacios ----")
matriz=np.empty([3,5])
print(matriz)
print("---- llenar arrelo con rango ----")
# el primer parametro s el vlo inicial
# el segundo parametro es el valor final
# el tercero  parametro es el incremento 
listas=np.arange(0,10,2)
print(listas)
print("---- llenar arrelo con rango  N0 2----")