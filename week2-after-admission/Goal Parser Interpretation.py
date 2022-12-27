class Solution:
    def interpret(self, command: str) -> str:
        return parse_goal(command)
    
def parse_goal(string):
    parsed_letters = [""]

    for letter in string:
        print(parsed_letters)
        if parsed_letters[-1] == "(" and letter == ")":
            parsed_letters[-1] = "o"
        else:
            parsed_letters.append(letter)
    
    for i in range(len(parsed_letters)):
        letter = parsed_letters[i]
        if letter == "(" or letter == ")":
            parsed_letters[i] = ""
    
    parsed_string = "".join(parsed_letters)
    return parsed_string
#20min
#1sub
        
