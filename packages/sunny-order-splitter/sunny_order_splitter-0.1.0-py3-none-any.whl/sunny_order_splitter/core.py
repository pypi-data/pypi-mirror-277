
from binance.spot import Spot
import time

class SunnyOrderSplitter:
    def __init__(self, api_key, secret_key):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret_key,
            'enableRateLimit': True,
        })

    def place_order(self, symbol, amount):
        """
        在 Binance 上下单购买指定数量的代币
        """
        try:
            order = self.exchange.create_market_buy_order(symbol, amount)
            print(f"Order placed: {order}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def split_order(self, symbol, total_amount, order_amount, interval):
        """
        将总金额拆分成多笔订单并按指定间隔下单
        """
        num_orders = total_amount // order_amount
        for i in range(num_orders):
            print(f"Placing order {i + 1} of {num_orders}")
            self.place_order(symbol, order_amount)
            if i < num_orders - 1:  # 最后一次下单后不需要等待
                time.sleep(interval)

# sunny_order_splitter/__init__.py

from .core import Sunny
