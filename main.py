import aiohttp
import time
import asyncio
import json
from pathlib import Path


def load_json(config_path):
    config_file = Path(config_path)
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
        urls = config.get("urls", [])
        check_interval = config.get("check_interval")
        return urls, check_interval
    return []


async def fetch(session, url):
    start = time.time()
    try:
        async with session.get(url, timeout=5) as response:
            status = response.status
            await response.read()
            elapsed = time.time() - start
            return url, status, elapsed
    except Exception as e:
        elapsed = time.time() - start
        return url, None, f"Ошибка: {e}"


async def check_websites(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results


async def periodic_monitor():
    urls, check_interval = load_json("config.json")
    while True:
        print(f"\nПроверка сайтов (интервал {check_interval} сек):")
        results = await check_websites(urls)
        for url, status, elapsed in results:
            if status is None:
                print(f"{url}: {elapsed}")
            else:
                print(f"{url}: Статус {status}, время {elapsed:.2f} сек")
        print("-" * 40)
        await asyncio.sleep(check_interval)


async def main():
    # Раскомментируй одну из опций ниже:
    # 1. Однократная проверка:

    # Рабочее название read_json
    # read_json = load_json("config.json")
    # urls = read_json[0]
    # results = await check_websites(urls)
    # for url, status, elapsed in results:
    #     if status is None:
    #         print(f"{url}: {elapsed}")
    #     else:
    #         print(f"{url}: Статус {status}, время {elapsed:.2f} сек")

    # 2. Периодический мониторинг (каждые 60 сек):
    await periodic_monitor()


if __name__ == "__main__":
    asyncio.run(main())
