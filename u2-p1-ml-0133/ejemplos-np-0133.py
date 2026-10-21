import numpy as np 

califas=np.array([60,70,90])
print("------------ ej 1 imprimir califas")
print(califas)# imprime la listas de califa
print(type(califas)) # muestra el tipo de arreglo
print("--ejemplo 2 imprimir califas-----")
califas=np.array(60)
print("califas")
print("Dimension :",califas.ndim)
print("--ejemplo 1 dimension de un array-----")
califas=np.array([60,70,90])
print(califas)
print("Dimension :",califas.ndim)
print("--ejemplo 2 imprimir array-----")
califas=np.array([
    [
    [60,70,90],
    [50,80,98]
   ],       
   [   
    [60,70,90],
    [50,80,98]
   ] 
]) # un arreglo de 2 dimenciones es como una taba en excel
print(califas)
print("dimension:",califas)
