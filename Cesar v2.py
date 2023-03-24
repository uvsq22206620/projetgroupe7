def chiffrement_cesar(texte_clair, decalage, alphabet):
  # Initialisation d'une variable qui va stocker le texte chiffré
  texte_chiffre = ""
  
  # Boucle qui parcourt chaque caractère du texte clair
  for caractere in texte_clair:
    
    # Vérification si le caractère est présent dans l'alphabet
    if caractere.lower() in alphabet:
      
      # Récupération de la position du caractère dans l'alphabet
      position = alphabet.index(caractere.lower())
      
      # Calcul de la nouvelle position en utilisant le décalage
      position_decalee = (position + decalage) % len(alphabet)
      
      # Récupération du caractère chiffré en utilisant la nouvelle position
      caractere_chiffre = alphabet[position_decalee].upper() if caractere.isupper() else alphabet[position_decalee].lower()
      
      # Ajout du caractère chiffré au texte chiffré
      texte_chiffre += caractere_chiffre
      
    # Si le caractère n'est pas dans l'alphabet, il est ajouté au texte chiffré sans modification
    else:
      texte_chiffre += caractere
  
  # Retour du texte chiffré
  return texte_chiffre

# Demande à l'utilisateur de saisir l'alphabet à utiliser
alphabet = input("Entrez l'alphabet à utiliser (exemple : 'abcdefghijklmnopqrstuvwxyz'): ")

# Demande à l'utilisateur de saisir le nom du fichier ou le texte à chiffrer
texte_clair = input("Entrez le nom du fichier à chiffrer ou le texte à chiffrer : ")

# Tentative d'ouverture du fichier si l'entrée correspond à un nom de fichier
try:
  with open(texte_clair, 'r') as fichier:
    texte_clair = fichier.read()
# Si l'ouverture du fichier échoue, l'entrée est considérée comme un texte en clair
except:
  pass

# Demande à l'utilisateur de saisir le décalage à utiliser
decalage = int(input("Entrez le décalage : "))

# Appel de la fonction de chiffrement de César en utilisant le texte clair, le décalage et l'alphabet
texte_chiffre = chiffrement_cesar(texte_clair, decalage, alphabet)

# Affichage du texte chiffré
print("Texte chiffré :\n" + texte_chiffre)
