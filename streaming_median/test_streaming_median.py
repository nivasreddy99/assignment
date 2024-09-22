# streaming_median/test_streaming_median.py
import unittest
import random
from .heap_median import MedianFinder
from .static_median import static_median

class TestStreamingMedian(unittest.TestCase):
    def test_heap_median(self):
        finder = MedianFinder()
        numbers = [5, 2, 8, 1, 9, 3, 7]
        expected_medians = [5.0, 3.5, 5.0, 3.5, 5.0, 4.0, 5.0]
        
        for num, expected in zip(numbers, expected_medians):
            finder.addNum(num)
            self.assertAlmostEqual(finder.findMedian(), expected, places=6)

    def test_static_median(self):
        numbers = [5, 2, 8, 1, 9, 3, 7]
        self.assertEqual(static_median(numbers), 5.0)

    def test_large_input(self):
        numbers = [random.randint(1, 1000000) for _ in range(100000)]
        
        finder = MedianFinder()
        for num in numbers:
            finder.addNum(num)
        
        heap_median = finder.findMedian()
        static_median_result = static_median(numbers)
        
        self.assertAlmostEqual(heap_median, static_median_result, places=6)

    def test_odd_even_transitions(self):
        finder = MedianFinder()
        numbers = [1, 2, 3, 4, 5]
        expected_medians = [1.0, 1.5, 2.0, 2.5, 3.0]
        
        for num, expected in zip(numbers, expected_medians):
            finder.addNum(num)
            self.assertAlmostEqual(finder.findMedian(), expected, places=6)

    def test_duplicate_values(self):
        finder = MedianFinder()
        numbers = [1, 1, 2, 2, 3]
        expected_medians = [1.0, 1.0, 1.0, 1.5, 2.0]
        
        for num, expected in zip(numbers, expected_medians):
            finder.addNum(num)
            self.assertAlmostEqual(finder.findMedian(), expected, places=6)

if __name__ == '__main__':
    unittest.main()