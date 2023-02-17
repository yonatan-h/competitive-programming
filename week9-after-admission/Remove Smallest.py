def main():
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        length = int(input())
        nums = list(map(int, input().split()))
        is_reducable = can_be_reduced(nums)

        if is_reducable: print("YES")
        else: print("NO")

def can_be_reduced(nums):
    nums.sort()

    for i in range(len(nums)-1):
        if abs(nums[i] - nums[i+1]) > 1:
            return False
    return True

main()

#10min
#1sub