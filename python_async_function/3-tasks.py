#!/usr/bin/env python3
"""
Working with async functions
"""

import asyncio
import typing

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task[float]:
    """A function that takes an integer max_delay and returns a asyncio.Task"""
    task1: asyncio.Task[float] = asyncio.create_task(wait_random(max_delay))
    return task1
