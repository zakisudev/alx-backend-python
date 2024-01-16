#!/usr/bin/env python3
"""
2-measure_runtime.py
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the execution time of four calls to the async_comprehension
    function using asyncio.gather.

    Returns:
        float: The total execution time in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return (end - start)
