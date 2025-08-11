import asyncio
import time

async def fetch_url(url):
    await asyncio.sleep(1)
    return f"Data from {url}"

async def main():
    urls = ["first", "second", "third", "fourth", "fifth"]

    start = time.perf_counter()
    results = await asyncio.gather(*(fetch_url(url) for url in urls))
    end = time.perf_counter()

    print(results)
    print(f"Выполнилось за: {end - start:.4f} секунд")
                                

if __name__ == "__main__":
    asyncio.run(main())