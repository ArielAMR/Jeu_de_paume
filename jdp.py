##!/usr/bin/env python 
##
## EPITECH PROJECT, 2024
## Jeu_de_paume
## File description:
## jdp.py
##


from math import *
from sys import *

g = 3.71
def calculateur_teta(V0, D, H, h):
    teta_1 = 0
    teta_2 = pi / 2
    teta = (teta_1 + teta_2) / 2
    y =  - (g * D**2) / (2 * V0**2 * cos(teta)**2) + D * tan(teta) + H
    while abs(y - h) > 0.01:
        if y > h:
            teta_2 = teta
        else:
            teta_1 = teta
        teta = (teta_1 + teta_2) / 2
        y =  - (g * D**2) / (2 * V0**2 * cos(teta)**2) + D * tan(teta) + H
    print(f"{degrees(teta):.3f}°")
def calculateur_i(V0, D, H):
    Ay2 = 1.1 + 0.03
    calculateur_teta(V0, D, H, Ay2)
    By2 = 2.2 - 0.03
    calculateur_teta(V0, D, H, By2)

if len(argv) == 2:
    print("Give 3 arguments. 1st is the original speed, 2nd is the distance to the back net, and 3d is the height racket")
    exit(0)

if len(argv) != 4:
    print("please insert 3 arguments or retry with -h.")
    exit(84)

for i in range(3):
    if argv[i + 1].replace(".", "").isnumeric() == False:
        exit(84)

calculateur_i(float(argv[1]), float(argv[2]), float(argv[3]))
