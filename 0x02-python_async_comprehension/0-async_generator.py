#!/usr/bin/env python3
'''
Asynchronously generates random floats between 0 and 10.
'''

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Asynchronously generates random floats between 0 and 10.'''
    for _ in range(10):
        # Sleep for 1 second
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10
        yield uniform(0, 10)
