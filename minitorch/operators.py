"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

def mul(a, b):
    return a * b

def id(a):
    return a

def add(a, b):
    return a + b

def neg(a):
    return float(-a)

def lt(a, b):
    return float(a < b)

def eq(a, b):
    return float(a == b)

def max(a, b):
    if a > b:
        return a 
    else:
        return b

def is_close(a, b, eps=1e-2):
    return 1.0 if abs(a-b) < eps else 0.0

def sigmoid(a):
    if a >= 0:
        return 1 / (1 + math.exp(-a))
    else:
        return exp(a) / (1.0 + exp(a))

def relu(a):
    return max(0.0, a)

def log(a):
    return math.log(a)

def exp(a):
    return math.exp(a)

def log_back(a, b):
    return b * (1 / a)

def inv(a):
    return 1 / a 

def inv_back(a, b):
    return -1.0 *  b * (1 / a**2)

def relu_back(a, b):
    if a > 0:
        return b 
    else:
        return 0.0
    
# new 

def map(func, lst):
    return [func(el) for el in lst]

def zipWith(func, lst1, lst2):
    return [func(el1, el2) for el1, el2 in zip(lst1, lst2)]

def reduce(func, lst, init):
    ans = init
    for el in lst:
        ans = func(el, ans)
    return ans

def negList(a):
    return map(neg, a)

def addLists(a, b):
    return zipWith(add, a, b)

def sum(a):
    return reduce(add, a, 0)
    
def prod(a):
    return reduce(mul, a, 1)




# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
