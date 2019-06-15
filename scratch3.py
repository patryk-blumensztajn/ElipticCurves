
from colors import prCyan, prGreen, prRed
from random import randint, getrandbits
from sympy import isprime
from mnozenie import  mnozenie_punktow


# Funkcja generująca losową liczbę pierwszą spełniającą warunki zadania
def losowanie_liczby_p(len=256):
    p = 0
    while (not isprime(p)) or (not (p % 4 == 3)):
        p = getrandbits(len)
        p |= (1 << len - 1) | 1
    return p


# Metoda zwracająca A, B oraz p
def generuj_krzywa_eliptyczna(len):
    Delta = 0
    while Delta == 0:
        p = losowanie_liczby_p(len)
        prGreen("{Wylosowana liczba p: " + f"{p}")
        A = randint(0, p - 1)
        prGreen("{Wylosowana liczba A: " + f"{A}")
        B = randint(0, p - 1)
        prGreen("{Wylosowana liczba B: " + f"{B}")
        Delta = (4 * (A ** 3) + 27 * B ** 2) % p
        prGreen("{Delta: " + f"{Delta}")

    return (A, B, p)


# Obliczenie punktu dla krzywej
def punkty_krzywej(A, B, p):
    warunek = 0
    while warunek != 1:
        punkt_x = randint(0, p - 1)  # Losowanie punktu
        f = (punkt_x ** 3 + A * punkt_x + B) % p  # Obliczenie F
        warunek = pow(f, (p - 1) // 2, p)  # Czy jest spełniony warunek

    punkt_y = pow(f, (p + 1) // 4, p)
    prGreen("{Obliczony punkt P: " + f"{(punkt_x, punkt_y)}")
    sprawdzenie_oraz_wypisanie_E(A, B, p, punkt_y, punkt_x)
    return (punkt_x, punkt_y)


# Obliczanie E
def sprawdzenie_oraz_wypisanie_E(A,B,p,punkt_y,punkt_x):
    lewa = (punkt_y ** 2) % p
    prawa = ((punkt_x ** 3) + A * punkt_x + B) % p
    prGreen("{Obliczone E: " + f"{lewa}" + " = " + f"{prawa}")


'''                           Wzory użyte zgodnie z wykładem
                            Delta = 4*a^3 + 27b^2 == 0 (mod p)
                                  f = x^3+a*x+b(mod p)
                               E : y^2 = x3 + a*x + b (mod p)
'''


##*********************************************
# Kolejne kroki w Algorytmie Diffiego Hellmanie
#**********************************************


# Znajdowanie krzywej (p test pierwszości, a, b oraz delta)
prCyan("\nZnajdownie krzywej")
KrzewaEliptyczna = generuj_krzywa_eliptyczna(250)

# Znajdowanie punktu oraz wypisanie E
prCyan("\nZnajdowanie punktu na krzywej")
q = punkty_krzywej(KrzewaEliptyczna[0], KrzewaEliptyczna[1], KrzewaEliptyczna[2])


# ALICE
n = randint(1, KrzewaEliptyczna[2])
prRed("\nALICE")
print("{Wylosowana liczba n: " + f"{n}")
PunktA = mnozenie_punktow(q, n, KrzewaEliptyczna)
print("{Mnożenie punktu: " + f"{PunktA}")

# BOB
k = randint(1, KrzewaEliptyczna[2])
prRed("\nBOB")
print("{Wylosowana liczba k: " + f"{k}")
PunktB = mnozenie_punktow(q, k, KrzewaEliptyczna)
print("{Mnożenie punktu: " + f"{PunktB}")

# Wymiana wiadomości
# Mnożenie oraz dodwanie punktów
RAlice = mnozenie_punktow(PunktB, n, KrzewaEliptyczna)
RBob = mnozenie_punktow(PunktA, k, KrzewaEliptyczna)

# Czy wygenerowane R są sobie równe
prRed("\nCzy R wylosowane przez Alice i Boba są sobie równe? ")
print(f"{RAlice == RBob}")

# Sprawdzenie czy punkt należy do krzywej
prRed("\nCzy punkt R należy do krzywej?")
print(f"{(RBob[1] ** 2) % KrzewaEliptyczna[2]} = {(RBob[0] ** 3 + RBob[0] * KrzewaEliptyczna[0] + KrzewaEliptyczna[1]) % KrzewaEliptyczna[2]}")
print((RBob[1] ** 2) % KrzewaEliptyczna[2] == (RBob[0] ** 3 + RBob[0] * KrzewaEliptyczna[0] + KrzewaEliptyczna[1]) % KrzewaEliptyczna[2])

