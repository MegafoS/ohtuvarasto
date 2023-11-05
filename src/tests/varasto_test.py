import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    
    def test_varaston_tilavuus_on_oikein(self):
        self.varasto = Varasto(10)
        self.assertEqual(self.varasto.tilavuus, 10)
    def test_varaston_tilavuus_ei_aloita_negatiivisena(self):
        self.varasto = Varasto(-10)
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_varaston_saldo_ei_aloita_negatiivisena(self):
        self.varasto = Varasto(10,-10)
        self.assertEqual(self.varasto.saldo, 0)


    def test_negatiivisen_lisaaminen_ei_onnistu(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_varastoon_lisaminen_toimii(self):
        self.varasto = Varasto(10.0, 5.0)
        self.varasto.lisaa_varastoon(3.0)
        self.assertEqual(self.varasto.saldo,8.0)
        self.varasto.lisaa_varastoon(5.0)
        self.assertEqual(self.varasto.saldo,10.0)

    def test_negatiivista_ei_voi_ottaa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, 5)

    
    def test_varastosta_voi_ottaa_kaiken(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(6)
        self.assertEqual(self.varasto.saldo, -20)
    
    def test_str_toimii(self):
        self.varasto = Varasto(10.0, 5.0)
        expected_str = "saldo = 5.0, vielä tilaa 5.0"
        self.assertEqual(str(self.varasto), expected_str)
    