class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        reps = {}
        alphabet = list(string.ascii_lowercase)
        for letter in alphabet:
            reps[letter] = letter
        
        inequalities = []
        for equation in equations:
            letter1 = equation[0]
            letter2 = equation[-1]
            has_equality = equation[1:3] == "=="

            if has_equality:
                union(letter1, letter2, reps)
            else:
                inequalities.append(equation)
        
        for equation in inequalities:
            letter1 = equation[0]
            letter2 = equation[-1]

            rep1 = find(letter1, reps)
            rep2 = find(letter2, reps)
            if rep1 == rep2:
                return False
        
        return True





def union(letter1, letter2, reps):
    rep1 = find(letter1, reps)
    rep2 = find(letter2, reps)
    reps[rep2] = rep1

def find(letter, reps):
    if letter == reps[letter]:
        return letter

    rep = find(reps[letter], reps)
    reps[letter] = rep
    return rep