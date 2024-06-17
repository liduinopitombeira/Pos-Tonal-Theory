# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:37:33 2024

@author: Liduino Pitombeira

"""

from normal import *

#Inversão TnI em torno de 0 e dá o resultado na forma normal
def I(conjunto, fator):

    inv = [((12-x) + fator)%12 for x in conjunto]
    return inv

def prima(conjunto):
    
    conjunto = normal(conjunto)
    inverso = I(conjunto,0)
    inverso = normal(inverso)
    
    intervalo_original = (conjunto[0] - conjunto[1])%12
    intervalo_inverso = (inverso[0] - inverso[1])%12
    
    if intervalo_original>intervalo_inverso:
        k = conjunto[0]
        fator = 12 - k
        formaprima = [(x+fator)%12 for x in conjunto]
        
    else:
        k = inverso[0]
        fator = 12 - k
        formaprima = [(x+fator)%12 for x in inverso]
        
    
    return formaprima


def main():
    conjunto = input('Entre com classes de conjuntos separadas por espaços: ').split()
    conjunto = [int(x) for x in conjunto]
    
    resultado = prima(conjunto)
    
    print('Forma normal:', normal(conjunto))
    print('Forma prima:', resultado)
    
    return resultado    
    

if __name__ == "__main__":
    main()