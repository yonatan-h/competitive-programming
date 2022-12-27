def separate(unreadable):
    encoded_letters = []

    for char in unreadable:
        if char == "#":
            encoded_letters[-2] += encoded_letters[-1]
            encoded_letters.pop()
        else:
            encoded_letters.append(char)
    return encoded_letters

def decode(encoded_letters):
    decoded_string = ""

    for encoded_letter in encoded_letters:
        ascii_num = int(encoded_letter) + ord("a") - 1
        decoded_letter = chr(ascii_num)
        decoded_string += decoded_letter
    
    return decoded_string

        
#10min
#1submission