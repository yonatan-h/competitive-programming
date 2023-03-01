class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        letters1 = list(word1)
        letters2 = list(word2)
        
        return "".join(merge_big(letters1, letters2))
        
        
def merge_big(letters1, letters2):
    ptr1 = 0
    ptr2 = 0
    merged = []
    
    while ptr1 < len(letters1) and ptr2 < len(letters2):
        if letters1[ptr1] > letters2[ptr2]:
            merged.append(letters1[ptr1])
            ptr1 += 1
        elif letters2[ptr2] > letters1[ptr1]:
            merged.append(letters2[ptr2])
            ptr2 += 1
        elif letters1[ptr1:] > letters2[ptr2:]:
            merged.append(letters1[ptr1])
            ptr1 += 1
        else:
            merged.append(letters2[ptr2])
            ptr2 += 1
            
            
            
    
    while ptr1 < len(letters1):
        merged.append(letters1[ptr1])
        ptr1 += 1
    
    while ptr2 < len(letters2):
        merged.append(letters2[ptr2])
        ptr2 += 1
    
    return merged
        
            
#15min
#1sub