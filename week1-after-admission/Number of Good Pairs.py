from collections import Counter 

def find_number_of_good_pairs(numbers):
    repeating_numbers = []
    counts = Counter(numbers)
    
    num_good_pairs = 0
    for number in counts.values():
        count = counts[number]
        num_good_pairs += (count * (count-1))//2

    return num_good_pairs
    


#40min