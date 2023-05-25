class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        else:
            nums.sort()
            que = deque(nums)
            return best_move(que, 0)


            
def best_move(que, num_pops):
    if num_pops == 3:
        return abs(que[0] - que[-1])
    
    child_differences = []

    left = que.popleft()
    child_differences.append(best_move(que, num_pops+1))
    que.appendleft(left)

    right = que.pop()
    child_differences.append(best_move(que, num_pops+1))
    que.append(right)

    return min(child_differences)




    
    
