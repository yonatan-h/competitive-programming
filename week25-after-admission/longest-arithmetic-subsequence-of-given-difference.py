class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        happy_chains = defaultdict(int)
        for num in arr:
            needed = num - difference
            len_chain = happy_chains[needed] + 1
            happy_chains[num] = max(happy_chains[num], len_chain)
        
        return max(happy_chains.values())