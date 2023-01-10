class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = convert_to_int(num1)
        int_num2 = convert_to_int(num2)

        multiplied = int_num1 * int_num2
        str_multiplied = str(multiplied)
        return str_multiplied

def convert_to_int(str_number):
    str_num_map = {
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "0":0
    }
    integer = 0
    length = len(str_number)
    for i in range(length):
        char = str_number[i]

        digit = str_num_map[char]
        ten_power = length - (i+1)

        integer += digit * 10**ten_power
    
    return integer

#15min
#1sub