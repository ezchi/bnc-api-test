# from binance.spot import Spot

import os

# client = Spot()
# print(client.time())

API_KEY=os.environ.get("BINANCE_TEST_API_KEY")
API_SECRET=os.environ.get("BINANCE_TEST_API_SECRET")


# client = Spot(key=API_KEY, secret=API_SECRET)

# # Get account information
# print(client.account())

# # Post a new order
# params = {
#     'symbol': 'BTCUSDT',
#     'side': 'SELL',
#     'type': 'LIMIT',
#     'timeInForce': 'GTC',
#     'quantity': 0.002,
#     'price': 9500
# }

# response = client.new_order(**params)
# print(response)

from binance.spot import Spot as Client

def get_asset(symbol, balances):
    for asset in balances:
        if asset["asset"] == symbol:
            return asset

def get_fund(asset):
    return float(asset["free"])


client = Client(key=API_KEY, secret=API_SECRET, base_url='https://testnet.binance.vision')
print(client.time())
# print(client.__dict__)

account = client.account()
print(account["balances"])
usdt = get_fund(get_asset("USDT", account["balances"]))
print("USDT = ", usdt)

vol = 0.002
price = 46100

# Post a new order
params = {
    'symbol': 'BTCUSDT',
    'side': 'SELL',
    'type': 'LIMIT',
    'timeInForce': 'GTC',
    'quantity': vol,
    'price': price
}

response = client.new_order(**params)
print(response)

account = client.account()
print(account["balances"])
usdt1 = get_fund(get_asset("USDT", account["balances"]))
print("USDT = ", usdt1)
print("Profit = ", usdt1 - usdt)
print((usdt1 - usdt) / vol, ", ", price)
