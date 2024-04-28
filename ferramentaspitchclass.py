# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 11:19:19 2023

@author: Liduino Pitombeira
"""

from music21 import *
from itertools import *

#Calcula a paleta de uma classe de conjuntos
def paleta(classe):
    
            
    paletaT = [normal([(y+x)%12 for y in classe]) for x in range(12)]
    paletaI = [normal([(12-y+x)%12 for y in classe]) for x in range(12)]
    
    paleta = set(map(tuple, paletaT + paletaI))
    
    return paleta


#Calcula forma prima
def prime(conjunto):
    
    prime = chord.Chord(conjunto).primeForm
    
    return prime

#Calcula forma normal
def normal(conjunto):
    
    normal = chord.Chord(conjunto).normalOrder
    
    return normal

#Calcula o vetor de classes de intervalares
def vetor(conjunto):
    
    vetor = [0,0,0,0,0,0]
    
    sub = set(combinations(conjunto, 2))
    sub = list(sub)
    sub = [list(x) for x in sub]
    
    # print(sub)
    
    for x in range(len(sub)):
        
        valor = (sub[x][1]-sub[x][0])%12
        # print(valor)
        if valor==1 or valor==11: vetor[0]=vetor[0]+1
        if valor==2 or valor==10: vetor[1]=vetor[1]+1
        if valor==3 or valor==9: vetor[2]=vetor[2]+1
        if valor==4 or valor==8: vetor[3]=vetor[3]+1 
        if valor==5 or valor==7: vetor[4]=vetor[4]+1 
        if valor==6 : vetor[5]=vetor[5]+1
        
                  
    return vetor        

#Transposição Tn e dá o resultado na forma normal"
def T(conjunto, fator):
    
    trans = [(x + fator)%12 for x in conjunto]
    return normal(trans)


#Inversão TnI em torno de 0 e dá o resultado na forma normal
def I(conjunto, fator):

    inv = [((12-x) + fator)%12 for x in conjunto]
    return normal(inv)

#Transforma a entrada em lista de inteiros
def str_int(lst):
    return [int(x) for x in lst.split()]


conjunto = str_int(input('Entre com o conjunto separado por espaços:'))

