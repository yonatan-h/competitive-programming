class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product = 1
        for num in nums: product *= num
        
        return len_prime_factors(product)


def len_prime_factors(num):
    prime_factors = set()

    for factor in range(2, num+1):
        if num%factor == 0:
            prime_factors.add(factor)

        while num%factor == 0:
            num //= factor
        
        if num == 1:
            break

    return len(prime_factors)
    
