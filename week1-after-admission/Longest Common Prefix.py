class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return get_longest_prefix(strs)


def get_longest_prefix(words):

    smallest_word = words[0]

    for word in words:
        if  len(word) < len(smallest_word):
            smallest_word = word

    for i in range(len(smallest_word)):
        for word in words:
            if smallest_word[i] != word[i]:
                return word[:i]
                
    return smallest_word

    
#40min