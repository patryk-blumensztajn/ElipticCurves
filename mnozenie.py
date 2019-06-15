from dodawanie import dodawanie_punktow

# Mnożenie punktu
def mnozenie_punktow(punkt, n, ec):
    P = punkt
    Q = (None, None)

# Zgodnie ze wzorem Eliptic Curves Multiplication
    for iterator in reversed(bin(n)[2:]):  # Reversed zwraca odwrócony ciąg znaków,  znaki od pozycji 2 do końca
        if iterator == '1':
            if Q == (None, None):
                Q = P
            else:
                Q = dodawanie_punktow(Q, P, ec)
        P = dodawanie_punktow(P, P, ec)
    return Q