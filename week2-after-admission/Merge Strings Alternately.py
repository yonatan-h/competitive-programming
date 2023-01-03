class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return merge_alternatively(word1, word2)

def merge_alternatively(word1, word2):
    merged = ""
    len1 = len(word1)
    len2 = len(word2)

    for i in range(min(len1, len2)):
        merged += word1[i]
        merged += word2[i]

    if len1 > len2:
        merged += word1[len2:]
    elif len2 > len1:
        merged += word2[len1:]
    
    return merged

#5min
#1sub