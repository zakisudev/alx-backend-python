#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
