import math

def fermat_fatorar(n):
    a = math.isqrt(n)
    if a * a < n:
        a += 1

    b2 = a*a - n
    it = 0

    while math.isqrt(b2)**2 != b2:
        a += 1
        b2 = a*a - n
        it += 1

    b = math.isqrt(b2)
    return a - b, a + b, it

for n in [5959, 10403, 8051]:
    p, q, it = fermat_fatorar(n)
    print(f"n={n} => p={p}, q={q}, iteracoes={it}, verif={p*q}")