// Asynchronous commucation of the application with the Models

# /modules/data_processor.py
import aiohttp
from config.settings import API_TIMEOUT

async def fetch_data(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=API_TIMEOUT) as response:
            return await response.text()
