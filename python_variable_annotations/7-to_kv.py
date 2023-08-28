#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return int or tuple(int, float)
    """
    return k, float(v ** 2)
