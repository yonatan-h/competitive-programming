class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        longest = 0
        left = 0
        char_counts = defaultdict(int)

        for right in range(len(s)):
            char_counts[s[right]] += 1

            #while too many replacable chars
            while (right-left+1) - max(char_counts.values()) > k:
                char_counts[s[left]] -= 1
                left += 1
            
            length = right-left+1
            longest = max(longest, length)

        return longest

#45min
#1sub
            




        
