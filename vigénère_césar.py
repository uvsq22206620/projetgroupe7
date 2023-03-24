#PROJET D'INFORMATIQUE POUR LE S2# 

#Pour l'instant il s'agit de creer des fonctions qui ont pour but de chiffrer et dechiffrer#

#PREMIERE ETAPE#
#Dans un premier temps, il faudra programmer en python le code de césar,le chiffre de Vigenère ainsi que la scytale, et une substitution monoalpha-bétique générale.#


#Le code de César#

def chiffrer_cesar(texte, decalage):
    resultat = "" # On initialise une variable qui stockera le texte chiffré
    for caractere in texte: # Pour chaque caractère dans le texte
        if caractere.isalpha(): # Si le caractère est une lettre de l'alphabet
            num = ord(caractere) # On calcule son code ASCII
            num += decalage # On effectue le décalage
            if caractere.islower(): # Si le caractère est une lettre minuscules
                if num > ord('z'): # Si le décalage a dépassé la fin de l'alphabet minuscules
                    num -= 26 # On soustrait 26 pour revenir à la première lettre de l'alphabet
                elif num < ord('a'): # Si le décalage a dépassé le début de l'alphabet minuscules
                    num += 26 # On ajoute 26 pour revenir à la dernière lettre de l'alphabet
            # Le même traitement s'applique pour les majuscules
            resultat += chr(num) # On ajoute le caractère chiffré au résultat
        else: # Si le caractère n'est pas une lettre de l'alphabet
            resultat += caractere # On ajoute le caractère sans modification au résultat
    return resultat # On retourne le résultat final

texte = input("Entrez le texte à chiffrer : ") # On demande le texte à chiffrer à l'utilisateur
decalage = int(input("Entrez le décalage souhaité : ")) # On demande le décalage à l'utilisateur

resultatchiffrécesar = chiffrer_cesar(texte, decalage) # On appelle la fonction pour chiffrer le texte
print("Texte chiffré :", resultatchiffrécesar) # On affiche le résultat final





def dechiffrer_cesar(texte, decalage):
    resultat = "" # On initialise une variable qui stockera le texte déchiffré
    for caractere in texte: # Pour chaque caractère dans le texte chiffré
        if caractere.isalpha(): # Si le caractère est une lettre de l'alphabet
            num = ord(caractere) # On calcule son code ASCII
            num -= decalage # On effectue l'opération inverse du décalage
            if caractere.islower(): # Si le caractère est une lettre minuscules
                if num > ord('z'): # Si le décalage a dépassé la fin de l'alphabet minuscules
                    num -= 26 # On soustrait 26 pour revenir à la première lettre de l'alphabet
                elif num < ord('a'): # Si le décalage a dépassé le début de l'alphabet minuscules
                    num += 26 # On ajoute 26 pour revenir à la dernière lettre de l'alphabet
            # Le même traitement s'applique pour les majuscules
            resultat += chr(num) # On ajoute le caractère déchiffré au résultat
        else: # Si le caractère n'est pas une lettre de l'alphabet
            resultat += caractere # On ajoute le caractère sans modification au résultat
    return resultat # On retourne le résultat final

texte = input("Entrez le texte à déchiffrer : ") # On demande le texte à déchiffrer à l'utilisateur
decalage = int(input("Entrez le décalage souhaité : ")) # On demande le décalage à l'utilisateur

resultatdechiffrécesar = dechiffrer_cesar(texte, decalage) # On appelle la fonction pour déchiffrer le texte
print("Texte déchiffré :", resultatdechiffrécesar) # On affiche le résultat final






















#Le chiffre de Vigenere#

def chiffre_vigenere(texte_clair, clef):
    # Convertir le texte en minuscules
    texte_clair = texte_clair.lower()
    # Convertir la clef en minuscules
    clef = clef.lower()
    # Initialiser le texte chiffré vide
    texte_chiffre = ""
    # Boucle sur chaque caractère du texte clair
    for i, caractere in enumerate(texte_clair):
        # Si le caractère n'est pas une lettre, le copier tel quel dans le texte chiffré
        if not caractere.isalpha():
            texte_chiffre += caractere
        # Si le caractère est une lettre, l'ajouter au texte chiffré en utilisant la méthode de Vigenère
        else:
            decalage = ord(clef[i % len(clef)]) - ord('a')
            texte_chiffre += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
    # Retourner le texte chiffré
    return texte_chiffre




def dechiffre_vigenere(texte_chiffre, clef):
    # Convertir le texte chiffré en minuscules
    texte_chiffre = texte_chiffre.lower()
    # Convertir la clef en minuscules
    clef = clef.lower()
    # Initialiser le texte clair vide
    texte_clair = ""
    # Boucle sur chaque caractère du texte chiffré
    for i, caractere in enumerate(texte_chiffre):
        # Si le caractère n'est pas une lettre, le copier tel quel dans le texte clair
        if not caractere.isalpha():
            texte_clair += caractere
        # Si le caractère est une lettre, l'ajouter au texte clair en utilisant la méthode de Vigenère
        else:
            decalage = ord(clef[i % len(clef)]) - ord('a')
            texte_clair += chr((ord(caractere) - ord('a') - decalage + 26) % 26 + ord('a'))
    # Retourner le texte clair
    return texte_clair
