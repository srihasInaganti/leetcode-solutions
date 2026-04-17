# Approach: Monotonic decreasing stack storing (price, span)
# Time Complexity: Amortized O(1) per call
# Space Complexity: O(n)
# Edge Cases: Strictly decreasing prices, strictly increasing prices

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span
