import unittest

def determine_buy_and_sell(filename: str) -> str:
    max_price, min_price = -float('inf'), float('inf')
    max_profit = -float('inf')
    filename = 'q2.txt'
    stock_prices = get_stock_prices_from_file(filename)
    for stock_price in stock_prices:
        min_price = min(stock_price, min_price) 
        if max_profit < stock_price - min_price:
            max_price, max_profit = stock_price, stock_price - min_price
    return f"buy {min_price}, sell {max_price}"

def get_stock_prices_from_file(filename: str) -> list[int]:
    with open(filename) as f:
        stock_prices = list(map(int, f.read().split()))
        return stock_prices

class TestQuestion2(unittest.TestCase):
    def test_determine_buy_and_sell(self):
        filename = 'q2.txt'
        expected = 'buy 51, sell 115'
        achieved = determine_buy_and_sell(filename)
        self.assertEqual(expected, achieved)

if __name__ == "__main__":
    unittest.main()
