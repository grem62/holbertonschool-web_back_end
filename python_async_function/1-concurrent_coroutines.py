#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Asynchronously collects and returns a sorted list of random delays.

    :param n: The number of delays to collect (default is 0).
    :param max_delay: The maximum value for
    random delay generation (default is 10).
    :return: A sorted list of randomly generated delays.
    """

    delays = []

    async def collect_delays():
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*(collect_delays() for i in range(n)))

    return sorted(delays)
