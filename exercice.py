#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

import math
import turtle


# TODO: Définissez vos fonction ici

def calculer_masse_volume(a: float = 1, b: float = 1, c: float = 1, p: float = 1) -> tuple:

    v = (4 * a * b * c * math.pi) / 3
    m = v * p

    return (v, m)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(calculer_masse_volume())
    print(calculer_masse_volume(2, 3, 4, 5))
    print(calculer_masse_volume(2, 6, 7.7, 23.8))
