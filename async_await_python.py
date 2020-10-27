import asyncio
import random
import time

async def coroutine_task_a():
    tasks = []
    for iteraction in range(100):
        tasks.append(asyncio.create_task(coroutine_task(iteraction)))
    await asyncio.gather(*tasks)


async def coroutine_task(iteraction):    
    process_time = random.randint(1,5)
    await asyncio.sleep(process_time)
    print(f'Iteration {iteraction}')

def main():
    asyncio.run(coroutine_task_a())

if __name__ == '__main__':
    main()
