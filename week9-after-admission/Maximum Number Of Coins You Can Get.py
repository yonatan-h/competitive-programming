from collections import deque

def get_max_coins(piles):
    piles.sort()
    piles_deque = deque(piles)

    my_total_coins = 0
    for _ in range(len(piles)//3):
        bob_pile = piles_deque.popleft()
        alice_pile = piles_deque.pop()
        my_pile = piles_deque.pop()

        my_total_coins += my_pile
    return my_total_coins

#1sub
#8min