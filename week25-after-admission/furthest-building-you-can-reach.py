class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        costs = [0]
        for i in range(len(heights)-1):
            change = heights[i+1] - heights[i]
            if change >= 0:
                costs.append(change)    
            else:
                costs.append(0)

        payment_heap = [0]

        i = 0
        while i < len(costs) and (ladders>0 or bricks>=costs[i]):
            cost = costs[i]
            if bricks >= cost:
                bricks -= cost
                heappush(payment_heap, -cost)
                i += 1
            else:
                ladders -= 1
                recycled = heappop(payment_heap) * -1
                if recycled < cost:
                    heappush(payment_heap, -1*recycled)
                    i+=1
                else:
                    bricks += recycled
                    heappush(payment_heap, 0)

            
        
        return i-1