from enum import Enum
from player_reader import PlayerReader


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


def sort_key(sorting):
    if sorting == SortBy.GOALS:
        return lambda player: player.goals
    if sorting == SortBy.ASSISTS:
        return lambda player: player.assists
    return lambda player: player.points


class StatisticsService:
    def __init__(self, reader: PlayerReader):
        self.reader = reader
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sorting=SortBy.POINTS):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_key(sorting)
        )

        return sorted_players[:how_many]