# water_jug/simulation.py
from collections import deque

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def water_jug_simulation(m, n, p):
    visited = set()
    queue = deque([(0, 0, [])])
    
    while queue:
        a, b, steps = queue.popleft()
        if a == p or b == p:
            return steps
        
        if (a, b) in visited:
            continue
        visited.add((a, b))
        
        # Fill jug A
        if a < m:
            queue.append((m, b, steps + [f"Fill A"]))
        # Fill jug B
        if b < n:
            queue.append((a, n, steps + [f"Fill B"]))
        # Empty jug A
        if a > 0:
            queue.append((0, b, steps + [f"Empty A"]))
        # Empty jug B
        if b > 0:
            queue.append((a, 0, steps + [f"Empty B"]))
        # Pour from A to B
        if a > 0 and b < n:
            amount = min(a, n - b)
            queue.append((a - amount, b + amount, steps + [f"Pour A to B"]))
        # Pour from B to A
        if b > 0 and a < m:
            amount = min(b, m - a)
            queue.append((a + amount, b - amount, steps + [f"Pour B to A"]))
    
    return None

def solve_water_jug(m, n, p):
    if p > max(m, n) or p % gcd(m, n) != 0:
        return "No solution exists"
    
    solution1 = water_jug_simulation(m, n, p)
    solution2 = water_jug_simulation(n, m, p)
    
    if solution1 and solution2:
        return min(solution1, solution2, key=len)
    elif solution1:
        return solution1
    elif solution2:
        return solution2
    else:
        return "No solution found"