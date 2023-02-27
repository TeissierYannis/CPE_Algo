L’objectif est de developper en python un module offrant le type abstrait ´ ABR. L’objet devra
disposer des methodes :
  • constructeur ( init (self))
  • insert(value) - en place, ne fait rien si value existe deja
  • delete(value) - en place
  • exist(value) - renvoie vrai ou faux
  • isEmpty() - renvoie vrai ou faux
  • clear() - en place
  • union(autre abr) - renvoie un arbre
  • intersection(autre abr) - renvoie un arbre
  • displayInfixe() -
  • displayPrefixe() -
  • displayBFS() - parcours en largeur
  • heightTree() - renvoie la hauteur de l’arbre

Dans le cas ou vous avez besoin d’une m ` ethode interm ´ ediaire, faites pr ´ efixer un double ´
underscore devant le nom de la fonction.
Essayez de faire la moitie des m ´ ethodes en r ´ ecursif et l’autre moiti ´ e en it ´ eratif. ´
Pour la methode d’affichage prefixe, essayez d’obtenir ce type d’affichage :


2 Performances
Tester plusieurs fois l’ajout de 500 entiers aleatoires entre 0 et 10000. Quelles sont les hauteurs ´
d’arbre obtenus? Tester votre code pour obtenir le profil du temps de recherche de 100 valeurs
(entre 0 et 10000) en fonction de la hauteur de l’arbre. Combien de nœuds sont visites en ´
moyenne? Que pouvez vous en dire?