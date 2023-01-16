class Solution:
    def minDeletionSize(self, words: List[str]) -> int:
        num_deleted_columns = 0
        word_length = len(words[0])
        
        for letter_index in range(word_length):
            prev_word_letter = "a"
            
            for word in words:
                letter = word[letter_index]
                
                if letter >= prev_word_letter:
                    prev_word_letter = letter
                else:
                    num_deleted_columns += 1
                    break
                    
        return num_deleted_columns
    
#2sub
#10min