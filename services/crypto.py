import aiohttp

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"
async def get_crypto_price(crypto_id: str) -> float:
    """
    Fetch the current price of a cryptocurrency in USD from CoinGecko.

    Args:
        crypto_id (str): The name of the crypto.

    Returns:
        float: The price of the crypto in US dollars
    """

    params = {
        "ids": crypto_id,
        "vs_currencies": "usd"
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(BASE_URL, params=params) as resp:
                if resp.status != 200:
                    print(await resp.text())  # debug the error message
                    raise ValueError(f"API request failed with status {resp.status}")
                data = await resp.json()
                return data[crypto_id]["usd"]

    except aiohttp.ClientError as e:
        raise ConnectionError(f"Network error: {e}")
    except KeyError:
        raise ValueError("Unexpected API response format")