import asyncio
import time
import random

def fetch(guid: int):
    print("going to sleep " + str(guid))

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.sleep(2))

    print("coming out of sleep" + str(guid))

def process(guid: int):
    print("calling f " + str(guid))
    fetch(guid)
    # None uses the default executor (ThreadPoolExecutor)
    #predict_result = await loop.run_in_executor(None, HANDLER.process, input_data, CONTEXT)
    print("finished f " + str(guid))
    return True

async def evaluate(guid: int):
    loop = asyncio.get_event_loop()
    # None uses the default executor (ThreadPoolExecutor)\
    print("Starting " + str(guid))
    predict_result = await loop.run_in_executor(None, process, guid)
    print("Finished " + str(guid))


async def main():
    await asyncio.gather(*(evaluate(n) for n in range(0,10)))

if __name__ == "__main__":
    random.seed(444)
    start = time.perf_counter()
    loop = asyncio.get_event_loop().run_until_complete(main())
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")

