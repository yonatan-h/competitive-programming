class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = defaultdict(int)

        for bill in bills:

            if bill == 10:
                if counter[5] >= 1:
                    counter[5] -= 1
                else:
                    return False
            ##
            elif bill == 20:
                if counter[10] >= 1 and counter[5] >= 1:
                    counter[10]-=1
                    counter[5]-=1
                elif counter[5] >= 3:
                    counter[5] -= 3
                else:
                    return False

            counter[bill]+=1
        return True

                