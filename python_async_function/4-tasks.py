#!/usr/bin/env python3
"""
Working with async functions
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    A async routine called task_wait_n
    that takes in 2 int arguments: n and max_delay.
    Will return the list of all the delays
    """
    tasks: List = []
    wait_time: List[float] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        wtime = await task
        wait_time.append(wtime)

    return wait_time
