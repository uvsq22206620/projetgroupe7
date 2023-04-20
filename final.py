import random
import string


#SCYTALE : Partie d'Anissa

def demande() -> str:
    
    """ fonction demande qui permet de demander à l'utilisateur 
    si il veut entrer un texte directement ou 
    un chemin vers un fichier.txt dans l'ordinateur. 
    """
    
    a = input("voulez vous entrer un texte ou un fichier texte? \n" + "entrer 'Texte' ou 'Fichier' : ")
    
    if a == "Fichier": #si l'utilisateur veut entrer un fichier .txt
        b = input("choisir un chemin .txt : ") 
        f = open(str(b), "r") # commande qui ouvre un fichier et qui le lit
        h = f.readlines() #récupère les caractères du fichier
        texte = ""
        for i in range(len(h)): #boucle qui va transformer la liste en str
            texte += h[i]
        
    elif a == "Texte": #si l'utilisateur veut entrer un texte 
         texte = input("entrer un texte : ")
    else: 
        print("erreur")
        return
    return texte



def scytale_encrypt(texte : str, diametre : int) ->str: 
    """fonction qui encrypte un texte en utilisant la technique de chiffrement de la Scytale"""

    l=[] #Liste qui contiendra les colonnes pour le chiffrement
    #Création de l'espace nécessaire dans la liste
    for i in range(diametre):
        l.append("") 
    
    result="" #Variable qui contiendra le message chiffré
    
    #Parcours le texte pour insérer les lettres lignes par lignes
    for i in range(len(texte)):
        l[i % diametre] += texte[i]
  #  print(l)
    #pour afficher en string
    for y in l: #parcours la liste
        result += y #on ajoute les colonnes 1 a 1 dans le résultat
    
    return result


def scytale_decrypt(texte_d : str, diametre : int):
    """fonction qui décrypte un texte en utilisant la technique de chiffrement de la Scytale"""

    reste = len(texte_d)%diametre #savoir si il y a un reste dans les colonnes
    if reste == 0: #si le reste est égal à 0
        nb_column = len(texte_d)//diametre #division entiere de la taille du texte et le diametre
    elif reste !=0:
        nb_column = len(texte_d)//diametre + 1 #division entiere de la taille du texte et le diametre + 1 pour être certain d'avoir assez de colonnes 



    row_tab = [] #liste qui sert à sauver chq élément de chq ligne
    row = []
    for i in range(diametre):
        row_copy=row.copy() #permet de copier la liste
        row_tab.append(row_copy) #ajoute la copie de la liste dans row_tab

    cpt = 0 #compteur pour parcourir tout le texte
    b = 0 
    for i in range(diametre): #boucle qui va parcourir chq ligne en faisant attention à ne pas dépasser le nombre d'él de la ligne
        if len(texte_d)%diametre !=0: 
            if reste >0:
                b = 0
            elif reste<=0:
                b = -1
        for j in range(nb_column+b):
            row_tab[i].append(texte_d[cpt])
            cpt+=1
        reste-=1


    new_text = ""
    c=0
    for i in range(nb_column): #double boucle qui permet d'explorer le message ligne par ligne 
        for j in range(diametre):
            new_text+=row_tab[j][i]
            c+=1
            if c == len(texte_d):
                break #obligés d'arrêter la boucle sinon elle tourne...
    return new_text


def brute_force_scytale(texte, n):
    """fonction qui permet d'attaquer la Scytale en force brute"""
    lst = []
    for i in range(1, n+1): #boucle qui va tester toutes les possibilités de diamètre de 1 jusqu'au nombre voulu
        lst += [scytale_decrypt(texte, i), i]
    return lst
    
print(scytale_encrypt(demande(),4))
print(scytale_decrypt(demande(), 4))   
print(brute_force_scytale(demande(), 6))


#CÉSAR : Partie de Kaïs

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


def brute_force_cesar(texte, n):
    l = []
    for i in range(1, n+1):
        l += [dechiffrer_cesar(texte, i), i ]
    return l 
print(brute_force_cesar(chiffrer_cesar(texte, decalage), 17))


#VIGENERE : Partie de Kaïs

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
print(chiffre_vigenere('un message', 3))



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
print(dechiffre_vigenere('un message', 3))



# SUBSTITUTION MONOALPHABÉTIQUE : Partie de Schneid 


dictionnaire = {}

def encryptage_substitution (message= ""):

    #DEMANDER A L'UTILISATEUR DE SUPPRIMER LES CARACTERES SPECIAUX ET/OU LES ESPACES
    supprimer_caracteres_speciaux = input ("Souhaitez-vous supprimer les caractères spéciaux ? (Répondre par 'oui' ou 'non')")
    while supprimer_caracteres_speciaux.lower() not in ["oui", "non"]: #on met tous les caractères du message en minuscule
        supprimer_caracteres_speciaux = input ("Souhaitez-vous supprimer les caractères spéciaux ? Une réponse par 'oui' ou 'non' est obligatoire")
    
    supprimer_espaces = input ("Souhaitez-vous supprimer les espaces ? (Répondre par 'oui' ou 'non')")
    while supprimer_espaces.lower() not in ["oui", "non"]:
        supprimer_espaces = input ("Souhaitez-vous supprimer les espaces ? Une réponse par 'oui' ou 'non' est obligatoire")

    #MIS EN PLACE DES VARIABLES
    liste = []
    mot_code = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    caracteres_speciaux = string.punctuation #on place l'ensemble des caractères spéciaux dans une chaîne de caractère. 
    alphabet_melange = random.sample(alphabet, len(alphabet)) #fonction qui permet de melanger aléatoirement une chaîne de caractère, ici c'est l'alphabet. Alphabet mélangé va donc devenir notre clé de chiffrement

    #REMPLACEMENT DES ESPACES ET SUPPRESSION DES CARACTERES SPECIAUX
    if supprimer_espaces.lower() == "oui" :
        message = message.replace(" ", "") #on remplace tous les espaces par du "vide", si l'utilisateur décide de les supprimer

    if supprimer_caracteres_speciaux.lower() == "oui" : #on réutilise 'if' car ces deux propositions doivent être vérifiées
        for lettre in message.lower(): 
            if lettre not in caracteres_speciaux :
                liste.append(lettre) #si l'utilisateur décide de supprimer tous les caractères spéciaux, on ajoute à la liste uniquement ce qui n'est pas un caractère spécial

    elif supprimer_caracteres_speciaux.lower() == "non" and supprimer_espaces.lower() == "non":
        for lettre in message.lower():
            liste.append(lettre) #si l'utilisateur décide au contraire de conserver les caractères spéciaux et les espaces, le message est placé caractères par caractères dans une liste

    #SUBSTITUTION
    for lettre in liste: 
        if lettre in alphabet :
            mot_code += alphabet_melange[alphabet.index(lettre)]#si le caractère est une lettre de l'alphabet, on ajoute au mot codé, la lettre positionnée à la même position dans l'alphabet mélangé, que la lettre initial dans l'alphabet normal.
        else :
            mot_code += lettre #on ajoute à la chaîne de caractère notre caractère codé

    #FIN DE LA FONCTION, RETOUR DU MOT CODE
    return mot_code



#CODER UN MESSAGE
coder_un_message = input("Souhaitez-vous coder un message ? (Répondre par 'oui' ou 'non')")
while coder_un_message.lower() not in ["oui", "non"]: 
    coder_un_message = input("Souhaitez-vous coder un message ? Une réponse par 'oui' ou par 'non' est obligatoire)")
if coder_un_message == 'oui' :
    message_chiffre = encryptage_substitution(message = input("Saisir le message à coder"))
    print("le message codé est :", message_chiffre)


#CODER UN FICHIER TEXTE 
coder_un_fichier_texte = input("Souhaitez-vous coder un fichier texte ? Répondre par 'oui' ou par 'non'")

if coder_un_fichier_texte.lower() == "oui" :
    nom_du_fichier = input("Entrez le nom du fichier avec l'extension '.txt'")
    with open(nom_du_fichier, "r") as fichier :
        message_fichier = fichier.read()
        mot_code = encryptage_substitution(message_fichier)
        print ("Le message du fichier codé est :", mot_code)




def decryptage_substitution(message_code=""): 

    #MIS EN PLACE DE VARIABLES POUR LA FONCTION
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cle_de_dechiffrement = random.sample(alphabet, len(alphabet))
    message_dechiffre = ""
    


    #DECHIFFREMENT PAR FORCE BRUTE
    for caractere in message_code:
        if caractere in alphabet:
            message_dechiffre += cle_de_dechiffrement[alphabet.index(caractere)] #on fait le chemin inverse de l'encryptage jusqu'à trouver la bonne combinaison, si le caractère dans le message n'est pas une lettre alors il n'a pas été codé et est ajouté tel quel au mot 
        else:
            message_dechiffre += caractere

    #FIN DE LA FONCTION, RETOUR DE LA VARIABLE
    return message_dechiffre



#MIS EN PLACE DE VARIABLES
message_code = input("Entrez le message chiffré à déchiffer")
nombre_de_tentatives = int(input("Entrez le nombre de tentatives que vous souhaitez voir (choisir NECESSAIREMENT un nombre positif (ou nul))")) #si le nombre de tentative = 0 alors le code ne rend pas de valeur


#NOMBRE DE TENTATIVES
for i in range(nombre_de_tentatives):
    essai = decryptage_substitution(message_code)
    if essai not in dictionnaire :
        dictionnaire[essai] = 1 #si la lettre n'est pas enregistrée dans le dictionnaire, maintenant elle y existe et on y associe sa 'fréquence' qui est de 1
        print (essai) #on renvoit ensuite ce que le programme a déchiffré à l'utilisateur
    else :
        continue #si la lettre est déjà dans le dictionnaire, le programme ne le renvoit pas (pour éviter de trouver des similitudes dans ce que peut envoyer python), et continue de le décrypter jusquà 'nombres_de_tentatives'



