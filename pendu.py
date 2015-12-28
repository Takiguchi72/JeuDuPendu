'''
Created on 26 déc. 2015

@author: takiguchi
'''
#!/usr/bin/python3

from fonctions import afficherIntro, saisirDifficultee, obtenirMot, recapitulerMotMasque, saisirLettre, afficherPendu, \
                    initialiserLettresATrouver
from variables import dessinPendu
from sys import exit

if __name__ == "__main__":
    continuer = True
        
    while(continuer):
        motTrouve = False
        lettresDites = []
        lettresATrouver = None
        coupsRestants = len(dessinPendu)
        lettreSaisie = ""
    
        # On affiche l'intro du jeu
        afficherIntro()
        
        # Saisie de la difficultée
        difficulte = saisirDifficultee()
        
        # Sélection d'un mot en fonction de la difficultée saisie
        motATrouver = obtenirMot(difficulte)
        
        # On affiche la taille du mot
        print("Le mot à trouver contient {0} lettres".format(len(motATrouver)))
        
        # On initialise un tableau contenant toutes les lettres composant le mot à trouver
        lettresATrouver = initialiserLettresATrouver(motATrouver)
        
        # Tant que le mot n'a pas été trouvé et qu'il reste des tentatives au joueur
        while(not motTrouve and coupsRestants > 0):
            # On affiche le nombre de coups restant
            print("\nNombre de coups restant : {0}".format(coupsRestants))
            
            # On affiche les lettres déjà saisies de manière triée
            if(len(lettresDites) > 0):
                print("Lettres dites : {0}".format(sorted(lettresDites)))
            
            # On affiche les tirets pour chaque lettre non trouvée du mot
            recapitulerMotMasque(motATrouver, lettresATrouver)
            
            # Saisie de la lettre par l'utilisateur
            lettreSaisie = saisirLettre(lettresDites)
            
            # On enregistre la lettre dans la liste des lettres déjà dites
            lettresDites.append(lettreSaisie)
            
            # Si la lettre saisie est dans le mot
            if(lettreSaisie in motATrouver):
                print("Bravo ! Cette lettre est contenue dans le mot !")
                
                # On supprime la lettre de la liste de lettres à trouver
                lettresATrouver.remove(lettreSaisie)
                
                # S'il ne reste plus de lettre à trouver
                if(len(lettresATrouver) == 0):
                    # Le joueur a gagné
                    motTrouve = True
                    
            else:
                print("Et non, le mot ne contient pas cette lettre !")
                afficherPendu(coupsRestants)
                # On décrémente le nombre de tentatives restantes
                coupsRestants -= 1
                
        # Si le mot a été trouvé ou que le joueur a épuisé ses tentatives,
        # on affiche le message indiquant si le joueur a gagné ou perdu
        print("Bravo ! Vous avez trouvé le mot masqué !") if motTrouve else print("Perdu... Le mot masqué était : {0}".format(motATrouver))
        
        rejouer = input("Voulez-vous rejouer ? (o/n) ")
         
        if(not rejouer.lower() == "o"):
            continuer = False

    print("Au revoir ! :)")
    exit(0)