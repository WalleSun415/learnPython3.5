import threading
import asyncio


@asyncio.coroutine
def hello():
    print("Hello world! (%s)" % threading.current_thread())
    yield from asyncio.sleep(1)
    print("Hello again! (%s)" % threading.current_thread())

loop = asyncio.get_event_loop()
task = [hello(), hello()]
loop.run_until_complete(asyncio.wait(task))
loop.close()
