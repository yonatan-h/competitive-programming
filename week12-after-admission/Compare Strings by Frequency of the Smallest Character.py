class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i in range(len(queries)):
            queries[i] = f(queries[i])
        f_queries = queries

        for i in range(len(words)):
            words[i] = f(words[i])
        f_words = words

        print(words, f_words)

        f_words.sort()

        f_words_above = [] #strictly lesser positions
        for f_query in f_queries:
            answer = get_f_words_above(f_words, f_query)
            f_words_above.append(answer)
        
        return f_words_above


def get_f_words_above(f_words, f_query):
    left = -1 #should land on <= query
    right = len(f_words) #should land on > query
    
    while right > left + 1:
        middle = (left + right)//2
        
        if f_words[middle] > f_query:
            right = middle
        else:
            left = middle
            
    num_above_query = len(f_words) - right
    return num_above_query

def f(word):
    counts = Counter(word)
    min_letter = "z"
    for letter in counts.keys():
        min_letter = min(min_letter, letter)
    
    return counts[min_letter]

#2sub
#60min