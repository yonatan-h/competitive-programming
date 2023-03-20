class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        sum_nums = sum(nums)

        smallest = 0
        biggest = max(nums)+1

        return best_divider(smallest, biggest, nums, threshold)


def best_divider(small_div, big_div, nums, threshold):
    left = small_div 
    right = big_div #lands on less sum or best sum

    #from big-sum to perf-sum to tiny-sum
    #from bad to good

    while left + 1 < right:
        mid = (left + right)//2

        is_good = divide_n_sum(nums, mid) <= threshold
        if is_good:
            right = mid
        else:
            left = mid
    
    return right



def divide_n_sum(nums, divider):
    sum_divided = 0
    for num in nums:
        sum_divided += math.ceil(num/divider)
    return sum_divided


#14sub

