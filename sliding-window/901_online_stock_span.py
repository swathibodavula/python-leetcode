class StockSpanner:
    """A class to calculate the span of a stock's price for each day.
    The span of the stock's price on a given day is defined as the maximum number of consecutive days (starting from that day and going backwards) for which the price of the stock was less than or equal to its price on that day.
    Arguments:
        price: Integer representing the stock's price on a given day.
    Returns:
        Integer representing the span of the stock's price on that day.
    """
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span +=self.stack.pop()[1]
        self.stack.append((price, span))
        return span

if __name__ == "__main__":
    stockSpanner = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    spans = [stockSpanner.next(price) for price in prices]
    print(spans)  # Output: [1, 1, 1,

    # let's test with another set of prices
    stockSpanner2 = StockSpanner()
    prices2 = [31, 41, 48, 59, 79]
    spans2 = [stockSpanner2.next(price) for price in prices2]
    print(spans2)  # Output: [1, 2, 3,

    # let's test with a decreasing set of prices
    stockSpanner3 = StockSpanner()
    prices3 = [100, 90, 80, 70, 60]
    spans3 = [stockSpanner3.next(price) for price in prices3]
    print(spans3)  # Output: [1, 1, 1,

    # let's test with a single price
    stockSpanner4 = StockSpanner()
    prices4 = [50]
    spans4 = [stockSpanner4.next(price) for price in prices4]
    print(spans4)  # Output: [1]