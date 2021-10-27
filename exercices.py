import random


# Exercice 1
def pair(n):
    n = int(n)
    if n % 2 == 0:
        return True
    return False


# Exercice 2
def age(n):
    n = int(n)
    if n >= 18:
        return "Majeur"
    return "Mineur"


# Exercice 3
def sophie():
    s = 1000
    print(2020, "=", s, "€  ")
    for k in range(2021, 2041):
        s = round(s * 1.02 + 100, 2)
        print(k, "=", s, "€")


# Exercice 4
def sophie_annee(n):
    s = 1000
    for k in range(2020, n):
        round(s * 1.02 + 100, 2)
    print(s, "€")


# Exercice 5
def fibonacci():
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for k in range(2, 11):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)


# Exercice 6
def somme(n):
    n = int(n)
    s = 0
    for k in range(n + 1):
        s += k
    return s


# Exercice 7
def alea():
    a = random.randint(1, 6)
    return a


# Exercice 8
def nbrpair():
    a = alea()
    if a % 2 == 0:
        return a, True
    return a, False


# Exercice 9
def guess(n):
    a = alea()
    if n == a:
        return n, a, True
    return n, a, False


# Exercice 10
def jeu():
    a = alea()
    b = alea()
    c = alea()
    if a == 1 and b == 2 and c == 4:
        return a, b, c, True
    elif a == 1 and b == 4 and c == 2:
        return a, b, c, True
    elif a == 2 and b == 1 and c == 4:
        return a, b, c, True
    elif a == 2 and b == 4 and c == 1:
        return a, b, c, True
    elif a == 4 and b == 1 and c == 2:
        return a, b, c, True
    elif a == 4 and b == 2 and c == 1:
        return a, b, c, True
    return a, b, c, False


# Bonus
# Exercice 10.1
def jeu_ugo():
    a = alea()
    b = alea()
    c = alea()
    if a == 4 or a == 2 or a == 1:
        if b == 4 or b == 2 or b == 1:
            if c == 4 or c == 2 or c == 1:
                if a != b and b != c and a != c:
                    return a, b, c, True
    return a, b, c, False


# Exercice 11
def decimal(n):
    a = bin(n)[2::]
    b = hex(n)[2::]
    print("base 2 →", a)
    print("base 16 →", b)


# Exercice 12
def binaire(n):
    n = str(n)
    a = int(n, 2)
    b = hex(int(n, 2))[2::]
    print("base 10 →", a)
    print("base 16 →", b)


# Exercice 13
def hexadecimale(n):
    a = int(n, 16)
    b = bin(int(n, 16))[2::]
    print("base 10 →", a)
    print("base 2 →", b)


# Exercice 14
def puissance(n):
    n = int(n)
    for k in range(1, 11):
        print(n, "**", k, "=", n**k)


# Exercice 15
def decomposition(n):
    k = 0
    L = []
    while 2**k <= n:
        k += 1
    p = 2**(k-1)
    for i in range(k):
        if p <= n:
            L.append(p)
            n -= p
        p //= 2
    print(L)
