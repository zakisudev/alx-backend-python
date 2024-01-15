#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spwans wait_random n times with the specified max_delay
    Args:
        n: number of times to spawn wait_random
        max_delay: the maximum delay to pass to wait_random
    Returns:
        A list of all the delays (float values) in ascending order
    """

    sorted_list: list[float] = []

    async def randsleep(max_delay: int, sorted_list: list[float]) -> None:
        sleep: float = await wait_random(max_delay)
        await asyncio.sleep(sleep)
        sorted_list.append(sleep)

    await asyncio.gather(*(randsleep(max_delay,
                                     sorted_list) for _ in range(n)))
    return sorted_list
