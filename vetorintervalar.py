# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 11:19:19 2023

@author: Liduino
"""

from music21 import *


def normal(conjunto):
    
    normal = chord.Chord(conjunto).normalOrder
    
    return normal

def vetor(conjunto):
    
    vetor=[]
    
    for x in conjunto:
        for y in conjunto[1:]:
            
            valor = (y-x)%12
            vetor.append(valor)
            
    return vetor        

def transposition(conjunto, fator):
    
    trans = [(x + fator)%12 for x in conjunto]
    return normal(trans)


def inversion(conjunto, fator):
    
    inv = [((12-x) + fator)%12 for x in conjunto]
    return normal(inv)


def str_int(lst):
    return [int(x) for x in lst.split()]


conjunto = str_int(input('Entre com o conjunto separado por espaços:'))

