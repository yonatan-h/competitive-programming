class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        return find_common_chars(words)
    
def get_char_count_map(word):
    char_count_map = [0]*26
    for letter in word:
        letter_index = ord(letter) - ord("a")
        char_count_map[letter_index]+=1
    return char_count_map

def find_min_common_counts(words):
    char_count_maps = []
    for word in words:
        char_count_maps.append(get_char_count_map(word))
    
    min_common_counts = char_count_maps[0]
    for char_count_map in char_count_maps:
        for letter_index in range(len(char_count_map)):
            min_count = min_common_counts[letter_index]
            cur_count = char_count_map[letter_index]
            min_common_counts[letter_index] = min(min_count, cur_count)

    return min_common_counts
    
def find_common_chars(words):
    min_common_counts = find_min_common_counts(words)
    common_chars = []
    for letter_index in range(len(min_common_counts)):
        char = chr(ord("a") + letter_index)
        count = min_common_counts[letter_index]

        if count > 0:
            common_chars += [char]*count

    return common_chars

#2sub
#25min