from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import pandas as pd

"""
{
    "accountAlias": "SgsR",    // unique account code
    "asset": "USDT",
    "balance": "122607.35137903",
    "withdrawAvailable": "102333.54137903"
}
"""

def get_balance():
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_balance()
    # PrintMix.print_data(result)
    return result

def get_balanceAvailableUSDT():
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_balance()
    acc_df = pd.DataFrame([acc.__dict__ for acc in result])
    return acc_df.withdrawAvailable[0]