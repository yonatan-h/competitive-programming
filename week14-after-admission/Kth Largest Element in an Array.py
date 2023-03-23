class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums)-k
        quick_sort(0, len(nums)-1, nums, index)
        return nums[index]

def partition(left, right, nums):
    #portion length should be >= 2
    pivot = nums[left]

    write = left+1
    for read in range(write, right+1):
        if nums[read] <= pivot:
            nums[read], nums[write] = nums[write], nums[read]
            write += 1
    
    #write is in >= pivot
    pivot_index = write - 1
    nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
    return pivot_index


def quick_sort(left, right, nums, index):
    print(left, right)
    if right - left <= 0:
        return

    pivot_index = partition(left, right, nums)

    if index < pivot_index:
        quick_sort(left, pivot_index-1, nums, index)
    else:
        quick_sort(pivot_index+1, right, nums, index)
