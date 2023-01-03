from collections import defaultdict

def main():
    num_words = int(input())
    unique_words = []
    word_counter = defaultdict(int)

    for i in range(num_words):
        word = input()

        if word in word_counter:
            word_counter[word] += 1
        else:
            unique_words.append(word)
            word_counter[word] += 1

    print(len(word_counter))

    for word in unique_words:
        print(word_counter[word], end=" ")


main()

#60 min
#1sub
