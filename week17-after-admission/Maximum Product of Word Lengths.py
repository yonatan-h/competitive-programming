class Solution:
    def maxProduct(self, words: List[str]) -> int:
        binary_sets = []

        for word in words:
            binary_sets.append(to_binary_set(word))

        max_prod = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if binary_sets[i] & binary_sets[j] >0:
                    continue
                prod = len(words[i])*len(words[j])
                max_prod = max(max_prod, prod)
        return max_prod

def to_binary_set(word):
    letter_set = 0
    for letter in word:
        order = ord(letter) - ord("a")
        mask = 1 << order
        letter_set |= mask
    return letter_set


