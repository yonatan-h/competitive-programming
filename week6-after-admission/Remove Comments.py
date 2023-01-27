def remove_slash_slash(lines):
    free_lines = []
    for line in lines:
        i_non_space = index_of_non_space(line)
        first_two_chars = line[i_non_space: 2+i_non_space]
        if first_two_chars != "//":
            free_lines.append(line)

    return free_lines

def index_of_non_space(line):
    for i in range(len(line)):
        char = line[i]
        if char != " ":
            return i
    return None
        
def join_ignoring_empty_lines(chars):
    joined = ""
    last_char = ""
    for char in chars:
        if char == last_char == "\n":
            pass
        else:
            joined += char
            last_char = char

    return joined




def remove_slash_stars(lines):
    file = "\n".join(lines)

    outside_chars = []
    i = 0
    is_inside_comment = False

    while i < len(file)-1:
        cur_char = file[i]
        next_char = file[i+1]

        if cur_char == "/" and next_char == "*":
            is_inside_comment = True
            i+=2 #skip forward, no need to check
            continue
        elif cur_char == "*" and next_char == "/":
            print("here")
            is_inside_comment = False
            i+=2 #skip forward, no need to check
            continue
        
        if not is_inside_comment:
            outside_chars.append(cur_char)

        i+=1

    free_file = join_ignoring_empty_lines(outside_chars)
    free_lines = free_file.split("\n")
    return free_lines



lines = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
print(remove_slash_stars(["abc", "/*not normal*/", "abebe abate"]))