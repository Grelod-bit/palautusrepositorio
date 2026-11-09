class PlayerStats:
    def __init__(self, reader):
        self.players=reader.get_players()

    def nationalities(self):
        return list(dict.fromkeys(player.nationality for player in self.players))

    def teams(self):
        return list(dict.fromkeys(player.team for player in self.players))

    def top_scorers_by_nationality(self,nationality):
        players_by_nation=[player for player in self.players if player.nationality == nationality]
        return sorted(players_by_nation,key=lambda x: x.goals+x.assists, reverse=True)

    def top_scorers_by_team(self, team):
        players_by_team = [player for player in self.players if player.team == team]
        return sorted(players_by_team, key=lambda x: x.goals + x.assists, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        return sorted(self.players, key=lambda x: x.goals, reverse=True)[:how_many]
