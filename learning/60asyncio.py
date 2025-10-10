# 158. Explain Python’s asyncio.
#
# Framework for asynchronous (non-blocking) programming using async and await.

# 159. How is async different from threading?
#
# Async → single-threaded, cooperative scheduling.
#
# Threading → pre-emptive, true concurrency for I/O.
# Async is lightweight & ideal for APIs / network calls.

import asyncio
async def task():
    print("Task running")
    await asyncio.sleep(1)