import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

from recursion_tracer import recursion_tracer

# --- demo functions ---

@recursion_tracer
def fibonacci_memo(n: int, memo: dict = {}) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

@recursion_tracer
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

@recursion_tracer
def reverse_list(to_reverse: list) -> list:
    if len(to_reverse) == 0:
        return []
    return reverse_list(to_reverse[1:]) + [to_reverse[0]]

# --- demo calls ---

fibonacci(6)
fibonacci_memo(6)
reverse_list([4,2,3,1])
