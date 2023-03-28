class Solution:
    def minWindow(self, big: str, small: str) -> str:
        small_counts = Counter(small)
        window_counts = defaultdict(int)

        min_right = float("inf")
        min_left = 0

        left = 0
        for right in range(len(big)):
            letter = big[right]
            window_counts[letter] += 1

            while can_shrink(small_counts, window_counts, big[left]):
                window_counts[big[left]] -= 1
                left += 1

            if has_small(small_counts, window_counts):
                if right-left < min_right-min_left:
                    min_left = left
                    min_right = right

        
        if min_right == float("inf"):
            return ""
        else:
            return big[min_left: min_right+1]

            



def has_small(small_counts, window_counts):
    for letter in small_counts.keys():
        window_count = window_counts[letter]
        small_count = small_counts[letter]

        if window_count < small_count:
            return False
    return True


def can_shrink(small_counts, window_counts, deducted_letter):
    window_counts[deducted_letter] -= 1

    if not has_small(small_counts, window_counts):
        window_counts[deducted_letter] += 1
        return False

    window_counts[deducted_letter] += 1
    return True


