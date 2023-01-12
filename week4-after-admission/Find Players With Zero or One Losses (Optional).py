class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_losses_map = get_players_loses_map(matches)

        no_loss_players = []
        one_loss_players = []

        for player in player_losses_map:
            loses = player_losses_map[player]

            print(loses)

            if loses == 0:
                no_loss_players.append(player)
            elif loses == 1:
                one_loss_players.append(player)

        no_loss_players.sort()
        one_loss_players.sort()

        return [no_loss_players, one_loss_players]


def get_zero():
    return 0

def get_players_loses_map(matches):
    player_losses_map = defaultdict(get_zero)
    for match in matches:
        winner = match[0]
        1+player_losses_map[winner] #just to initialize

        loser = match[1]
        player_losses_map[loser] += 1
    
    return player_losses_map

#1sub
#30min

