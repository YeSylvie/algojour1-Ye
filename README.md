# Cours d'algorithme jour 1 

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

# Cours d'algorithme jour 2 

### Sujet :
Création d'une blockchaine

1. api.py    
Un fichier permettant d'exposer les APIs :

Pour les tester exécutez les commandes suivantes :   
```cd algojour2-YE```   
```export FLASK_APP=api.py```   
```flask run```   
Ensuite pour les méthodes *GET* vous pouvez les exécuter directement via un moteur de recherche, ou sur un logiciel comme *Postman*. Et pour les *PUT* et *POST*, via *Postman* uniquement.

2. block.py   

Un fichier contenant la classe *Block*. Cette classe représente un block d'une blockchaine. Elle possède les attributs :

| Attribut                  | Fonction     | 
| -------------             | -------------| 
| previous_hash             | Le hash du block précédent de la blockchaine (s'il s'agit du premier, sa valeur est *NONE*) | 
| data                      | La donnée du block      |  
| proof_of_work             | La preuve de travail     |
| creation_date             | La date de création du block     |
| hash                      | Le hash du block, qui respecte la règle de n zéro (définie lors de la création de la blockchaine)     |
| index                     | La position du block dans la blockchaine     |
| nounce                    | Le nombre de fois qu'on a regénéré le hash   |   



Elle possède les méthodes suivantes :
- is_format_hash_ok
- generate_preuvre_travail
- create_hash

Permettant de créer un block, en générant une preuve de travail, et un hash. 

3. blockchaine.py    

Un fichier contenant la classe *Blockchaine*. Cette classe représente une blockchaine et possède les attributs :

| Attribut                  | Fonction     | 
| -------------             | -------------| 
| blockchaines             | Une liste de Block, représentant la blockchaine | 
| nbr_zero                  | Le nombre de 0 à avoir en début de la chaine du hash, pour que le block soit crée      |  

Elle possède les méthodes suivantes :
- add_block
- replace_blockchaine
- delete_all
- delete_one
- is_format_all_hash_valid
- is_all_hash_equal_previous_hash
- is_blockchaine_valid
- afficher
- afficher_one_block
- afficher_last_block

Permettant de créer une blockchaine, de lui ajouter ou supprimer des blocks, et de l'afficher ainsi que son/ses blocks. 

4. blockchaine.txt  

Le fichier permettant de stocket le nombre de 0 souhaité pour la blockchaine sauvegardée dans ce fichier.

3. crud_file.py  

Un fichier contenant la classe *File*. 
Elle possède les méthodes suivantes :
- save
- read
Cette classe permet de lire et écrire dans le fichier *blockchaine.txt* pour sauvegarder la blockchaine, et la récupérer lors du relancement du server.

3. main.py  

Un fichier permettant de créer, et gérer une blockchaine, grâce à un menu. Pour tester notre code, exécuter la commande :   
```python3 main.py```   
 Un menu s'affiche proposant les différents choix possibles.
