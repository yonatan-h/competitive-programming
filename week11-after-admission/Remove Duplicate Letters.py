class Solution:
    def removeDuplicateLetters(self, string: str) -> str:
        non_stack_counts = Counter(string)
        stack = []
        stack_set = set()

        for letter in string:
            def letter_in_stack():
                return letter in stack_set
            
            def top_has_backup():
                return non_stack_counts[stack[-1]] > 0
            
            def letter_is_smaller():
                return letter < stack[-1]

            while stack and  letter_is_smaller() and top_has_backup() and not letter_in_stack() :
                popped = stack.pop()
                stack_set.remove(popped)
            
            if letter not in stack_set:
                stack.append(letter)
                stack_set.add(letter)

            non_stack_counts[letter] -= 1
        
        return "".join(stack)

#40min
#5sub

