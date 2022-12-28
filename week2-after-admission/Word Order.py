import textwrap

def wrap(string, max_width):
    paragraph = string[0]
    for i in range(1,len(string)):
        letter = string[i]

        if i%max_width == 0:
            paragraph += "\n"
        paragraph += letter
    
    return paragraph

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#5min
#1sub