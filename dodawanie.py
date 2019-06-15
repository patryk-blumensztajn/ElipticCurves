# Dodanie punktów
def dodawanie_punktow(punkt1, punkt2, krzywa):
    x1, y1 = punkt1[0], punkt1[1]
    x2, y2 = punkt2[0], punkt2[1]
    APoint, BPoint, p = krzywa[0], krzywa[1], krzywa[2]

    if (x1 == x2 and y1 != y2):
        return None, None
    if (punkt1 == punkt2 and y1 == 0):
        return None, None

    if punkt1 == punkt2:
        if punkt1 == (None, None): # neutralny
            return (None, None)

        lamb = ((3 * pow(x1, 2) + APoint) * pow(2 * y1, p - 2, p)) % p

    else:
        if punkt1 == (None, None): # neutralny
            return punkt2
        if punkt2 == (None, None):
            return punkt1

        lamb = ((y2 - y1) * pow(x2 - x1, p - 2, p)) % p

    x3 = (pow(lamb, 2) - x1 - x2) % p
    y3 = (lamb * (x1 - x3) - y1) % p

    return x3, y3