import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

# pylint: disable=wrong-import-position
from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class PlayerStatsTest(unittest.TestCase):
    def setUp(self):
        players = [
            Player({
                "name": "Aarne Ahonen",
                "nationality": "FIN",
                "assists": 30,
                "goals": 20,
                "games": 70,
                "team": "AAA",
            }),
            Player({
                "name": "Bertil Berg",
                "nationality": "SWE",
                "assists": 40,
                "goals": 10,
                "games": 70,
                "team": "AAA",
            }),
            Player({
                "name": "Calle Carlsson",
                "nationality": "SWE",
                "assists": 10,
                "goals": 30,
                "games": 70,
                "team": "BBB",
            }),
        ]
        self.stats = PlayerStats(PlayerReaderStub(players))

    def test_nationalities_returns_unique_nationalities(self):
        self.assertEqual(self.stats.nationalities(), ["FIN", "SWE"])

    def test_top_scorers_by_nationality_returns_players_by_points(self):
        players = self.stats.top_scorers_by_nationality("SWE")

        self.assertEqual(
            [player.name for player in players],
            ["Bertil Berg", "Calle Carlsson"],
        )

    def test_top_scorers_by_team_returns_players_by_points(self):
        players = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(
            [player.name for player in players],
            ["Aarne Ahonen", "Bertil Berg"],
        )

    def test_top_goal_scorers_returns_requested_number(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in players],
            ["Calle Carlsson", "Aarne Ahonen"],
        )


if __name__ == "__main__":
    unittest.main()
