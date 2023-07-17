class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0

        def count_pairs(sorted1, sorted2): #big to small
            nonlocal count
            sorted1 = deque(sorted1)
            sorted2 = deque(sorted2)

            while sorted1 and sorted2:
                if sorted1[0] - sorted2[0] <= diff:
                    sorted2.popleft()
                    count += len(sorted1)
                else:
                    sorted1.popleft()
            
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            halfway = len(nums)//2
            left = merge_sort(nums[:halfway])
            right = merge_sort(nums[halfway:])

            merged = merge(left, right)
            return merged
        
        def merge(sorted1, sorted2):
            count_pairs(sorted1, sorted2)
            sorted1 = deque(sorted1)
            sorted2 = deque(sorted2)
            merged = []

            while sorted1 and sorted2:
                if sorted1[0] > sorted2[0]:
                    merged.append(sorted1.popleft())
                else:
                    merged.append(sorted2.popleft())
            merged.extend(list(sorted1))
            merged.extend(list(sorted2))

            return merged
        
        one_minus_twos = []
        for i in range(len(nums1)):
            one = nums1[i]
            two = nums2[i]
            one_minus_twos.append(one-two)
        
        merge_sort(one_minus_twos)
        return count


            

