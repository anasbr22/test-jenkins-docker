
import unittest
from app import CalculatorLogic  

class TestCalculatorLogic(unittest.TestCase):

    def setUp(self):
        # Initialise la logique sans interface graphique
        self.logic = CalculatorLogic()

    def test_initial_result(self):
        # Teste l'état initial 
        self.assertEqual(self.logic.get_result(), "")

    def test_reset(self):
        # Teste la réinitialisation de l'application
        self.logic.append("123")
        self.logic.reset()
        self.assertEqual(self.logic.get_result(), "")

    def test_calculate(self):
        # Teste le calcul de l'expression
        self.logic.append("2+2")
        self.logic.calculate()
        self.assertEqual(self.logic.get_result(), "4")

    def test_calculate_invalid_expression(self):
        # Teste le calcul d'une expression invalide
        self.logic.append("2/0")
        self.logic.calculate()
        self.assertEqual(self.logic.get_result(), "Erreur")

    def test_append(self):
        # Teste l'ajout de caractères à l'expression
        self.logic.append("1")
        self.logic.append("+")
        self.logic.append("1")
        self.assertEqual(self.logic.get_result(), "1+1")

if __name__ == "__main__":
    unittest.main()

