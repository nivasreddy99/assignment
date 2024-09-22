# water_jug/diophantine.py

def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x

def solve_diophantine(m, n, p):
    gcd, x, y = extended_euclidean(m, n)
    if p % gcd != 0:
        return None
    
    x *= p // gcd
    y *= p // gcd
    
    # Minimize the number of steps
    while x < 0 or y > 0:
        x += n // gcd
        y -= m // gcd
    while x > 0 and y < 0:
        x -= n // gcd
        y += m // gcd
    
    return abs(x) + abs(y)