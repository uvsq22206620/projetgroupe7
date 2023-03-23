def scytale_espace_e(texte,diametre):
    l=[] #initialisation de la liste qui contiendra les colonnes pour le chiffrement
    for i in range(diametre): #boucle qui prend en paramètre le diamètre 
        l.append("") 
    result="" #initialisation de la variable qui contiendra le message chiffré
    for i in range(len(texte)): #boucle qui parcoure le texte
        l[i%diametre]+=texte[i] #pour inserer les lettres colonne par colonne
    for y in l: #parcoure la liste
        result+=y #on ajoute les colonnes 1 a 1 dans le résultat
    return result

print(scytale_espace_e("un message",3))

'''
def scytale_espace_d(texte, diametre):   
    return scytale_espace_e(len(texte) // diametre, texte)
print(scytale_espace_d("umsenea sg", 3))
'''
            

    