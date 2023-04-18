def scytale_encrypt(texte,diametre):
    global l
    l=[] #Liste qui contiendra les colonnes pour le chiffrement

    #Création de l'espace nécessaire dans la liste
    for i in range(diametre): 
        l.append("") 

    result="" #Variable qui contiendra le message chiffré

    #Parcours le texte pour insérer les lettres lignes par lignes
    for i in range(len(texte)):
        l[i % diametre] += texte[i]

    #pour afficher en string
    for y in l: #parcours la liste
        result += y #on ajoute les colonnes 1 a 1 dans le résultat

    return result

print(scytale_encrypt("messager tres mesquin",3))

def scytale_decrypt(texte,diametre):
    #Liste qui contiendra les colonnes pour le chiffrement
    liste_colonnes = []
    #Création de l'espace nécessaire dans la liste
    for i in range(len(max(l))):
        for j in range(diametre): # Exploration des sous-listes
            liste_colonnes += l[j][i] # On ajoute les valeurs des colonnes dans des listes
    result = "" #Variable qui contiendra le message chiffré
    #Parcours le texte pour insérer les lettres colonnes par colonnes
    for i in range(len(texte)):
        l[i % diametre] += texte[i]

    # Transforme la liste en chaine de caractère
    for y in liste_colonnes:
        result += y

    return result

print(scytale_decrypt(scytale_encrypt("messager tres mesquin",3), 3))

