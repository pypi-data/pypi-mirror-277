
import logging
import math
import time
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError


config_logging(logging, logging.DEBUG)

class SunnyOrderSplitter:

    def __init__(self, platform, symbol, api_key, secret_key, base_url = 'https://api.binance.com'):
        
        self.client = Client(api_key, secret_key, base_url = base_url)
        self.symbol = symbol

        #构造币对相关的信息;
        response = self.get_exchange_info(symbol)
        #logging.info(response['symbols'][0])
        self.baseAsset = response['symbols'][0]['baseAsset']
        self.quoteAsset = response['symbols'][0]['quoteAsset']
        self.filters = response['symbols'][0]['filters']

    def get_exchange_info(self, symbol):
        """
        获取交易币对相关信息
        """
        try:
            response = self.client.exchange_info(symbol)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
            return None

    def place_order(self, params):
        """
        在 Binance 下单购买指定数量的代币
        """
        try:
          response = self.client.new_order(**params)
          logging.info(response)
        except ClientError as error:
          logging.error(
              "Found error. status: {}, error code: {}, error message: {}".format(
                  error.status_code, error.error_code, error.error_message
              )
          )

    """
    params = {
        "side": "SELL" || "BUY",
        "type": "MARKET",
        "timeInForce": "GTC",
        "quantity": // 计算数量
        "orderAmount": 1000, // 每笔订单的金额
        "totalAmount": 9500, // 总金额
        "interval": 5, // 下单间隔
    }
    """

    def split_order(self, params):
        """
        将总金额拆分成多笔订单并按指定间隔下单
        """
        timeInForce = "GTC"
        type = "MARKET" # 目前默认为市价单
        side = params['side']
        order_amount = params['orderAmount']
        total_amount = params['totalAmount']
        interval = params['interval']

        #检查余额是否充足
        if side == "BUY":
            if not self.check_balance(self.quoteAsset, total_amount):
                logging.error("Insufficient balance")
                return
        elif side == "SELL":
            if not self.check_balance(self.baseAsset, total_amount):
                logging.error("Insufficient balance")
                return

        #计算需要拆分的订单数量
        num_orders = math.ceil(total_amount / order_amount)
        for i in range(num_orders):
  
            current_order_amount = order_amount if (i < num_orders - 1) else total_amount - order_amount * (num_orders - 1)
            current_order_params = {
                "symbol": self.symbol,
                "side": side,
                "type": type,
            }

            if side == "BUY":
                current_order_params["quoteOrderQty"] = current_order_amount
            elif side == "SELL":
                current_order_params["quantity"] = current_order_amount

            self.place_order(current_order_params)

            if i < num_orders - 1:  # 最后一次下单后不需要等待
                time.sleep(interval)

    def check_balance(self, asset, amount):
        """
        检查指定资产的余额
        """
        try:
            response = self.client.user_asset(asset=asset)
            logging.info(response)
            return float(response[0]['free']) >= amount
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
        return False
    
# sunny_order_splitter/__init__.py

