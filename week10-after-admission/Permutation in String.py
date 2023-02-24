class Solution:
    def checkInclusion(self, smaller: str, larger: str) -> bool:
        smaller_count = defaultdict(int)
        for letter in smaller:
            smaller_count[letter] += 1
            
        current_count = defaultdict(int)
        left = 0
        
        for right in range(len(larger)):
            at_right = larger[right]
            current_count[at_right] += 1
            
            if right - left == len(smaller):
                at_left = larger[left]
                current_count[at_left] -= 1
                if current_count[at_left] == 0:
                    del current_count[at_left]
                left += 1
                
            if current_count == smaller_count:
                return True
        
        return False
    
#20min
#1sub
            
                
                