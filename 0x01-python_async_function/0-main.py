#!/usr/bin/env python3

import asyncio
import time
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay


async def fetch_data(id, delay_time):
    print(f"fetching data from the web for id: {id}")
    await asyncio.sleep(delay_time)
    return delay_time

async def main():
    tasks = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 5))
    
    task1 = await asyncio.create_task(fetch_data(1, 2))
    task2 = await asyncio.create_task(fetch_data(2, 1))
    task3 = await asyncio.create_task(fetch_data(3, 5))
    
    print(f"Task 1: {task1}, Task 2: {task2}, Task 3: {task3}")
    print(f"Recieved results: {tasks}")

asyncio.run(main())

#!/usr/bin/env python3
# chained.py

import asyncio
import random
import time

async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result

async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    return result

async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")
