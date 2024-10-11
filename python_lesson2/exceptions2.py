import requests

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: An issue occurred with the request: {e}")
    finally:
        print("API request completed.")

api_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc'
result = fetch_data_from_api(api_url)

#Print the result if data is returned
for coin in result:
    print(f"Coin: {coin['name']}")
    print(f"Symbol: {coin['symbol']}")
    print(f"Current Price: {coin['current_price']}")
    print(f"Market Cap: {coin['market_cap']}")
    print(f"High 24h: {coin['high_24h']}")
    print(f"Low 24h: {coin['low_24h']}")
    print(f"Price Change (24h): {coin['price_change_percentage_24h']}%")
    print(f"Last Updated: {coin['last_updated']}")
    print("-" * 40)
                             
