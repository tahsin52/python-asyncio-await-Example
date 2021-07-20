from aiohttp import ClientSession
import asyncio
import pathlib

async def fetch(url, session, year):
    async with session.get(url) as response:
        html_body = await response.read()
        return {'body': html_body, 'year': year}


async def fetch_with_semaphore(semaphore, url, session, year=None):
    async with semaphore:
        return await fetch(url, session, year)

async def main(start_year=2021, years_ago=5):
    html_body = ""
    tasks = []
    """
    SEMAPHORE is actually going to prevent just crushing their server 
    which is absolutely something we dont to do for several reasons
    """
    sem = asyncio.Semaphore(10)

    async with ClientSession() as session:
        for i in range(0, years_ago):
            year = start_year - i
            print("year", year)
            url = f'https://www.boxofficemojo.com/year/{year}/'
            tasks.append(
                asyncio.create_task(
                    fetch_with_semaphore(sem, url, session, year)
                )
            )

        pages_content = asyncio.gather(*tasks) # [{'body': '...data', 'year': 2021}]
        return await pages_content

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
results = asyncio.run(main())
output_dir = pathlib.Path().resolve() / "snapshots"
output_dir.mkdir(parents=True, exist_ok=True)

for result in results:
    current_year = result.get('year')
    html_data = result.get('body')
    output_file = output_dir / f"{current_year}.html"
    output_file.write_text(html_data.decode())
