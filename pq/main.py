import asyncio
import aiohttp
from datetime import datetime
from random import randint



async def async_get_img_link(count: int) -> list[str]:
    url = "https://random.dog/woof.json"


    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(session.get(url)) for _ in range(count)
        ]

        responses = await asyncio.gather(*tasks)
        json_responses = [await resp.json() for resp in responses]
        img_urls = [item.get('url') for item in json_responses]
        return img_urls



async def async_save_images(urls: list[str]):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(session.get(url)) for url in urls
        ]

        responses = await asyncio.gather(*tasks)


        for i, response in enumerate(responses):
            img_data = await response.read()
            filename = f"dog{randint(1, 1000)}.jpg"
            with open(filename, 'wb') as f:
                f.write(img_data)
            print(f"Картинка сохранена как {filename}")



async def async_main():
    img_urls = await async_get_img_link(2)
    await async_save_images(img_urls)



if __name__ == "__main__":
    start = datetime.now()


    asyncio.run(async_main())

    print(f"Время исполнения: {datetime.now() - start}")
