# main.py
from water_jug import comparison as wj_comparison
from execution_time import complexity_analysis
from streaming_median import comparison as sm_comparison

def main():
    print("1. Water Jug Problem")
    wj_comparison.run_comparison()

    print("\n2. Comparing Execution Times")
    complexity_analysis.analyze_executables()

    print("\n3. Median of Streaming Numbers")
    sm_comparison.compare_algorithms()

    print("\n4. Summary")
    print("Please write your summary here based on your experience with the assignment.")

if __name__ == "__main__":
    main()