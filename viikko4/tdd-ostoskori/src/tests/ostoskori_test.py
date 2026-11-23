import unittest

from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(
        self,
    ):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(
        self,
    ):
        maito = Tuote("Maito", 3)
        peruna = Tuote("Peruna", 1)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(peruna)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(
        self,
    ):
        maito = Tuote("Maito", 3)
        peruna = Tuote("Peruna", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(peruna)
        self.assertEqual(self.kori.hinta(), 4)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(
        self,
    ):
        maito = Tuote("Maito", 3)
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_2_kertaa_tuotteen_hinta(
        self,
    ):
        maito = Tuote("Maito", 3)
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jälkeen_ostoskori_sisältää_yhden_ostoksen(
        self,
    ):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jälkeen_ostoskori_sisältää_saman_nimisen_ostoksen(
        self,
    ):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jälkeen_ostoskori_sisältää_kaksi_ostosta(
        self,
    ):
        maito = Tuote("Maito", 3)
        peruna = Tuote("Peruna", 1)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(peruna)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jälkeen_ostoskori_sisältää_tasan_yhden_ostoksen(
        self,
    ):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

