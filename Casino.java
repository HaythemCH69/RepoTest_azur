import java.util.Random;

public class Casino {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java Casino <argent_initial>");
            System.exit(1);
        }

        int gains = 0;
        int miseUtilisateur = 0;
        int nbrUtilisateur = 0;

        try {
            gains = Integer.parseInt(args[0]);
        } catch (NumberFormatException e) {
            System.out.println("Vous devez entrer un nombre entier pour l'argent initial !");
            System.exit(1);
        }

        Random random = new Random();

        System.out.println("Bienvenue au casino ! Misez sur un nombre entre 0 et 49. Si vous tombez sur le bon nombre, vous gagnez 3 fois votre mise. Sinon, vous perdez votre mise.");

        while (gains > 0) {
            System.out.print("Combien voulez-vous miser ? ");
            miseUtilisateur = Integer.parseInt(System.console().readLine());

            if (miseUtilisateur > gains) {
                System.out.println("Vous ne pouvez pas miser plus que ce que vous avez (" + gains + ") !");
                continue;
            }

            System.out.print("Sur quel nombre voulez-vous miser ? ");
            nbrUtilisateur = Integer.parseInt(System.console().readLine());

            if (nbrUtilisateur < 0 || nbrUtilisateur > 49) {
                System.out.println("Vous devez entrer un nombre entre 0 et 49 !");
                continue;
            }

            System.out.println("La roulette tourne...");

            // Génération du nombre aléatoire
            int numRandom = random.nextInt(50);

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
            String continuePlaying = System.console().readLine();
            if (continuePlaying.equalsIgnoreCase("n")) {
                System.out.println("Vous partez avec " + gains + "€");
                System.out.println("Au revoir !");
                break;
            }
        }
    }
}
