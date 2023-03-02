class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        player_index = 0
        trainer_index = 0

        pair_count = 0

        while player_index < len(players) and trainer_index < len(trainers):
            player = players[player_index]
            trainer = trainers[trainer_index]

            if player <= trainer:
                pair_count += 1
                player_index += 1
                trainer_index += 1

            else: #player > trainer
                trainer_index += 1

        return pair_count

#15min
#1sub

