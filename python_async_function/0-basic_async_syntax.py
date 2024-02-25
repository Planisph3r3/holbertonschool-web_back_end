#!/usr/bin/env python3
"""
Working with async functions
"""

import asyncio
import random
import typing


async def wait_random(max_delay: int = 10) -> float:
    waiter = random.uniform(0, max_delay)
    await asyncio.sleep(waiter)
    return waiter
