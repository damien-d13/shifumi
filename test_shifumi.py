import unittest
from unittest.mock import patch

from shifumi import get_random_choice, determine_winner, play_user_vs_computer, main


class TestShifumiSimulation(unittest.TestCase):

    def test_get_random_choice(self):
        """
        Teste la fonction get_random_choice.
        :return:
        """
        for _ in range(100):
            choice = get_random_choice()
            self.assertIn(choice, ['pierre', 'feuille', 'ciseaux'], "Choix invalide généré")

    def test_determine_winner(self):
        """
        Teste la fonction determine_winner.
        :return:
        """
        # Cas d'égalité
        self.assertEqual(determine_winner('pierre', 'pierre'), "Égalité")
        self.assertEqual(determine_winner('feuille', 'feuille'), "Égalité")
        self.assertEqual(determine_winner('ciseaux', 'ciseaux'), "Égalité")

        # Cas où Joueur 1 gagne
        self.assertEqual(determine_winner('pierre', 'ciseaux'), "Joueur 1 gagne")
        self.assertEqual(determine_winner('feuille', 'pierre'), "Joueur 1 gagne")
        self.assertEqual(determine_winner('ciseaux', 'feuille'), "Joueur 1 gagne")

        # Cas où Joueur 2 gagne
        self.assertEqual(determine_winner('pierre', 'feuille'), "Joueur 2 gagne")
        self.assertEqual(determine_winner('feuille', 'ciseaux'), "Joueur 2 gagne")
        self.assertEqual(determine_winner('ciseaux', 'pierre'), "Joueur 2 gagne")

    @patch('shifumi.input', side_effect=['pierre', 'q'])
    @patch('builtins.print')  # Simule les appels print
    @patch('shifumi.get_random_choice', return_value='ciseaux')
    def test_play_user_vs_computer(self, mock_random_choice, mock_print, mock_input):
        """
        Teste la fonction play_user_vs_computer.
        :param mock_random_choice:
        :param mock_print:
        :param mock_input:
        :return:
        """
        play_user_vs_computer()

        mock_print.assert_any_call(
            f"L'ordinateur a choisi : {mock_random_choice.return_value}")
        mock_print.assert_any_call("Merci d'avoir joué !")

    @patch('builtins.input', side_effect=['1', '2'])
    @patch('shifumi.simulate_games')
    def test_main_mode_selection(self, mock_simulate_games, mock_input):
        """
        Teste la sélection du mode de jeu dans la fonction main.
        :param mock_simulate_games:
        :param mock_input:
        :return:
        """
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Bienvenue dans le jeu de Shifumi !")
            mock_simulate_games.assert_called_once_with(2)


if __name__ == "__main__":
    unittest.main()
