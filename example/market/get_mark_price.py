from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

# request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

# result = request_client.get_mark_price(symbol="BTCUSDT")

# print("======= Mark Price =======")
# PrintBasic.print_obj(result)
# print("==========================")

def _print_obj(obj):
    price = None
    if not obj:
        return -1

    members = [attr for attr in dir(obj) if not callable(attr) and not attr.startswith("__")]
    for member_def in members:
        val_str = str(getattr(obj, member_def))
        if member_def == 'markPrice':
            print(member_def + ":" + val_str)
            price = val_str
            break
    return price

def get_ETH_price:
    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
    result = request_client.get_mark_price(symbol="ETHUSDT")
    return float(_print_obj(result))