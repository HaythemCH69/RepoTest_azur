from random import randint
from math import ceil

# Déclaration des variables
numRandom = 0
gains = 0
miseUtilisateur = 0
nbrUtilisateur = 0

print("Bienvenue au casino ! Misez sur un nombre entre 0 et 49. si vous tombez sur le bon nombre, vous gagnez 3 fois votre mise. sinon vous perdez votre mise ")

while True:
    try:
        gains = int(input("Avec combien d'argent vous êtes rentré ? "))
        break
    except ValueError:
        print("Vous devez entrer un nombre entier !")

while gains > 0:
    while True:
        try:
            miseUtilisateur = int(input("Combien voulez-vous miser ? "))
            if miseUtilisateur > gains:
                print(f"Vous ne pouvez pas miser plus que ce que vous avez ({gains}) !")
                continue
            break
        except ValueError:
            print("Vous devez entrer un nombre entier !")
    
    while True:
        try:
            nbrUtilisateur = int(input("Sur quel nombre voulez-vous miser ? "))
            if nbrUtilisateur <0 or nbrUtilisateur > 49:
                print("Vous devez entrer un nombre entre 0 et 49 !")
                continue
            break
        except ValueError:
            print("Vous devez entrer un nombre entier !")

    print("La roulette tourne...")

    # Génération du nombre aléatoire
    numRandom = randint(0, 49)

    print(f"Le numéro gagnant est le {numRandom}")

    if numRandom == nbrUtilisateur:
        gains += ceil (miseUtilisateur * 3)
        print(f"Bravo ! Vous avez gagné {ceil (miseUtilisateur * 3)}€ !")
    elif numRandom % 2 == nbrUtilisateur % 2:
        gains += ceil (miseUtilisateur / 2)
        couleur = "noir" if numRandom % 2 == 0 else "rouge"
        print(f"Vous avez misé sur la bonne couleur qui est {couleur}, vous gagnez {miseUtilisateur / 2}€ !")
    else:
        gains -= miseUtilisateur
        print(f"Vous avez perdu {miseUtilisateur}€")

    print(f"Vous avez maintenant {gains}€")
    
    continue_playing = input("Voulez vous rejouer ? (o/n) ")
    if continue_playing.lower() == "n":
        print(f"Vous partez avec {gains}€")
        print("Au revoir !")
        break