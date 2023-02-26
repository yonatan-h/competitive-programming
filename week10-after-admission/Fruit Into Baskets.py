class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)
        max_length = 0
        
        left = 0
        for right in range(len(fruits)):
            at_right = fruits[right]
            fruit_count[at_right] += 1
            
            while len(fruit_count) > 2:
                print(left)
                at_left = fruits[left]
                fruit_count[at_left] -= 1
                if fruit_count[at_left] == 0:
                    del fruit_count[at_left]
                left += 1
            
            length = right - left + 1
            max_length = max(max_length, length)
        
        return max_length
    
#30min
#2sub