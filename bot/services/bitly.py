import aiohttp

import os
from dotenv import load_dotenv

env_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

load_dotenv(dotenv_path=env_file_path)

BITLY_TOKEN: str = os.getenv('BITLY_TOKEN')


async def get_short_link(long_url, bitly_token=BITLY_TOKEN) -> str:

    api_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {bitly_token}",
        "Content-Type": "application/json"
    }
    data = {
        'long_url': long_url
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                return result.get('link')
            else:
                return long_url
