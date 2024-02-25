#!/usr/bin/env python3
"""
Working with async functions
"""

import asyncio
import time
import typing

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    This function will measure the total
    runtime of the gather method.
    """

    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = time.time()
    return end_time - start_time
