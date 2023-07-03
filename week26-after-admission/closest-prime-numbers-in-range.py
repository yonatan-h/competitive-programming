class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_primes = [True]*(right+1)
        is_primes[0] = is_primes[1] = False

        best_pair = [-float('inf'), float('inf')]
        cur_prime = -float('inf')

        for i in range(2, len(is_primes)):
           
            if not is_primes[i]: continue

            if left <= i <= right:
                if i-cur_prime < best_pair[1] - best_pair[0]:
                    best_pair = [cur_prime, i]
                cur_prime = i
                 
            for multiple in range(i, len(is_primes), i):
                is_primes[multiple] = False
                
        if best_pair[0] == -float('inf'):
            return [-1,-1]
        else:
            return best_pair

            