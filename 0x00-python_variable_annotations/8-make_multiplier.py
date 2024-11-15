#!/usr/bin/env python3
""" complex types - list of floats """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier. """
    
    def f(n: float) -> float:
        return n * multiplier

    return f