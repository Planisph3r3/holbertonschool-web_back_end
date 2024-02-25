#!/usr/bin/env python3
"""
Working with async functions
"""

import asyncio
import random
import typing


async def wait_random(max_delay: int = 10) -> float:
    """
    An async coroutine that takes an integer as a argument
    that it would be the max range for the random module, being
    this value the delay until the value is returned
    """
    
    waiter = random.uniform(0, max_delay)
    await asyncio.sleep(waiter)
    return waiter
