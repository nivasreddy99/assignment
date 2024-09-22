# execution_time/complexity_analysis.py
import subprocess
import time
import math
import matplotlib.pyplot as plt
import numpy as np

def run_executable(executable, input_size):
    start_time = time.time()
    subprocess.run([executable, str(input_size)], capture_output=True)
    end_time = time.time()
    return end_time - start_time

def analyze_executables():
    executables = ["./file_1", "./file_2"]  # Adjust paths as needed
    input_sizes = [10**i for i in range(2, 6)]  # 10^2 to 10^5
    
    plt.figure(figsize=(10, 6))
    
    for executable in executables:
        times = []
        for size in input_sizes:
            execution_time = run_executable(executable, size)
            times.append(execution_time)
        
        # Plot log-log graph
        plt.loglog(input_sizes, times, marker='o', label=executable)
        
        # Estimate complexity
        log_sizes = [math.log(size) for size in input_sizes]
        log_times = [math.log(time) for time in times]
        slope, _ = np.polyfit(log_sizes, log_times, 1)
        
        complexity = "O(n)" if slope < 1.5 else "O(n^2)" if slope < 2.5 else "O(n^3)"
        print(f"{executable} estimated complexity: {complexity} (slope: {slope:.2f})")
    
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time vs Input Size")
    plt.legend()
    plt.grid(True)
    plt.savefig("complexity_analysis.png")
    plt.close()

    # Analyze output to determine what the code does
    sample_output = subprocess.run(["./file_1", "100"], capture_output=True, text=True).stdout
    print(f"Sample output for analysis:\n{sample_output}")
    print("Based on the output, analyze the pattern to determine what the code does.")

if __name__ == "__main__":
    analyze_executables()