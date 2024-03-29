#!/usr/bin/env python3
"""
Working with async functions
"""


import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async
    comprehension over async_generator,
    then returns the 10 random numbers.
    """
    return [val async for val in async_generator()]
