# tests/test_core.py

import unittest
from sunny_order_splitter.core import SunnyOrderSplitter

class TestSunnyOrderSplitter(unittest.TestCase):
    def test_split_order(self):
        platform = "BINANCE"
        base_url = "https://api.binance.com"
        #base_url = "https://testnet.binance.vision"  # Testnet base URL
        # Mock API keys for testing
        api_key = "Q9TdT7Tl9KaoFBWaxJ6Rlt8N4fEurKYeBsYfUhXgTRSFMZWzbWa14kybz5vLebCk"
        secret_key = "9UJ7Vx3SZRF6mvmmLGksR08UMChTiWZG3fyA4JdsyK4pWKsnuqXQwk7N3q8mBw43"
        symbol = 'BTCUSDT'
        bos = SunnyOrderSplitter(platform, symbol, api_key, secret_key)
        
        # Call split_order method with test parameters
        """
        params = {
            "side": "BUY",
            "orderAmount": 20,
            "totalAmount": 85,
            "interval": 5
        }
        """
        params = {
            "side": "SELL",
            "orderAmount": 1000,
            "totalAmount": 4100,
            "interval": 5
        }
        
        #bos.split_order(params)  # Use 1 second interval for testing

if __name__ == "__main__":
    unittest.main()
