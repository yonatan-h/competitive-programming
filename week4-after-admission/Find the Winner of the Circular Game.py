class Solution:
    def findTheWinner(self, num_players: int, num_hops: int) -> int:
        players = [i for i in range(1, num_players+1)]
        return play(players, num_hops)


def play(players, num_hops):
    player_index = num_hops-1
    
    while len(players) != 1:
        print(players.pop(player_index))
        player_index = (player_index + num_hops-1) % len(players)
    
    return players[0]

#1sub
#60min