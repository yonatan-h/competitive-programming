class TopVotedCandidate:

    def __init__(self, persons: List[int], days: List[int]):
        self.winners = get_winners(persons, days)


    def q(self, day: int) -> int:
        (day, winner) = find_winner(self.winners, day)
        return winner

        

def find_winner(winners, day):
    left = -1 #before or equal to day
    right = len(winners) #after day

    while right > left + 1:
        mid = (left + right)//2
        day_at_mid = winners[mid][0]

        if day_at_mid > day: right = mid
        else: left = mid
    
    return winners[left]


    
def get_winners(persons, days):

    day_person_pairs = list(zip(days, persons))
    
    #to keep votes per day as they were
    day_person_pairs = sorted(day_person_pairs, key=lambda x: x[0])

    vote_count = defaultdict(int)
    winners = [(-1, None)] #day winner pairs
    max_person = None

    for (day, person) in day_person_pairs:
        vote_count[person] += 1
        
        #>= for most recent
        if vote_count[person] >= vote_count[max_person]:
            max_person = person
        
        same_day = winners[-1][0] == day
        if same_day:
            winners.pop()
            winners.append((day, max_person))
        else:
            winners.append((day, max_person))

    return winners
            
            
        

        






    

def flip_tuples(arr):
    for i in range(len(arr)):
        (x,y) = arr[i]
        arr[i] = (y,x)
    

def get_node():
    return None

def get_person_votes_map():
    return default_dict(int)


#50min
#1sub