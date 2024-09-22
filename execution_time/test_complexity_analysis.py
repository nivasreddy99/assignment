# execution_time/test_complexity_analysis.py
import unittest
from unittest.mock import patch, Mock
from .complexity_analysis import run_executable, analyze_executables

class TestComplexityAnalysis(unittest.TestCase):
    @patch('subprocess.run')
    @patch('time.time')
    def test_run_executable(self, mock_time, mock_run):
        mock_time.side_effect = [0, 1]  # Simulate 1 second execution time
        mock_run.return_value = Mock()

        execution_time = run_executable("dummy_executable", 100)
        
        self.assertEqual(execution_time, 1)
        mock_run.assert_called_once_with(["dummy_executable", "100"], capture_output=True)

    @patch('matplotlib.pyplot.savefig')
    @patch('subprocess.run')
    @patch('time.time')
    def test_analyze_executables(self, mock_time, mock_run, mock_savefig):
        mock_time.side_effect = [i for i in range(0, 20, 2)]  # Simulate increasing execution times
        mock_run.return_value = Mock(stdout="Sample output")

        with patch('builtins.print') as mock_print:
            analyze_executables()

        mock_savefig.assert_called_once_with("complexity_analysis.png")
        self.assertTrue(any("estimated complexity" in str(call) for call in mock_print.call_args_list))
        self.assertTrue(any("Sample output for analysis" in str(call) for call in mock_print.call_args_list))

if __name__ == '__main__':
    unittest.main()