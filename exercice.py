#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

import math
from turtle import forward, back, right, left
import string


# TODO: Définissez vos fonction ici

def calculer_masse_volume(a: float = 1, b: float = 1, c: float = 1, p: float = 1) -> tuple:

    v = (4 * a * b * c * math.pi) / 3
    m = v * p

    return (v, m)

# def histogram(sentence: str):
#
#     dict = {}
#
#     for letter in sentence:
#         if letter == " ":
#             continue
#         elif letter in dict:
#             dict[letter] += 1
#         else:
#             dict.update({letter: 1})
#
#         y = lambda x:
#         return y(letter)
#voir screenshot 19 octobre
#il faut trasnformer le dictionnaire en un autre type de donne afin de pouvoir lordonne

def draw_left(degres, avant):
    left(degres)
    forward(avant)

def arbre():
    i = 0
    degres = 20
    left(90)
    forward(100)
    for _ in range(7):
        i+=2
        draw_left(degres, 100/i)
    #voir screenshot 19 octobre
    pass
    





def valide(adn: str):
    if len(adn) == 0: return False
    for i in adn:
        if i == "u" or i == "g" or i == "t" or i =="c":
            bool = True
        else: return False
    return bool

def saisi(phrase: str):
    if valide(phrase):
        return str
    else: return False

def proportion (chaine: str , sequence: str):
    proportion = (chaine.count(sequence)/len(chaine)) * 100
    return f'Il y a {proportion}% de "{sequence}".'







if __name__ == '__main__':
    #print(arbre())
    # print(calculer_masse_volume())
    # print(calculer_masse_volume(2, 3, 4, 5))
    # print(calculer_masse_volume(2, 6, 7.7, 23.8))
    # print(histogram("jaime les tomates"))
    # print(valide(""))
    # print(valide("ugtc"))
    # print(valide("ugtcugg gtcu"))
    # print(valide("ugtcrugggtcu"))
    #
    # print(proportion("ugtcatgctaug", "ug"))
