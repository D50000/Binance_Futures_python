from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

""" 
the structure of Position 
        self.entryPrice = 0.0
        self.isAutoAddMargin = False
        self.leverage = 0.0
        self.maxNotionalValue = 0.0
        self.liquidationPrice = 0.0
        self.markPrice = 0.0
        self.positionAmt = 0.0
        self.symbol = ""
        self.unrealizedProfit = 0.0
        self.marginType = ""
        self.isolatedMargin = 0.0
        self.positionSide = ""
"""

def get_position():
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_position()
    # PrintMix.print_data(result)
    return result