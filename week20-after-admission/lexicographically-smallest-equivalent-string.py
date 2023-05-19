class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        reps = {}
        alphabet = list(string.ascii_lowercase)
        for letter in alphabet:
            reps[letter] = letter
        
        for i in range(len(s1)):
            letter1 = s1[i]
            letter2 = s2[i]
            union(letter1, letter2, reps)
        
        lowest_string = ""
        for letter in baseStr:
            lowest_letter = find(letter, reps)
            lowest_string += lowest_letter
        
        return lowest_string





def union(letter1, letter2, reps):
    rep1 = find(letter1, reps)
    rep2 = find(letter2, reps)

    merge_to_1 = rep1 < rep2
    if merge_to_1:
        reps[rep2] = rep1
    else:
        reps[rep1] = rep2




def find(letter, reps):
    if letter == reps[letter]:
        return letter

    rep = find(reps[letter], reps)
    reps[letter] = rep
    return rep