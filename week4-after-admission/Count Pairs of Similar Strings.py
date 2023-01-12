class Solution:
    def similarPairs(self, words: List[str]) -> int:
        set_words = []
        for word in words:
            set_words.append((set(word)))
        
        similar_pairs_count = 0
        for i in range(len(set_words)):
            for j in range(i+1, len(set_words)):
                set_word1 = set_words[i]
                set_word2 = set_words[j]
                if set_word1 == set_word2:
                    similar_pairs_count += 1

        return similar_pairs_count

#1sub
#10min