#!/usr/bin/env python
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""


def factorial(n):
    prod = 1
    for i in range(n):
        prod = prod * (n - i)
    return prod


def test_factorial():
    assert factorial(1) == 1
    assert factorial(4) == 24
    assert factorial(0) == 1


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. pytest) as a library, we should not run code
    # below
    nconditions = input("Please enter number of conditions: ")
    norders = factorial(int(nconditions))
    print("Number of possible trial orders: " + str(norders))
