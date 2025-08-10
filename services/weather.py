import aiohttp

API_KEY = "b7f83d122a24937478d95fecfc9bfdc7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
async def get_weather(city: str) -> float:
    """
    Fetch the current temperature for a given city from the weather API.
    
    Args:
        city (str): The name of the city.

    Returns:
        float: The temperature in Celsius.
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(BASE_URL, params=params) as resp:
                if resp.status != 200:
                    print(await resp.text())  # debug the error message
                    raise ValueError(f"API request failed with status {resp.status}")
                data = await resp.json()
                return data["main"]["temp"]

    except aiohttp.ClientError as e:
        raise ConnectionError(f"Network error: {e}")
    except KeyError:
        raise ValueError("Unexpected API response format")