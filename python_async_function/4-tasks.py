#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n. The code is 
nearly identical to wait_n except task_wait_random is being called.
"""

import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    "return all async "

    delays = []

    async def collect_delays():
        delay = await task_wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*(collect_delays() for i in range(n)))

    return sorted(delays)
