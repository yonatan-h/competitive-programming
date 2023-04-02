class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        range_ = set(list(range(1,len(nums)+1)))
        appeared = set(nums)

        in_range_appeared = appeared.intersection(range_)
        missing = range_ - in_range_appeared
        return list(missing)

