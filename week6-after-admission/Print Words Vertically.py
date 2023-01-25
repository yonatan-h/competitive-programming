class Solution:
    def printVertically(self, s: str) -> List[str]:
        return build_vertical_words(s)
        

def cancel_trailing_spaces(letters):
    for i in reversed(range(len(letters))):
        letter = letters[i]
        if letter == " ":
            letters.pop()
        else:
            break

def build_vertical_words(sentence):
    words = sentence.split()
    
    
    vertical_words = []
    
    letter_index = 0
    
    while True:
        vertical_letters = []
        
        for word in words:
            letter = None
            
            if letter_index >= len(word):
                letter = " "
            else:
                letter = word[letter_index]
                
            vertical_letters.append(letter)
            
        cancel_trailing_spaces(vertical_letters)
        
        if len(vertical_letters) == 0: break
            
        vertical_word = "".join(vertical_letters) 
        vertical_words.append(vertical_word)
        
        letter_index += 1
        
        
    
    return vertical_words
            
#20min
#2sub