class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        num_rows = rowIndex + 1
        return get_last_line([], num_rows)



def get_last_line(line, num_future_lines):
    
    my_line = build_line(line)
    if num_future_lines == 1:
        return my_line

    return get_last_line(my_line, num_future_lines-1)


def build_line(prev_line):
    line = [None]*(len(prev_line)+1)
    line[0] = 1
    line[-1] = 1

    for i in range(1, len(line)-1):
        line[i] = prev_line[i-1] + prev_line[i]

    return line
    
#10min
#1sub