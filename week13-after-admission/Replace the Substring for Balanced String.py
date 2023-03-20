class Solution:
    def balancedString(self, string: str) -> int:
        return balance(string)

from collections import Counter, defaultdict
def balance(string):
    excess = excess_letters(string)
    window = defaultdict(int)

    print(excess)

    if len(excess) == 0:
        return 0

    left = 0
    min_win_len = float("inf")
    for right in range(len(string)):
        letter = string[right]
        window[letter] += 1
        while can_shrink(window, excess, string[left]):
            window[string[left]] -= 1
            left += 1
        
        if is_sub_dict(excess, window):
            min_win_len = min(min_win_len, right-left+1)

    return min_win_len

        

def excess_letters(string):
    a_fourth = len(string)//4
    counts = Counter(string)
    excess_letters = {}

    for letter in counts.keys():
        excess = counts[letter] - a_fourth
        if excess > 0:
            excess_letters[letter] = excess
    return excess_letters

def is_sub_dict(excess, window):
    for letter in excess.keys():
        if window[letter] < excess[letter]:
            return False
    return True

def can_shrink(window, excess, left_letter):
    #shrink and test validity
    window[left_letter] -= 1

    if not is_sub_dict(excess, window):
        window[left_letter] += 1
        return False

    #restore from test
    window[left_letter] += 1
    return True
