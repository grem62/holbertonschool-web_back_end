#!/usr/bin/env python3
""" Basic syntax await async """

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
    mesure the time of the function wait_n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    end_time = time.perf_counter() - start_time
    total_time = end_time / n

    return total_time
