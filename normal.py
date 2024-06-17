# -*- coding: utf-8 -*-
"""
Created on Wed May 11 2024

@author: Liduino Pitombeira
"""

def normal(conjunto):
    
    conjunto = list(set(conjunto))
    conjunto.sort()
    
    lista = [conjunto[k:] + conjunto[:k] for k in range(len(conjunto))]
    # print ('Lista = ', lista)
    
    
    position = 1
    
    while position<=len(lista[0]):
        # print ('Len lista[0] = ', len(lista[0]))
        intervalos = [(lista[x][-position] - lista[x][0]) % 12 for x in range(len(lista))]
        # print ('Intervalos = ', intervalos)
        menor = min(intervalos)
        # print('Menor =', menor)
        indices = [i for i, x in enumerate(intervalos) if x == menor]
        # print('Indices =', indices)
        novalista = [lista[x] for x in indices]
        # print('Novalista =', novalista)
        lista = novalista
        position += 1
        # print('Position =', position)
        # print('Check =', position<=len(lista[0]))
        
    return lista[0]


def main():
    conjunto = input('Entre com classes de conjuntos separadas por espaços: ').split()
    conjunto = [int(x) for x in conjunto]
    
       
    resultado = normal(conjunto)
    
    print('Forma normal:', resultado)
    
    return resultado


if __name__ == "__main__":
    main()
