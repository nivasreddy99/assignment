# water_jug/comparison.py
import time
from .simulation import solve_water_jug
from .diophantine import solve_diophantine

def run_comparison():
    test_cases = [
        (3, 5, 4),
        (2, 6, 5),
        (17, 23, 8),
        (99, 97, 5),
        (1000, 1001, 1),
        (9999, 10000, 1),
        (12345, 67890, 9),
        (100000, 100001, 1),
        (999999, 1000000, 1)
    ]
    
    print("Comparing Water Jug Problem solutions:")
    print("M\tN\tP\tSimulation Time\tDiophantine Time\tSimulation Steps\tDiophantine Steps")
    
    for m, n, p in test_cases:
        start_time = time.time()
        sim_solution = solve_water_jug(m, n, p)
        sim_time = time.time() - start_time
        
        start_time = time.time()
        dio_solution = solve_diophantine(m, n, p)
        dio_time = time.time() - start_time
        
        sim_steps = len(sim_solution) if isinstance(sim_solution, list) else "N/A"
        
        print(f"{m}\t{n}\t{p}\t{sim_time:.6f}\t{dio_time:.6f}\t{sim_steps}\t{dio_solution}")

if __name__ == "__main__":
    run_comparison()