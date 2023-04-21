# projetgroupe7
MI - TD-03


dépot du projet du groupe 7 - Anissa Kourban, Kaïs Rosenthal, Schneid Toussaint

https://github.com/uvsq22206620/projetgroupe7/

UTILISATION DU PROGRAMME : 
Le but de ce programme est de chiffrer des messages avec plusieurs types de chiffrements. Ici, nous avons codé 4 types de chiffrements : la Scytale, le César, le Vigénère, et la substitution monoalphabétique. On nous a également demandé de faire une attaque contre nos programmes : on a donc décidé de faire l'attaque brute force sur chacun de nos codes.

La Scytale (Partie d'Anissa) : 
Le chiffrement de la Scytale est un chiffrement par transposition. Il est l'un des plus anciens dispositifs de cryptographie (les Spartiates). Il consiste à prendre un texte et mettre chaque lettre du texte dans chaque case d'une grille. On aura une clé qui représente le nombre de colonnes, et le but de notre code Scytale est de pivoter la grille en laissant chaque caractère à la position initiale et essayer d'y retrouver un texte clair.


Explication Cesar et Vigenere ( Partie de Kaïs)

Cesar : - Le chiffrement César est l'un des premiers exemples connus de chiffrement par substitution. Il a été utilisé par Jules César pour communiquer avec ses généraux pendant les guerres. Le chiffrement consiste à décaler chaque lettre d'un certain nombre de positions dans l'alphabet.
Par exemple, si le décalage est de 3, la lettre "A" devient "D", la lettre "B" devient "E", et ainsi de suite. Le décalage est généralement représenté par un nombre entier compris entre 1 et 25.
Le code de César en Python utilise cette idée de décalage pour chiffrer un message en remplaçant chaque lettre par une lettre décalée. Le code utilise la fonction chr() pour convertir un entier en caractère ASCII et ord() pour convertir un caractère ASCII en entier.
La fonction caesar_cipher prend un message et une valeur de décalage (ou shift) comme arguments. Elle itère sur chaque caractère du message et applique le décalage

- Ce code définit une fonction dechiffrement_cesar qui prend un message chiffré et une valeur de décalage comme arguments et renvoie le message déchiffré correspondant. La fonction itère sur chaque caractère du message chiffré et applique le décalage 
l'attaque la plus logique pour un chiffrement tel que le code de cesar serait de le faire via brute force ,  cra il n'y a que 26 possibilité en theorie, 

VIGENERE : Le chiffre de Vigenère est une technique de chiffrement par substitution polyalphabétique inventée par le cryptographe français Blaise de Vigenère au 16ème siècle. Il s'agit d'une extension du chiffre de César, qui utilise un décalage fixe pour chiffrer le texte.
Dans le chiffre de Vigenère, un mot-clé est utilisé pour déterminer une série de décalages pour chaque lettre du texte en clair. Chaque lettre du texte en clair est ensuite décalée en utilisant le décalage correspondant de la série pour obtenir le texte chiffré. Le mot-clé est répété autant de fois que nécessaire pour couvrir tout le texte en clair.
Ce code utilise une clé secrète appelée cle pour cacher le message texte_clair. La clé est transformée en une liste de nombres en utilisant la fonction ord, qui donne le code ASCII d'une lettre. Le message clair est aussi transformé en une liste de nombres.
Ensuite, pour chaque lettre du message clair, nous utilisons la clé pour cacher la lettre en utilisant (texte_clair_en_nombres[i] + cle_en_nombres[i % longueur_cle]) % 26. La lettre cachée est ensuite transformée en une lettre lisible en utilisant la fonction chr et ajoutée à la variable texte_chiffre.
Le résultat final est le message caché sous forme de chaîne de lettres.
L'attaque la plus courante pour casser un chiffre de Vigenère est l'analyse fréquentielle, qui exploite la répartition statistique des caractères dans une langue donnée pour essayer de déterminer la longueur de la clé et de la déchiffrer. Voici les étapes générales de cette attaque :
Déterminer la longueur probable de la clé : on peut le faire en utilisant des techniques telles que l'index de coïncidence, qui mesure la probabilité que deux caractères choisis au hasard soient identiques.
Diviser le texte chiffré en sous-textes correspondant à chaque lettre de la clé : on peut le faire en regroupant les caractères de même position dans le texte chiffré, en fonction de la longueur probable de la clé.
Déterminer la clé en utilisant l'analyse fréquentielle pour chaque sous-texte : on peut le faire en comparant les distributions fréquentielles des caractères dans chaque sous-texte avec celles attendues dans la langue cible.
Déchiffrer le texte en utilisant la clé trouvée : une fois que vous avez déterminé la clé, vous pouvez la utiliser pour déchiffrer le texte entier.


La Substitution Monoalphabétique Générale (Partie de Schneid) : 
La substitution monoalphabétique générale est l'une des techniques de chiffrement les plus anciennes, qui consiste à remplacer chaque lettre d'un message initial par une autre lettre. La même lettre du message initial est toujours remplacée par la même lettre du message chiffré, peu importe sa position dans le message, cela rend la chose plus ou moins facile à décrypter par analyse de fréquence. Pour cela nous utilisons une table de substitution, qui associe à chaque lettre du message une autre lettre de l'alphabet. La table de substitution est créée en utilisant une clé de chiffrement (en l'occurrence, il s'agit de l'alphabet mélangé aléatoirement).

L'attaque brute-force : 
L'attaque brute-force (attaque par force brute) est une méthode utilisée en cryptanalyse pour trouver un mot de passe ou une clé. Il s'agit de tester, une à une, toutes les combinaisons possibles.


L'attaque par analyse de fréquence :
L'analyse de fréquence est une méthode de cryptanalyse utilisée pour déchiffrer des messages cryptés. Elle repose sur l'étude des fréquences d'apparition des lettres ou des groupes de lettres dans un texte chiffré afin de les comparer aux fréquences d'apparition attendues dans la langue utilisée pour le message. Notamment, dans la langue française, les lettres les plus utilisées sont le 'e', le 's' et le 'a'. Suite à cette connaissance, nous pouvons déduire que, si dans le message chiffré une lettre chiffrée revient systématiquement plus que les autres, elle peut être une des lettres les plus communément utilisées. 
