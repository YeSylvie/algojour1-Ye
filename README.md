#Cours d'algorithme jour 1 

### Groupe TD8 : 
* TRICHET Laura
* YE Sylvie

### Sujet :
Comparaison de plusieurs algorithmes de tri en Python

1. Tri à bulle    


   De la gauche vers la droite, on prend les deux premières valeurs et on les compare. Si parmi ces deux valeurs, celle de 
   droite est plus petite que celle de gauche, alors on les inverve. Ensuite, on répète le procédé avec la deuxième et 
   troisième valeur, troisième et quatrième valeur, etc. 
   Une fois toute la liste parcourue, la plus grande valeur se trouvera tout à droite.
   On répète ce procédé en repartant de la première valeur de la liste jusqu'à n-1 ( n = taille de la liste).  

2. Tri par sélection    


    a. Première méthode


Pour i, allant de 0 jusqu'à n (n = taille de la liste), on cherche la position de la valeur minimale (à partir de i + 1) 
de cette liste et on l'inverse avec celle à la position i.

    b. Deuxième méthode   
   
On parcourt la liste pour trouver la valeur minimale et on la stock dans une deuxième liste.
On supprime cette valeur de la liste initiale, et on répète le procédé jusqu'à que la liste initiale soit vide.
Ainsi, on obtient une nouvelle liste avec les valeurs de la liste initiale triées.

3. Tri par insertion 
   
On prend la valeur à la position i + 1 de la liste et on la compare avec celles allant de 0 jusqu'à i. Si elle est plus 
petite que l'une d'entre elles, on insère cette valeur à la bonne position. Ce qui fait que les positions des autres 
valeurs, après celle inserée, sont décalées d'un rang vers la droite. Le tableau sera donc trié de la gauche vers la droite.

4. Tri par fusion 
   
On exécute de manière récursive une méthode qui divise en deux la liste initiale jusqu'à obtenir uniquement des 
listes avec une seule valeur. Ensuite, on fusionne deux à deux chacune de ces listes en les triant jusqu'à obtenir une unique liste
triée avec toutes les valeurs initiales.

5. Tri rapide

On définit un pivot (une valeur de la liste), dans notre cas ce sera la première valeur. A partir de ce pivot, on crée 
deux listes : une avec toutes les valeurs inférieures ou égale au pivot, et une autre avec toutes celles supérieures. 
Cette méthode est appelée de manière récursive jusqu'à avoir une liste avec seulement un élément ou vide. Une fois que toutes
les listes sont vides ou ne contiennent qu'un seul élément, elles sont toutes concaténées. 

#### Comparaisons des différents algorithmes
Le tri rapide et le tri fusion sont les deux algorithmes les plus rapides et stables car ils font moins de comparaison 
par rapport au trois autres algorithmes lorsqu'on est sur de longue liste de valeur.   
Le tri par sélection est le moins efficace car c'est celui qui effectue le plus de comparaison. 