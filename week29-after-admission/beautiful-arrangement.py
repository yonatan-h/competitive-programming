class Solution:
    def countArrangement(self, n: int) -> int:

        num_beautifuls = 0
        def explore(used, i):
            nonlocal num_beautifuls
            if i > n:
                num_beautifuls += 1
                return

            for num in range(1, n+1):
                if 1<<num & used != 0:
                    continue
                if num % i == 0 or i % num == 0:
                    new_used = used | 1<<num
                    explore(new_used, i+1)

        explore(0, 1)
        return num_beautifuls
                
                