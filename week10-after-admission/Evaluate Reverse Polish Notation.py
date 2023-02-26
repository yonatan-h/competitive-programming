class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        
        for token in tokens:
            if token.isnumeric():
                num_stack.append(int(token))
            else:
                num2 = num_stack.pop() 
                num1 = num_stack.pop() 
                
                result = None
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num1 - num2
                elif token == "*":
                    result = num1 * num2
                elif token == "/":
                    result == num1//num2
                
                num_stack.append(result)
                
        return num_stack.pop()
    
#15min                    
#1sub
                
            
        
