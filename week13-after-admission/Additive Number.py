class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return find_additive([], num)
        
def find_additive(sequence, string):
    print(sequence, string)

    if string == "" and len(sequence) >= 3:
        return True
    

    for i in range(1, len(string)+1):
        portion = string[:i]
        if portion != "0" and portion[0] == "0":
            return False
        portion = int(portion)

        sum_satisfied = len(sequence)>=2 and sequence[-1]+sequence[-2] == portion
        too_early = len(sequence) < 2

        if sum_satisfied or too_early:
            sequence.append(portion)
            if find_additive(sequence, string[i:]): return True
            sequence.pop()
