#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    task = asyncio.create_task(wait_random(max_delay))
    return task
