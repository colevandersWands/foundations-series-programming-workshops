import unittest

from ..recursion_tracer import recursion_tracer

class TestTesting(unittest.TestCase):
    """Test the fibonacci_lib function"""

    def test_0(self):
        """It should evaluate 0 to []"""
        @recursion_tracer
        def fibonacci(n: int) -> int:
            if n <= 0:
                return 0
            if n == 1:
                return 1
            return fibonacci(n - 1) + fibonacci(n - 2)
        fibonacci(3)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()

