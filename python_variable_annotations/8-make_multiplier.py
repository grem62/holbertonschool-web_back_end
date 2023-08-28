#!/usr/bin/env python3
"""
 Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    "make mutliplier"
    def multiplier_funtcion(x: float) -> float:
        "make function mutliplier"
        return x * multiplier
    "return the result"
    return multiplier_funtcion
