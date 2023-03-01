from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        return decode_level(s)


def get_simple_letters(chars):
    simple_letters = ""
    while chars and chars[0].isalpha():
        simple_letters += chars.popleft()
    return simple_letters


def get_num(chars):
    num = ""
    while chars and chars[0].isdigit():
        num += chars.popleft()
    if num: return int(num)
    else: return ""


def get_between_brackets(chars):
    if not chars or chars[0] != "[":
        return "" 

    bracket_stack = [chars.popleft()] #[

    between_brackets = ""
    while True:
        char = chars.popleft()
        if char == "[":
            bracket_stack.append("[")
        elif char == "]":
            bracket_stack.pop()

        if not bracket_stack:
            break

        between_brackets += char
        
    return between_brackets


def decode_level(string):#aa2[...]
    if string == "":#base case
        return string

    decoded = ""
    chars = deque(string) #[a]

    while chars:
        simple_letters = get_simple_letters(chars) #a
        num = get_num(chars) or 0
        between_brackets = get_between_brackets(chars)
        decoded +=  simple_letters + num * decode_level(between_brackets)
       
    return decoded
            

#50min
#1sub