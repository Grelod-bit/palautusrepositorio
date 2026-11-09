from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.players=reader.get_players()

    def top_scorers_by_nationality(self,nationality):
        players_by_nation=[player for player in self.players if player.nationality == nationality]
        return sorted(players_by_nation,key=lambda x: x.goals+x.assists, reverse=True)
