class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        return add_spaces(s, spaces)


def add_spaces(text, spaces):
    spaces.append(None)
    space_pointer = 0
    letters_with_spaces = []
    
    for i in range(len(text)):
        letter = text[i]
        cur_space_index = spaces[space_pointer]
        
        if i == cur_space_index:
            letters_with_spaces.append(" ")
            letters_with_spaces.append(letter)
            space_pointer += 1
        else:
            letters_with_spaces.append(letter)
    
    return "".join(letters_with_spaces)

#20min
#1sub