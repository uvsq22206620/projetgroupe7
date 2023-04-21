import random
import string
import collections


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

#CHIFFREMENT CESAR#

def chiffrement_cesar(message, clé):
    message_chiffré = ""
    for caractère in message:
        if caractère.isalpha(): # Vérifie si le caractère est une lettre
            décalage = ord(caractère) + clé # Décalage du caractère
            if caractère.isupper(): # Vérifie si la lettre est en majuscule
                if décalage > ord('Z'):
                    décalage -= 26
                message_chiffré += chr(décalage)
            elif caractère.islower(): # Vérifie si la lettre est en minuscule
                if décalage > ord('z'):
                    décalage -= 26
                message_chiffré += chr(décalage)
        elif caractère == " ": # Si le caractère est un espace
            message_chiffré += " "
        else: # Si le caractère est un caractère spécial
            message_chiffré += ""
    return message_chiffré


clé = int(input("Entrez la clé de chiffrement, soit le décalage, (un nombre entier) : "))
choix_fichier = input("Voulez-vous chiffrer un fichier .txt ? (O/N) : ")
if choix_fichier.upper() == "O":
    nom_fichier = input("Entrez le nom du fichier (avec l'extension .txt) : ")
    with open(nom_fichier, "r") as fichier:
        message = fichier.read()
        message_chiffré = chiffrement_cesar(message, clé)
        print("Message chiffré via fichier texte :", message_chiffré)

message = input("Entrez un message à chiffrer : ")
clé = int(input("Entrez la clé de chiffrement, soit le décalage, (un nombre entier) : "))

message_chiffré = chiffrement_cesar(message, clé)
print("Message chiffré demandé :", message_chiffré)

#DECHIFFREMENT CESAR#

def dechiffrement_cesar(message_chiffré, clé):
    message_déchiffré = ""
    for caractère in message_chiffré:
        if caractère.isalpha(): # Vérifie si le caractère est une lettre
            décalage = ord(caractère) - clé # Décalage du caractère
            if caractère.isupper(): # Vérifie si la lettre est en majuscule
                if décalage < ord('A'):
                    décalage += 26
                message_déchiffré += chr(décalage)
            elif caractère.islower(): # Vérifie si la lettre est en minuscule
                if décalage < ord('a'):
                    décalage += 26
                message_déchiffré += chr(décalage)
        elif caractère == " ": # Si le caractère est un espace
            message_déchiffré += " "
        else: # Si le caractère est un caractère spécial
            message_déchiffré += ""
    return message_déchiffré

message_chiffré = input("Entrez un message chiffré à déchiffrer : ")
clé = int(input("Entrez la clé de déchiffrement (doit être la même que la clé de chiffrement) : "))

message_déchiffré = dechiffrement_cesar(message_chiffré, clé)
print("Message déchiffré :", message_déchiffré)

choix_fichier = input("Voulez-vous déchiffrer un fichier .txt ? (O/N) : ")
if choix_fichier.upper() == "O":
    nom_fichier = input("Entrez le nom du fichier (avec l'extension .txt) : ")
    with open(nom_fichier, "r") as fichier:
        message = fichier.read()
        message_chiffré = chiffrement_cesar(message, clé)
        print("Message chiffré via fichier texte :", message_chiffré)

#ATTAQUE POUR Cesar#

def brute_force_cesar():
    message_chiffre = input("Entrez le message chiffré : ")
    for cle in range(1, 26):
        message_dechiffre = ''
        premiere_lettre = True
        for lettre in message_chiffre:
            if lettre.isalpha():
                decalage = ord(lettre.lower()) - ord('a')
                if premiere_lettre:
                    lettre_dechiffre = chr((decalage - cle) % 26 + ord('a'))
                    premiere_lettre = False
                else:
                    lettre_dechiffre = chr((decalage - cle_prec) % 26 + ord('a'))
                cle_prec = cle
            else:
                lettre_dechiffre = lettre
            message_dechiffre += lettre_dechiffre
        print('Clé', cle, ':', message_dechiffre)



brute_force_cesar()


#VIGENERE : Partie de Kaïs

#CHIFFREMENT VIGENERE#



def vigenere_chiffrement(texte="", cle="", fichier="", supprimer_espaces=True, supprimer_caracteres=True):
    if not texte and not fichier:
        print("Aucun texte ou fichier à chiffrer n'a été fourni.")
        return ""
    
    if fichier:
        try:
            with open(fichier, "r") as f:
                texte = f.read()
        except FileNotFoundError:
            print("Le fichier spécifié n'a pas été trouvé.")
            return ""
    
    texte_chiffre = ""
    i = 0
    for char in texte:
        if char.isalpha():
            # Convertir le caractère en sa position dans l'alphabet (0-25)
            char_position = ord(char.lower()) - 97
            cle_position = ord(cle[i % len(cle)].lower()) - 97
            # Chiffrer le caractère en utilisant la clé de Vigenère
            chiffre_position = (char_position + cle_position) % 26
            chiffre_char = chr(chiffre_position + 97)
            # Ajouter le caractère chiffré au texte chiffré
            texte_chiffre += chiffre_char
            i += 1
        elif char.isspace() and not supprimer_espaces:
            # Ajouter l'espace au texte chiffré si l'utilisateur a choisi de ne pas supprimer les espaces
            texte_chiffre += " "
        elif not char.isalpha() and not char.isspace() and not supprimer_caracteres:
            # Ajouter le caractère spécial au texte chiffré si l'utilisateur a choisi de ne pas supprimer les caractères spéciaux
            texte_chiffre += char
    
    return texte_chiffre

# Demander à l'utilisateur le texte à chiffrer et la clé de Vigenère
texte_a_chiffrer = input("Entrez le texte à chiffrer (laissez vide si vous voulez chiffrer un fichier) : ")
cle_de_vigenere = input("Entrez la clé de Vigenère : ")
supprimer_espaces = input("Voulez-vous supprimer les espaces ? (oui/non) ").lower() == "oui"
supprimer_caracteres = input("Voulez-vous supprimer les caractères spéciaux ? (oui/non) ").lower() == "oui"

# Demander à l'utilisateur s'il veut chiffrer un fichier
chiffrer_fichier = input("Voulez-vous chiffrer un fichier ? (oui/non) ").lower() == "oui"
if chiffrer_fichier:
    nom_fichier = input("Entrez le nom du fichier à chiffrer : ")
else:
    nom_fichier = ""

# Chiffrer le texte ou le contenu du fichier en utilisant la clé de Vigenère et afficher le texte chiffré
texte_chiffre = vigenere_chiffrement(texte_a_chiffrer, cle_de_vigenere, nom_fichier, supprimer_espaces, supprimer_caracteres)
print("Le texte chiffré est :", texte_chiffre)

#DECHIFFREMENT VIGENERE#


def vigenere_dechiffrement(texte="", cle="", fichier="", supprimer_espaces=True, supprimer_caracteres=True):
    if not texte and not fichier:
        print("Aucun texte ou fichier à déchiffrer n'a été fourni.")
        return ""
    
    if fichier:
        try:
            with open(fichier, "r") as f:
                texte = f.read()
        except FileNotFoundError:
            print("Le fichier spécifié n'a pas été trouvé.")
            return ""
    
    texte_dechiffre = ""
    i = 0
    for char in texte:
        if char.isalpha():
            # Convertir le caractère en sa position dans l'alphabet (0-25)
            char_position = ord(char.lower()) - 97
            cle_position = ord(cle[i % len(cle)].lower()) - 97
            # Déchiffrer le caractère en utilisant la clé de Vigenère
            dechiffre_position = (char_position - cle_position) % 26
            dechiffre_char = chr(dechiffre_position + 97)
            # Ajouter le caractère déchiffré au texte déchiffré
            texte_dechiffre += dechiffre_char
            i += 1
        elif char.isspace() and not supprimer_espaces:
            # Ajouter l'espace au texte déchiffré si l'utilisateur a choisi de ne pas supprimer les espaces
            texte_dechiffre += " "
        elif not char.isalpha() and not char.isspace() and not supprimer_caracteres:
            # Ajouter le caractère spécial au texte déchiffré si l'utilisateur a choisi de ne pas supprimer les caractères spéciaux
            texte_dechiffre += char
    
    return texte_dechiffre

# Demander à l'utilisateur le texte à déchiffrer et la clé de Vigenère
texte_a_dechiffrer = input("Entrez le texte à déchiffrer (laissez vide si vous voulez déchiffrer un fichier) : ")
cle_de_vigenere = input("Entrez la clé de Vigenère : ")
supprimer_espaces = input("Voulez-vous supprimer les espaces ? (oui/non) ").lower() == "oui"
supprimer_caracteres = input("Voulez-vous supprimer les caractères spéciaux ? (oui/non) ").lower() == "oui"

# Demander à l'utilisateur s'il veut déchiffrer un fichier
dechiffrer_fichier = input("Voulez-vous déchiffrer un fichier ? (oui/non) ").lower() == "oui"
if dechiffrer_fichier:
    nom_fichier = input("Entrez le nom du fichier à déchiffrer : ")
else:
    nom_fichier = ""

# Déchiffrer le texte ou le contenu du fichier en utilisant la clé de Vigenère et afficher le texte déchiffré
texte_dechiffre = vigenere_dechiffrement(texte_a_dechiffrer, cle_de_vigenere, nom_fichier, supprimer_espaces, supprimer_caracteres)
print("Le texte déchiffré est :", texte_dechiffre)


#ATTAQUE POUR VIGENERE - ANALYSE DE FREQUENCE TENTATIVE #


def casser_vigenere(texte_chiffre, langue='fr'):
    # Charger les fréquences attendues pour la langue choisie
    with open(f'{langue}_freq.txt') as f:
        freq_attendues = [float(x.strip().split()[1]) for x in f]

    # Trouver la longueur probable de la clé
    def indice_de_coincidence(ct):
        return sum(c1 == c2 for c1, c2 in zip(ct, ct[1:])) / (len(ct) - 1)
    longueur_max_cle = 1
    max_indice = 0
    for i in range(2, len(texte_chiffre)):
        indice = sum(indice_de_coincidence(texte_chiffre[j::i]) for j in range(i)) / i
        if indice > max_indice:
            max_indice = indice
            longueur_max_cle = i

    # Trouver la clé
    def decrypter(longueur_cle, decalage):
        texte_clair = ''
        for i, c in enumerate(texte_chiffre):
            k = ord(cle[i % longueur_cle]) - ord('A')
            p = chr((ord(c) - ord('A') - k + 26 - decalage) % 26 + ord('A'))
            texte_clair += p
        return texte_clair
    cle = ''
    for i in range(longueur_max_cle):
        sous_texte = ''.join(texte_chiffre[j] for j in range(i, len(texte_chiffre), longueur_max_cle))
        freq = collections.Counter(sous_texte)
        max_correlation = 0
        meilleur_decalage = 0
        for decalage in range(26):
            correlation = 0
            for j, c in enumerate(sorted(freq.keys())):
                correlation += freq[c] * freq_attendues[(ord(c) - ord('A') - decalage) % 26]
            if correlation > max_correlation:
                max_correlation = correlation
                meilleur_decalage = decalage
        cle += chr(meilleur_decalage + ord('A'))
    return cle, decrypter(longueur_max_cle, 0)

# Exemple d'utilisation
texte_chiffre = 'BJQSXQJHVYUBYQBJHVYUBYQBJHVYU'
cle, texte_clair = casser_vigenere(texte_chiffre)
print(f'Clé : {cle}')
print(f'Texte : {texte_clair}')



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





#TENTATIVE ATTAQUE ANALYSE DE FRÉQUENCE SUR LA SUBSTITUTION MONOALPHABÉTIQUE

def decryptage_substitution(message_code=""):


    frequences_attendues_langue_francaise ={'a': 9.42, 'b': 1.02, 'c': 2.64, 'd': 3.39, 'e': 15.87, 'f': 0.95, 'g': 1.04, 'h': 0.77, 'i': 8.41, 'j': 0.89, 'k': 0.00, 'l': 5.34, 'm': 3.24, 'n': 7.15, 'o': 5.14, 'p': 2.86, 'q': 1.06, 'r': 6.46, 's': 7.90, 't': 7.26, 'u': 6.24, 'v': 2.15, 'w': 0.00, 'x': 0.30, 'y': 0.24, 'z': 0.32} #fréquence attendues des lettres dans la langue française
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    
    frequence_mot_chiffre = {} #on crée un dictionnaire pour stocker les lettres du mot codé et leur fréquence d'apparition
    for lettre in message_code : 
        if lettre not in frequence_mot_chiffre :
            frequence_mot_chiffre[lettre] = 1 #si la lettre n'est pas enregistrée dans le dictionnaire, maintenant elle existe et on y associe sa fréquence qui est de 1
        else :
            frequence_mot_chiffre[lettre] += 1 #si la lettre est déjà dans le dictionnaire, on ajoute à la valeur précédente + 1


    mot_dechiffre = message_code #mis en place d'une nouvelle variable que l'on va modifier afin de ne pas perdre la précédente
    
    while len(frequence_mot_chiffre) > 0 : #on parcout tout le dictionnaire qui stocke les lettres codés
        valeur_maximale = max(frequence_mot_chiffre, key=frequence_mot_chiffre.get) #on stocke la lettre associée à l'élement le plus élevé dans notre mot codé
        if valeur_maximale in alphabet: #car les espaces peuvent être le caractère qui revient le plus et pourtant l'espace n'est pas codé
            lettre_correspondante = max(frequences_attendues_langue_francaise, key=frequences_attendues_langue_francaise.get) #on récupère la lettre qui revient le plus de fois dans l'alphabet
            mot_dechiffre = mot_dechiffre.replace(valeur_maximale, lettre_correspondante)
            del frequences_attendues_langue_francaise[lettre_correspondante]
        del frequence_mot_chiffre[valeur_maximale] # on supprime les lettres qui ont la plus grande fréquence dans la langue française et celle qui apparait le plus de fois dans le mot pour qu'il y ait un nouvel maxim
    
    #RETOUR DU MOT DECHIFFRE
    return mot_dechiffre

print (decryptage_substitution(input("Saisir le message chiffré à déchiffrer")))


#ATTAQUE POUR VIGENERE - ANALYSE DE FREQUENCE TENTATIVE #

def casser_vigenere(texte_chiffre, langue='fr'):
    # Charger les fréquences attendues pour la langue choisie
    with open(f'{langue}_freq.txt') as f:
        freq_attendues = [float(x.strip().split()[1]) for x in f]

    # Trouver la longueur probable de la clé
    def indice_de_coincidence(ct):
        return sum(c1 == c2 for c1, c2 in zip(ct, ct[1:])) / (len(ct) - 1)
    longueur_max_cle = 1
    max_indice = 0
    for i in range(2, len(texte_chiffre)):
        indice = sum(indice_de_coincidence(texte_chiffre[j::i]) for j in range(i)) / i
        if indice > max_indice:
            max_indice = indice
            longueur_max_cle = i

    # Trouver la clé
    def decrypter(longueur_cle, decalage):
        texte_clair = ''
        for i, c in enumerate(texte_chiffre):
            k = ord(cle[i % longueur_cle]) - ord('A')
            p = chr((ord(c) - ord('A') - k + 26 - decalage) % 26 + ord('A'))
            texte_clair += p
        return texte_clair
    cle = ''
    for i in range(longueur_max_cle):
        sous_texte = ''.join(texte_chiffre[j] for j in range(i, len(texte_chiffre), longueur_max_cle))
        freq = collections.Counter(sous_texte)
        max_correlation = 0
        meilleur_decalage = 0
        for decalage in range(26):
            correlation = 0
            for j, c in enumerate(sorted(freq.keys())):
                correlation += freq[c] * freq_attendues[(ord(c) - ord('A') - decalage) % 26]
            if correlation > max_correlation:
                max_correlation = correlation
                meilleur_decalage = decalage
        cle += chr(meilleur_decalage + ord('A'))
    return cle, decrypter(longueur_max_cle, 0)

# Exemple d'utilisation
texte_chiffre = 'BJQSXQJHVYUBYQBJHVYUBYQBJHVYU'
cle, texte_clair = casser_vigenere(texte_chiffre)
print(f'Clé : {cle}')
print(f'Texte : {texte_clair}')

