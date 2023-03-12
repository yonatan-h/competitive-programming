class Solution:
    def splitString(self, string: str) -> bool:
        divided = []

        def divide(rest_of_string):
            if not rest_of_string and len(divided) > 1:
                return True


            for i in range(1, len(rest_of_string)+1):
                num = int(rest_of_string[:i])

                if len(divided) and num != divided[-1]-1:
                    continue
                
                divided.append(num)
                if divide(rest_of_string[i:]): return True
                divided.pop()

        return divide(string)
            

#30min
#1sub