class Solution:

    def toEnglish(self, word, map):
        englishWord = ""
        for letter in word:
            englishLetter = map[letter]
            englishWord += englishLetter
        return englishWord
    
    def getAlienToEnglishMap(self, order):
        alienToEnglish = {}
        for i in range(26):
            english = chr(97+i)
            alien = order[i]
            alienToEnglish[alien] = english
        return alienToEnglish

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alienToEnglish = self.getAlienToEnglishMap(order)
        englishWords = ["A"]
        for word in words:
            englishWord = self.toEnglish( word, alienToEnglish)
            englishWords.append(englishWord)
            if englishWords[-2] > englishWords[-1]: return False
        return True
        
#40min