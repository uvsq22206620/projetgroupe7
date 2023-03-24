def chiffrement_vigenere(texte_clair, cle, alphabet):
  # Initialisation d'une variable qui va stocker le texte chiffré
  texte_chiffre = ""
  
  # Boucle qui parcourt chaque caractère du texte clair
  for i, caractere in enumerate(texte_clair):
    
    # Vérification si le caractère est présent dans l'alphabet
    if caractere.lower() in alphabet:
      
      # Récupération de la position du caractère dans l'alphabet
      position = alphabet.index(caractere.lower())
      
      # Récupération de la position de la lettre de la clé correspondante
      position_cle = alphabet.index(cle[i % len(cle)].lower())
      
      # Calcul de la nouvelle position en utilisant la position de la clé
      position_decalee = (position + position_cle) % len(alphabet)
      
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

# Demande à l'utilisateur de saisir la clé à utiliser
cle = input("Entrez la clé à utiliser : ")

# Appel de la fonction de chiffrement de Vigenère en utilisant le texte clair, la clé et l'alphabet
texte_chiffre = chiffrement_vigenere(texte_clair, cle, alphabet)

# Affichage du texte chiffré
print("Texte chiffré :\n" + texte_chiffre)




#Le chiffre de Vigenère et le code de César sont deux algorithmes de chiffrement couramment utilisés dans l'histoire pour protéger les informations confidentielles.

#Le code de César est un algorithme de chiffrement simple où chaque lettre du message clair est décalée de n positions dans l'alphabet pour produire un message chiffré. Le nombre de positions de décalage est appelé la "clé".

#Le chiffre de Vigenère est un algorithme de chiffrement plus complexe qui utilise une clé plus longue pour décaler les caractères du message clair. Au lieu d'utiliser un seul décalage, comme dans le code de César, le chiffre de Vigenère utilise une séquence de décalages, en utilisant une lettre de la clé pour déterminer le décalage de chaque caractère du message clair.

#En résumé, le code de César est un algorithme de chiffrement simple avec une clé unique, tandis que le chiffre de Vigenère est un algorithme de chiffrement plus complexe avec une clé plus longue.#