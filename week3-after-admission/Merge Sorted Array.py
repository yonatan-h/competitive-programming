class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merge_sorted(nums1,m, nums2,n)

def merge_sorted(big_list, big_length, small_list, small_length):

    max_big_ptr = big_length-1
    max_small_ptr = small_length - 1
    insertor = len(big_list) - 1

    while max_big_ptr >= 0 and max_small_ptr >= 0:
        max_big = big_list[max_big_ptr]
        max_small = small_list[max_small_ptr]

        if max_big > max_small:
            big_list[insertor] = max_big
            max_big_ptr -= 1
            insertor -= 1
        else:
            big_list[insertor] = max_small
            max_small_ptr -= 1
            insertor -= 1
    
    #if elements left in big list: pass

    #elements left in small list
    if max_small_ptr >= 0:
        for i in range(max_small_ptr + 1):
            big_list[i] = small_list[i]

    #if niether: pass


#15min
#2sub