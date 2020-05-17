from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

# api detail:
# https://binance-docs.github.io/apidocs/futures/en/#new-order-trade
# Mandatory: symbol, side, quantity, timestamp
# {    Make Order example
#     "orderId":1740810387,
#     "symbol":"ETHUSDT",
#     "status":"NEW",
#     "clientOrderId":"9yW9Xq5RR7rheRiMoBoOS0",
#     "price":"0",
#     "avgPrice":"0.00000",
#     "origQty":"0.700",
#     "executedQty":"0",
#     "cumQty":"0",
#     "cumQuote":"0",
#     "timeInForce":"GTC",
#     "type":"MARKET",
#     "reduceOnly":false,
#     "closePosition":false,
#     "side":"SELL",
#     "positionSide":"BOTH",
#     "stopPrice":"0",
#     "workingType":"CONTRACT_PRICE",
#     "origType":"MARKET",
#     "updateTime":1589646615540
# }

def long_ETH(size):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.post_order(symbol="ETHUSDT", side=OrderSide.BUY, ordertype=OrderType.MARKET, quantity=size)
    # PrintBasic.print_obj(result)
    return result

def short_ETH(size):
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.post_order(symbol="ETHUSDT", side=OrderSide.SELL, ordertype=OrderType.MARKET, quantity=size)
    # PrintBasic.print_obj(result)
    return result
