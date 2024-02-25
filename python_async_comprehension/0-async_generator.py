#!/usr/bin/env python3
"""
Working with async functions
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Funtion that loops 10 times.
    Each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """

    for val in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
