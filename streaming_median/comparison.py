# streaming_median/comparison.py
import time
import random
from .heap_median import MedianFinder
from .static_median import static_median

def compare_algorithms():
    test_sizes = [10**i for i in range(0, 5)]  # 10^2 to 10^6
    
    print("Comparing Streaming Median algorithms:")
    print("Size\tHeap Time\tStatic Time")
    
    for size in test_sizes:
        numbers = [random.randint(1, 1000000) for _ in range(size)]
        
        # Heap-based algorithm
        start_time = time.time()
        median_finder = MedianFinder()
        for num in numbers:
            median_finder.addNum(num)
        heap_median = median_finder.findMedian()
        heap_time = time.time() - start_time
        
        # Static algorithm
        start_time = time.time()
        for num in range(len(numbers)): 
            static_median_result = static_median(numbers[:num+1])  # Update static median in-place
            
        static_time = time.time() - start_time
        
        print(f"{size}\t{heap_time:.6f}\t{static_time:.6f}")
    
    print("\nExample of heap-based algorithm:")
    example_numbers = [5, 2, 8, 1, 9, 3, 7]
    median_finder = MedianFinder()
    print("Input\tMedian")
    for num in example_numbers:
        median_finder.addNum(num)
        print(f"{num}\t{median_finder.findMedian():.1f}")

if __name__ == "__main__":
    compare_algorithms()