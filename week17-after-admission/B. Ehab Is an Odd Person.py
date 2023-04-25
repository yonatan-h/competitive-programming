length = int(input())
nums = list(map(int, input().split()))

has_odd = False
has_even = False

for num in nums:
    is_even = num % 2 == 0
    has_odd = has_odd or (not is_even)
    has_even = has_even or is_even

if has_odd and has_even:
    print(* sorted(nums))
else:
    print(*nums)