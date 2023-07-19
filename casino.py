import java.util.Random;
import java.util.Scanner;

public class Casino {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int numRandom = 0;
        int gains = 0;
        int miseUtilisateur = 0;
        int nbrUtilisateur = 0;

        System.out.println("Bienvenue au casino ! Misez sur un nombre entre 0 et 49. Si vous tombez sur le bon nombre, vous gagnez 3 fois votre mise. Sinon, vous perdez votre mise.");

        while (true) {
            try {
                System.out.print("Avec combien d'argent êtes-vous rentré ? ");
                gains = Integer.parseInt(scanner.nextLine());
                break;
            } catch (NumberFormatException e) {
                System.out.println("Vous devez entrer un nombre entier !");
            }
        }

        while (gains > 0) {
            while (true) {
                try {
                    System.out.print("Combien voulez-vous miser ? ");
                    miseUtilisateur = Integer.parseInt(scanner.nextLine());
                    if (miseUtilisateur > gains) {
                        System.out.println("Vous ne pouvez pas miser plus que ce que vous avez (" + gains + ") !");
                        continue;
                    }
                    break;
                } catch (NumberFormatException e) {
                    System.out.println("Vous devez entrer un nombre entier !");
                }
            }

            while (true) {
                try {
                    System.out.print("Sur quel nombre voulez-vous miser ? ");
                    nbrUtilisateur = Integer.parseInt(scanner.nextLine());
                    if (nbrUtilisateur < 0 || nbrUtilisateur > 49) {
                        System.out.println("Vous devez entrer un nombre entre 0 et 49 !");
                        continue;
                    }
                    break;
                } catch (NumberFormatException e) {
                    System.out.println("Vous devez entrer un nombre entier !");
                }
            }

            System.out.println("La roulette tourne...");

            // Génération du nombre aléatoire
            numRandom = random.nextInt(50);

            System.out.println("Le numéro gagnant est le " + numRandom);

            if (numRandom == nbrUtilisateur) {
                gains += Math.ceil(miseUtilisateur * 3);
                System.out.println("Bravo ! Vous avez gagné " + Math.ceil(miseUtilisateur * 3) + "€ !");
            } else if (numRandom % 2 == nbrUtilisateur % 2) {
                gains += Math.ceil(miseUtilisateur / 2);
                String couleur = (numRandom % 2 == 0) ? "noir" : "rouge";
                System.out.println("Vous avez misé sur la bonne couleur qui est " + couleur + ", vous gagnez " + Math.ceil(miseUtilisateur / 2) + "€ !");
            } else {
                gains -= miseUtilisateur;
                System.out.println("Vous avez perdu " + miseUtilisateur + "€");
            }

            System.out.println("Vous avez maintenant " + gains + "€");

            System.out.print("Voulez-vous rejouer ? (o/n) ");
            String continuePlaying = scanner.nextLine();
            if (continuePlaying.equalsIgnoreCase("n")) {
                System.out.println("Vous partez avec " + gains + "€");
                System.out.println("Au revoir !");
                break;
            }
        }

        scanner.close();
    }
}
