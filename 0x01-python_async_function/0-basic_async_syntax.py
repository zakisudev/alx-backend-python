#!/usr/bin/env python3
# 0-basic_async_syntax.py

""" Aysynchronous function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async function that returns a random float between 0 and max_delay
    Args:
        max_delay: int
    Returns: float
    """
    await asyncio.sleep(1)
    return random.random() * max_delay
