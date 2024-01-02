import requests

CRYPTO_API_URL = "https://min-api.cryptocompare.com/data/pricemultifull"


def get_crypto_prices():
    params = {
        'fsyms': 'BTC,ETH,BNB,USDT,SOL,DOGE',
        'tsyms': 'USD,EUR,UAH',
    }

    response = requests.get(CRYPTO_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return process_crypto_data(data)
    else:
        return []


def process_crypto_data(data):
    data_raw = data.get('RAW', {})
    crypto_coins_list = []

    for key, value in data_raw.items():
        crypto_coin = {
            'name': key,
            'prices': {}
        }

        for currency_code, currency_data in value.items():
            price = currency_data.get('PRICE')
            image_url = currency_data.get('IMAGEURL')

            if price is not None:
                crypto_coin['prices'][currency_code] = {
                    'price': price,
                    'image_url': f'https://www.cryptocompare.com/{image_url}',
                }

        crypto_coins_list.append(crypto_coin)

    return crypto_coins_list
