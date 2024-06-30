import unittest
from models.Caixa import CAIXA
from models.Excecoes  import ErroEntradaInvalida, ErroCedulasIndisponiveis

class TestCAIXA(unittest.TestCase):
    def setUp(self):
        self.caixa = CAIXA()

    def test_saque_negativo_ou_zero_lanca_erro_entrada_invalida(self):
        with self.assertRaises(ErroEntradaInvalida):
            self.caixa.sacar(0)
        with self.assertRaises(ErroEntradaInvalida):
            self.caixa.sacar(-100)

    def test_saque_valor_indisponivel_lanca_erro_cedulas_indisponiveis(self):
        with self.assertRaises(ErroCedulasIndisponiveis):
            self.caixa.sacar(3)

    def test_saque_valor_valido(self):
        resultado = self.caixa.sacar(240)
        self.assertEqual(resultado, {'100': 2, '50': 0, '20': 2, '10': 0, '5': 0, '2': 0})

if __name__ == '__main__':
    unittest.main()