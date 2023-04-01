
def countBits(n):
    known_counts = {0:0}
    counts = []

    for num in range(n+1):
        #last digit + what is after shift
        count = (num & 1) + known_counts[num//2]
        known_counts[num] = count
        counts.append(count)

        print(num, " -> ", count)
        print(num//2, " -> ", known_counts[num//2])
        print()

    print(known_counts)
    return counts


print(countBits(5))