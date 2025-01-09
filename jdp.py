import math
g = 3.71
def calculateur_teta(V0, D, H, h):
    teta_1 = 0
    teta_2 = math.pi / 2
    teta = (teta_1 + teta_2) / 2
    y =  - (g * D**2) / (2 * V0**2 * math.cos(teta)**2) + D * math.tan(teta) + H
    while abs(y - h) > 0.01:
        if y > h:
            teta_2 = teta
        else:
            teta_1 = teta
        teta = (teta_1 + teta_2) / 2
        y =  - (g * D**2) / (2 * V0**2 * math.cos(teta)**2) + D * math.tan(teta) + H
    print(math.degrees(teta))
def calculateur_i(V0, D, H):
    Ay2 = 1.1 + 0.03 
    calculateur_teta(V0, D, H, Ay2)
    By2 = 2.2 - 0.03
    calculateur_teta(V0, D, H, By2)
calculateur_i(18.6, 28, 1)
