import random


def get_random_choice():
    """
    Retourne un choix aléatoire : 'pierre', 'feuille' ou 'ciseaux'.
    :return: str
    """
    return random.choice(['pierre', 'feuille', 'ciseaux'])


def determine_winner(choice1, choice2):
    """
    Détermine le gagnant entre deux choix : 'pierre', 'feuille' ou 'ciseaux'.
    :param choice1: str
    :param choice2: str
    :return: str
    """
    if choice1 == choice2:
        return "Égalité"
    elif (choice1 == 'pierre' and choice2 == 'ciseaux') or \
            (choice1 == 'feuille' and choice2 == 'pierre') or \
            (choice1 == 'ciseaux' and choice2 == 'feuille'):
        return "Joueur 1 gagne"
    else:
        return "Joueur 2 gagne"


def simulate_games(num_games):
    """
    Simule un certain nombre de parties entre deux ordinateurs.
    :param num_games: int
    """
    for i in range(num_games):
        choice1 = get_random_choice()
        choice2 = get_random_choice()
        result = determine_winner(choice1, choice2)
        print(f"Partie {i + 1}: Joueur 1 a choisi {choice1}, Joueur 2 a choisi {choice2}. Résultat : {result}")


def play_user_vs_computer():
    """
    Permet à un joueur humain de jouer contre l'ordinateur.
    """
    while True:
        user_choice = input("Entrez votre choix (pierre, feuille, ciseaux) ou 'q' pour quitter : ").lower()
        if user_choice == 'q':
            print("Merci d'avoir joué !")
            break
        elif user_choice not in ['pierre', 'feuille', 'ciseaux']:
            print("Choix invalide, veuillez essayer à nouveau.")
            continue

        computer_choice = get_random_choice()
        print(f"L'ordinateur a choisi : {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(f"Résultat : {result}")


def main():
    """
    Fonction principale pour initialiser le jeu.
    :return:
    """
    print("Bienvenue dans le jeu de Shifumi !")
    mode = input("Choisissez le mode de jeu :\n1 - 2 ordinateurs\n2 - Jouer contre l'ordinateur\nEntrez 1 ou 2 : ")

    if mode == '1':
        num_games = int(input("Combien de parties voulez-vous simuler entre les ordinateurs ? "))
        simulate_games(num_games)
    elif mode == '2':
        play_user_vs_computer()
    else:
        print("Choix invalide. Veuillez relancer le programme et entrer 1 ou 2.")


if __name__ == "__main__":
    main()
