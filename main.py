# main.py
from water_jug import comparison as wj_comparison
from streaming_median import comparison as sm_comparison

def main():
    print("1. Water Jug Problem")
    wj_comparison.run_comparison()
  
    print("\n2. Median of Streaming Numbers")
    sm_comparison.compare_algorithms()


if __name__ == "__main__":
    main()