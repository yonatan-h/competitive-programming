class Solution:
    def shipWithinDays(self, weights: List[int], target_days: int) -> int:
        min_capacity = max(weights)
        max_capacity = sum(weights)

        prefix_weights = [0]
        for weight in weights:
            prefix_weights.append(prefix_weights[-1] + weight)


        return find_best(min_capacity, max_capacity, target_days, prefix_weights)



def find_best(min_capacity, max_capacity, target_days, prefix_weights):

    smaller = min_capacity-1
    bigger = max_capacity
    
    while smaller + 1 < bigger:
        mid = (smaller+ bigger)//2
        least_days = find_least_days(prefix_weights, mid)

        if least_days <= target_days:
            bigger = mid
        else:
            smaller = mid

    return bigger
        



def find_least_days(prefix_weights, capacity):
    before_sum = 0
    day_count = 0

    for i in range(1, len(prefix_weights)):
        prefix_weight = prefix_weights[i]
        prev_prefix = prefix_weights[i-1]

        over_flow = prefix_weight - before_sum > capacity

        if over_flow:
            before_sum = prev_prefix
            day_count += 1

    if prefix_weights[-1] > before_sum:
        day_count += 1

    return day_count



