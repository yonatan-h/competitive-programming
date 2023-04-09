class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = defaultdict(int)
        for num in deck:
            counter[num] += 1
        
        counts = list(counter.values())

        greatest = counts[0]
        for count in counts:
            greatest = gcf(greatest, count)
            if greatest == 1:
                return False
        return True
        
        
def gcf(num1, num2):
    big_num = max(num1, num2) #probably not neccessary
    small_num = min(num1, num2) #probably not neccessary

    while small_num:
        remainder = big_num%small_num
        big_num = small_num
        small_num = remainder
    
    return big_num
    