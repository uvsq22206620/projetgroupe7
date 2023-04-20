# projetgroupe7
dépot du projet du groupe 7 - Anissa Kourban, Kaïs Rosenthal, Schneid Toussaint

https://github.com/uvsq22206620/projetgroupe7/

UTILISATION DU PROGRAMME : 
Le but de ce programme est de chiffrer des messages avec plusieurs types de chiffrements. Ici, nous avons codé 4 types de chiffrements : la Scytale, le César, le Vigénère, et la substitution monoalphabétique. On nous a également demandé de faire une attaque contre nos programmes : on a donc décidé de faire l'attaque brute force sur chacun de nos codes.

La Scytale (Partie d'Anissa) : 
Le chiffrement de la Scytale est un chiffrement par transposition. Il est l'un des plus anciens dispositifs de cryptographie (les Spartiates). Il consiste à prendre un texte et mettre chaque lettre du texte dans chaque case d'une grille. On aura une clé qui représente le nombre de colonnes, et le but de notre code Scytale est de pivoter la grille en laissant chaque caractère à la position initiale et essayer d'y retrouver un texte clair.


Le chiffrement de César (Partie de Kaïs) : 


Le chiffre de Vignénère (Partie de Kaïs) :


La Substitution Monoalphabétique Générale (Partie de Schneid) : 
La substitution monoalphabétique générale est l'une des techniques de chiffrement les plus anciennes, qui consiste à remplacer chaque lettre d'un message initial par une autre lettre. La même lettre du message initial est toujours remplacée par la même lettre du message chiffré, peu importe sa position dans le message, cela rend la chose plus ou moins facile à décrypter par analyse de fréquence. Pour cela nous utilisons une table de substitution, qui associe à chaque lettre du message une autre lettre de l'alphabet. La table de substitution est créée en utilisant une clé de chiffrement (en l'occurrence, il s'agit de l'alphabet mélangé aléatoirement).

L'attaque brute-force : 
L'attaque brute-force (attaque par force brute) est une méthode utilisée en cryptanalyse pour trouver un mot de passe ou une clé. Il s'agit de tester, une à une, toutes les combinaisons possibles.


L'attaque par analyse de fréquence :
L'analyse de fréquence est une méthode de cryptanalyse utilisée pour déchiffrer des messages cryptés. Elle repose sur l'étude des fréquences d'apparition des lettres ou des groupes de lettres dans un texte chiffré afin de les comparer aux fréquences d'apparition attendues dans la langue utilisée pour le message. Notamment, dans la langue française, les lettres les plus utilisées sont le 'e', le 's' et le 'a'. Suite à cette connaissance, nous pouvons déduire que, si dans le message chiffré une lettre chiffrée revient systématiquement plus que les autres, elle peut être une des lettres les plus communément utilisées. 
