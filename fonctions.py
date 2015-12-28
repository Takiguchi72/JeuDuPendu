'''
Created on 26 déc. 2015

@author: takiguchi
'''
from re import match
from random import choice
from variables import listeMots, dessinPendu
from exceptions.lettreDejaTrouveeException import LettreDejaTrouveeException
from exceptions.saisieException import SaisieException



def afficherIntro():
    '''
    Affiche le message d'intro du jeu
    '''
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("        L E   P E N D U         ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nBienvenue dans le Bigbee Pendu." )
    print("Vous devez trouver le mot qui est uniquement composé de lettres.")
    
def initialiserLettresATrouver(pMotATrouver):
    '''
    Retourne la liste des lettres contenues dans le mot à trouver
    
    @param pMotATrouver: Le mot à trouver
    
    @return: Le tableau contenant les lettres à trouver
    '''
    listeLettreATrouver = []
    # i ne sert à rien, mais s'il n'était pas présent, lettre serait un tableau de deux valeurs
    for i, lettre in enumerate(pMotATrouver):
        if(not lettre in listeLettreATrouver):
            listeLettreATrouver.append(lettre)
    return listeLettreATrouver

def afficherDifficultes():
    '''
    Affiche les difficultés possibles du jeu
    '''
    print("\nVeuillez choisir votre difficulté : \n   (0) Facile\n   (1) Intermédiaire\n   (2) Difficile")

def verifierDifficulte(pDifficulte):
    '''
    Vérifie que la saisie effectuée est comprise entre 0 et 2 (inclus)
    
    @raise Exception: Si la saisie est différente de 0, 1 ou 2
    '''
    if(not match("^[0-2]$", pDifficulte)):
        raise SaisieException()

def saisirDifficultee():
    '''
    Effectue la saisie de la difficulté, en affichant les difficultés disponibles,
    et en contrôlant la saisie
    
    @return: La difficulté saisie [int]
    '''
    # On affiche les difficultées
    afficherDifficultes()
    
    # On effectue la saisie
    difficulte = input()
    
    try:
        verifierDifficulte(difficulte)
    except SaisieException:
        # En cas d'erreur, on affiche le message correspondant et on réeffectue la saisie
        print("Erreur : Numéro de difficulté incorrect !")
        difficulte = saisirDifficultee()
    
    # On retourne le numéro de la difficulté saisie
    return difficulte

def obtenirMot(pDifficulte):
    '''
    Retourne un mot aléatoire parmit la liste en fonction de la difficulté
    
    @param pDifficulte: La difficulté choisie par le joueur
    '''
    return choice(listeMots[int(pDifficulte)])

def recapitulerMotMasque(pMotATrouver, pLettresATrouver):
    '''
    Affiche les parties du mot masqué en fonction des lettres déjà trouvées
    
    @param pMotATrouver: Le mot masqué de la partie
    
    @param pLettresTrouvees: Tableau contenant les lettres trouvées du mot masqué
    '''
    motAAfficher = ""
    # i ne sert à rien, mais s'il n'était pas présent, lettre serait un tableau de deux valeurs
    for i, lettre in enumerate(pMotATrouver):
        if(lettre in pLettresATrouver):
            motAAfficher += "-"
        else:
            motAAfficher += lettre
    print("Mot : {0}".format(motAAfficher))
#     return motAAfficher
        
def verifierLettre(pLettre):
    '''
    Vérifie que la saisie effectuée est une lettre
    
    @raise Exception: Si la saisie n'est pas une lettre
    '''
    if(not match("^[a-zA-Z]$", pLettre)):
        raise SaisieException()   
    
def verifierLettreDejaSaisie(pLettre, pLettresDites):
    '''
    Vérifie que la lettre n'a pas déjà été dite
    
    @raise LettreDejaTrouveeException: Si la lettre a déjà été dite
    '''
    if(pLettre in pLettresDites):
        raise LettreDejaTrouveeException()
    
def saisirLettre(pLettresDites):
    '''
    Effectue la saisie d'une lettre.
    Si la lettre saisie est dans la liste des lettres déjà tapées, la saisie est refaite
    
    @param pLettresTrouvees: Liste des lettres déjà tapées
    
    @return: La lettre saisie
    '''
    lettre = input("Veuillez saisir une lettre : ")
    
    try :
        verifierLettre(lettre)
        verifierLettreDejaSaisie(lettre, pLettresDites)
    except SaisieException:
        print("Erreur : {0} n'est pas une lettre !".format(lettre))
        lettre = saisirLettre(pLettresDites)
    except LettreDejaTrouveeException:
        print("Vous avez déjà saisi cette lettre !")
        lettre = saisirLettre(pLettresDites)
    
    return lettre

def afficherPendu(pCoupsRestants):
    '''
    Affiche la sprite correspondante au nombre d'échecs du joueurs
    '''
    print("\n{0}\n".format(dessinPendu[10-pCoupsRestants]))