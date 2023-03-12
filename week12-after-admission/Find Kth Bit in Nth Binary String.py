class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        final_string = operate("0", 1, n)
        return final_string[k-1]


def invert_then_reverse(string):
    string = list(string)
    for i in range(len(string)):
        if string[i] == "0":
            string[i] = "1"
        else:
            string[i] = "0"

    string.reverse()
    return "".join(string)


def operate(string, operations_before, num_operations):
    if operations_before == num_operations:
        return string

    after_operation = string + "1" + invert_then_reverse(string)
    return operate(after_operation, operations_before+1, num_operations)

#1sub
#25min

    