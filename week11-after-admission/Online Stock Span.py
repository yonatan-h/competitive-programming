class StockSpanner:

    def __init__(self):
        #not price only but (price, popped) pair
        self.stack = []
        

    def next(self, price: int) -> int:
        popped = 0
        while self.stack and self.stack[-1][0]<=price:
            popped += 1
            popped += self.stack.pop()[1]

        price_popped_pair = (price, popped)
        self.stack.append(price_popped_pair)

        return popped+1

            
#40min
#1sub