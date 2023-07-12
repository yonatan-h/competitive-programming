class Solution:
    def reversePairs(self, nums: List[int]) -> int:
    
        count = 0

        def merge_sort(nums):
            if len(nums) <= 1:
                return nums

            half_way = len(nums)//2
            first_half = merge_sort(nums[:half_way])
            second_half = merge_sort(nums[half_way:])

            merged = merge(first_half, second_half)
            count_reverse_pairs(first_half, second_half)
            return merged
        
        def count_reverse_pairs(nums1, nums2):
            nonlocal count
            nums1 = deque(nums1)
            nums2 = deque(nums2)
            
            while nums1 and nums2:
                if nums1[0] > 2*nums2[0]:
                    count += len(nums2) 
                    nums1.popleft()
                else:
                    nums2.popleft()

        
        def merge(nums1, nums2):
            nums1 = deque(nums1)
            nums2 = deque(nums2)
            merged = []

            while nums1 and nums2:
                num1 = nums1[0]
                num2 = nums2[0]

                if num1 >= num2:
                    merged.append(nums1.popleft())
                else:
                    merged.append(nums2.popleft())


            merged.extend(list(nums1))
            merged.extend(list(nums2))
                
            return merged
        
        print(merge_sort(nums)) 
            
        return count
                    

