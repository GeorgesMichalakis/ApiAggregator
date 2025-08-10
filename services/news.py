from typing import List
import aiohttp

API_KEY = "9a3593f5d2744f1389e76d825cd0b296"
BASE_URL = "https://newsapi.org/v2/everything"
async def get_country_news(keyword: str) -> List[str]:
    """
    Fetch the current top headlines for a keyword from newsapi.

    Args:
        keyword (str): The name of the country.

    Returns:
        list[str]: List of headline titles
    """

    params = {
        "q": keyword,
        "apiKey": API_KEY
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(BASE_URL, params=params) as resp:
                if resp.status != 200:
                    print(await resp.text(encoding='utf-8'))  # debug the error message
                    raise ValueError(f"API request failed with status {resp.status}")
                data = await resp.json()
                titles = [article['title'] for article in data['articles'] if article.get('title')]
                if not titles:
                    return ["No news found."]
                return titles
            
    except aiohttp.ClientError as e:
        raise ConnectionError(f"Network error: {e}")
    except KeyError:
        raise ValueError("Unexpected API response format")