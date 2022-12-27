class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return get_extra_letter(s,t)

def get_extra_letter(original, extra):
    difference = Counter(extra) - Counter(original)
    for key in difference.keys():
        return key

#10min
#2submission