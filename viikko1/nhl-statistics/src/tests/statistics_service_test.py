import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),   # 4 goals, 12 assists, 16 points
            Player("Lemieux", "PIT", 45, 54),  # 45 goals, 54 assists, 99 points
            Player("Kurri",   "EDM", 37, 53),  # 37 goals, 53 assists, 90 points
            Player("Yzerman", "DET", 42, 56),  # 42 goals, 56 assists, 98 points
            Player("Gretzky", "EDM", 35, 89)   # 35 goals, 89 assists, 124 points
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def nimet(self, players):
        return [player.name for player in players]

    # search

    def test_haku_loytaa_olemassa_olevan_pelaajan(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")

    def test_haku_palauttaa_none_jos_pelaajaa_ei_ole(self):
        player = self.stats.search("Selanne")

        self.assertIsNone(player)

    def test_haku_toimii_osittaisella_nimella(self):
        player = self.stats.search("Gretz")

        self.assertEqual(player.name, "Gretzky")

    # team

    def test_joukkue_palauttaa_oikean_maaran_pelaajia(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)

    def test_joukkue_palauttaa_vain_joukkueen_pelaajat(self):
        players = self.stats.team("EDM")

        for player in players:
            self.assertEqual(player.team, "EDM")

    def test_tuntematon_joukkue_palauttaa_tyhjan_listan(self):
        players = self.stats.team("XYZ")

        self.assertEqual(players, [])

    # top, default sorting

    def test_top_ilman_parametria_jarjestaa_pisteiden_mukaan(self):
        players = self.stats.top(3)

        self.assertEqual(self.nimet(players), ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_palauttaa_pyydetyn_maaran(self):
        players = self.stats.top(2)

        self.assertEqual(len(players), 2)

    def test_top_nolla_palauttaa_tyhjan_listan(self):
        players = self.stats.top(0)

        self.assertEqual(players, [])

    def test_top_kaikki_pelaajat(self):
        players = self.stats.top(5)

        self.assertEqual(len(players), 5)

    # top, SortBy

    def test_top_pisteiden_mukaan(self):
        players = self.stats.top(3, SortBy.POINTS)

        self.assertEqual(self.nimet(players), ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_maalien_mukaan(self):
        players = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(self.nimet(players), ["Lemieux", "Yzerman", "Kurri"])

    def test_top_syottojen_mukaan(self):
        players = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(self.nimet(players), ["Gretzky", "Yzerman", "Lemieux"])

    def test_top_ilman_parametria_sama_kuin_points(self):
        self.assertEqual(
            self.nimet(self.stats.top(5)),
            self.nimet(self.stats.top(5, SortBy.POINTS))
        )