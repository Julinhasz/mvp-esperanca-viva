import unittest
from app import EstoqueComunitario

class TestEstoqueComunitario(unittest.TestCase):
    def setUp(self):
        self.sistema = EstoqueComunitario()

    def test_adicionar_doacao_valida(self):
        saldo = self.sistema.adicionar_doacao("Arroz", 10)
        self.assertEqual(saldo, 10)

    def test_adicionar_doacao_invalida(self):
        with self.assertRaises(ValueError):
            self.sistema.adicionar_doacao("Feijão", 0)

    def test_registrar_saida_valida(self):
        self.sistema.adicionar_doacao("Óleo", 5)
        saldo_restante = self.sistema.registrar_saida("Óleo", 2)
        self.assertEqual(saldo_restante, 3)

    def test_registrar_saida_estoque_insuficiente(self):
        self.sistema.adicionar_doacao("Macarrão", 2)
        with self.assertRaises(ValueError):
            self.sistema.registrar_saida("Macarrão", 5)

if __name__ == "__main__":
    unittest.main()
