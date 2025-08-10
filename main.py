import asyncio
from services.crypto import get_crypto_price
from services.news import get_country_news

async def main():
    crypto_id = "bitcoin"

    value_task = asyncio.create_task(get_crypto_price(crypto_id))
    news_task = asyncio.create_task(get_country_news(crypto_id))
    
    value, news = await asyncio.gather(value_task, news_task)
    
    print(f"The value of {crypto_id} against USD is ${value}")
    print(f"Top news headlines for {crypto_id}:")
    for i, headline in enumerate(news, start=1):
        print(f"{i}. {headline}")

if __name__ == "__main__":
    asyncio.run(main())
