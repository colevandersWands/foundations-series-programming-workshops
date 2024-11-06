#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Tree Recursion

Tree recursion is a recursive function calls itself more than once in the body.

The names "Linear" and "Tree" recursion will make sense after the next chapter:
    2. Visualizing Recursion

This is a recursive function with two base cases and two recursive calls.

"""

def fibonacci(n: int) -> int:
    """
    Calculates the n'th number in the Fibonacci Sequence.

    base case 1:
        0               ->   0
    base case 2:
        1                ->   1
    recursive case:
        n > 1          ->   ƒ(n - 1) + ƒ(n - 2)
    """
    if n <= 0:  # base case 1
        return 0 # turn-around 1
    
    if n == 1:  # base case 2
        return 1 # turn-around 2
    
    #            rec. 1   | bd 1 |       rec. 2  | bd 2 |
    return fibonacci(n - 1) + fibonacci(n - 2)
    #                            | build-up |

# --- --- --- test cases --- --- ---


