#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""

import asyncio
import random
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    "return 4 parrallel coroutine"

    first_time = time.time()
    tasks = [async_comprehension() for i in range(4)]
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    time_total = end_time - first_time
    return time_total
