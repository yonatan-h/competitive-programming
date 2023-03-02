class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = deque(s)

        letter_counts = Counter(s)
        unique_letters_left = len(letter_counts)
        popped_set = set()

        partition_sizes = []
        sum_partition_sizes = 0
        
        for _ in range(len(s)):
            letter = letters.popleft()

            popped_set.add(letter)
            letter_counts[letter] -= 1

            if letter_counts[letter] == 0:
                del letter_counts[letter]
            
            no_shared_letters = unique_letters_left == len(letter_counts) + len(popped_set)
            if no_shared_letters:
                partition_size = len(s) - sum_partition_sizes - len(letters)
                partition_sizes.append(partition_size)
                sum_partition_sizes += partition_size

                #cut out the partition, start again
                unique_letters_left -= len(popped_set)
                popped_set.clear()

        return partition_sizes

#25min
#1sub
