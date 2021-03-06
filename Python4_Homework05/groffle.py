#!/bin/env python
# -*- coding: utf-8 -*-

""" 
Program for optimization. Python 4, Lesson 5. 
Calculates the groffle speed of a knurl widget 
of average density given by user input. 
""" 

from math import log 
from timeit import Timer 

def groffle_slow(mass, density):
    total = 0.0 
    for i in range(10000): 
        masslog = log(mass * density) 
        total += masslog/(i+1)
    return total

def groffle_fast(mass, density):
    masslog = log(mass * density)
    total = masslog * sum(list(1/i for i in range(1, 10001)))
    return total

mass = 2.5
density = 12.0

"Compare executing time"
timer = Timer("total = groffle_slow(mass, density)", "from __main__ import groffle_slow, mass, density") 
print("[groffle_slow] time:", timer.timeit(number=1000), " result:", groffle_slow(mass, density))
timer = Timer("total = groffle_fast(mass, density)", "from __main__ import groffle_fast, mass, density") 
print("[groffle_fast] time:", timer.timeit(number=1000), " result:", groffle_fast(mass, density))

"Check answers"
print("Result error: ", abs(groffle_fast(mass, density) - groffle_slow(mass, density)))
