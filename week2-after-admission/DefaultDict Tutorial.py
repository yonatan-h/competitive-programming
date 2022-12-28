from collections import defaultdict

def get_letter_indexes(letters):
    letter_indexes_map = defaultdict(lambda : [])

    for i in range(len(letters)):
        letter = letters[i]
        human_index = i + 1
        letter_indexes_map[letter].append(str(human_index))
    
    return letter_indexes_map

def print_indexes(letters, letter_indexes_map):
    for letter in letters:
        indexes = letter_indexes_map[letter]
        if indexes:
            print(" ".join(indexes))
        else:
            print(-1)

def main():
    num_group1, num_group2 = map(int, input().split())
    
    group1_letters = []
    for i in range(num_group1):
        group1_letters.append(input())

    group2_letters = []
    for i in range(num_group2):
        group2_letters.append(input())

    letter_indexes = get_letter_indexes(group1_letters)
    print_indexes(group2_letters, letter_indexes)

main()

#10min
#1sub