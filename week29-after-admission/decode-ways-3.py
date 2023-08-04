class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def pick(index):
            if index >= len(s):
                return 1

            count = 0

            #0x
            if s[index]=="0":
                return 0
                

            #a
            count += pick(index+1)



            #ab
            if index+1 < len(s):
                two_digits = int(s[index]+s[index+1])
                
                if two_digits <= 26:
                    count += pick(index+2)
            
            return count
        
        return pick(0)