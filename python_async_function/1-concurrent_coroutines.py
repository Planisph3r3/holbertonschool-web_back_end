#!/usr/bin/env python3
"""
Working with async functions
"""

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    A async routine called task_wait_n
    that takes in 2 int arguments: n and max_delay.
    Will return a sorted list with
    """
    tasks: List = []
    wait_time: List[float] = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        wtime = await task
        wait_time.append(wtime)

    return wait_time
