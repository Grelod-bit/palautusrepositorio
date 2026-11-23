import unittest
from unittest.mock import Mock

from kassapaate import HINTA, Kassapaate


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 10

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 4

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_kortille_ladataan_positiivinen_summa(self):
        maksukortti_mock = Mock()

        self.kassa.lataa(maksukortti_mock, 1)
        maksukortti_mock.lataa.assert_called_once_with(1)

    def test_kortille_ladataan_negatiivinen_summa(self):
        maksukortti_mock = Mock()

        self.kassa.lataa(maksukortti_mock, -1)
        maksukortti_mock.lataa.assert_not_called()
