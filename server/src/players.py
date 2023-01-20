import player


class Players:
    def __init__(self):
        self.players = []

    def add_player(self, player: player.Player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def list_players(self):
        for player in self.players:
            print(player.get_name())

    def count_votes(self):
        in_favor = 0
        against = 0

        for player in self.players:
            vote = player.get_vote()

            if vote is None:
                print("Vote not set correctly")
                raise RuntimeError(
                    "Vote not set correctly of player", player.get_chair_number())

            if vote == "YES":
                in_favor += 1
            if vote == "NO":
                against += 1

        return in_favor, against

    def reset_votes(self):
        for player in self.players:
            player.reset_vote()
