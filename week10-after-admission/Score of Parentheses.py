class Solution:
    def scoreOfParentheses(self, string: str) -> int:
        children_score_stack = [0] #the children brackets are no scored yet
                
        for char in string:
            if char == "(":
                #new parent found, append the score of its children
                children_score_stack.append(0)
            elif char == ")":
                childrens_score = children_score_stack.pop()
                
                if childrens_score == 0:
                    my_score = 1
                    children_score_stack[-1] += my_score
                else:
                    my_score = childrens_score*2
                    children_score_stack[-1] += my_score
                    
        children_in_root_score = children_score_stack.pop()
        return children_in_root_score
            
                
                
#60
#1sub 