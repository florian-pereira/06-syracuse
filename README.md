# Liste de Syracuse

Cet exercice est la continuité d'un exercice précédent sur [les suites de Syracuse](https://perso.esiee.fr/~courivad/python/ex04-suites-syracuse.html) pour lequel les valeurs de la suite étaient calculées à la volée sans mémorisation. L'objectif est ici de les stocker dans une liste pour post traitement.

Le fichier ``main.py`` contient :

- une fonction secondaire ``syr_plot()`` (NE PAS MODIFIER) qui permet de construire un graphique. Pour l'utiliser il faut installer [Plotly](https://plotly.com/python/) :

    $ python -m pip install plotly

- une fonction secondaire ``syracuse_l()``
  
  - qui prend en argument un entier ``n`` ;
  - et retourne la liste des valeurs de la suite.

- une fonction secondaire ``temps_de_vol()``
  
  - qui prend en argument une liste de Syracuse ``l`` ;
  - et retourne son temps de vol.

- une fonction secondaire ``temps_de_vol_en_altitude()``
  
  - qui prend en argument une liste de Syracuse ``l`` ;
  - et retourne son temps de vol en altitude.

- une fonction secondaire ``altitude_maximale()``
  
  - qui prend en argument une liste de Syracuse ``l`` ;
  - et retourne son altitude maximale.

- la fonction principale ``main()`` qui fait appel aux fonctions secondaires pour vérifier leur bon fonctionnement .

## To do

1️⃣ Ecrire le code des fonctions secondaires à modifier.

2️⃣ Ecrire quelques appels à la fonction secondaire dans ``main()``.

3️⃣ Exécuter le programme depuis le terminal

    $ python main.py

4️⃣ Une fois le code fonctionnel, le soumettre aux tests unitaires. Le grade obtenu est le pourcentage de tests réussis. 

    $ pytest .python

Si le grade n'est pas satisfaisant, répéter le cycle 1️⃣ 2️⃣ 3️⃣ 4️⃣

5️⃣ Lorsque le grade est satisfaisant, s'intéresser à la [qualité du code](https://perso.esiee.fr/~courivad/python/chapters/16-style.html). Scorer cette qualité

    $ pylint main.py

Si le score n'est pas maximal, répéter l'étape 5️⃣ en tenant compte des messages

6️⃣ Lorsque le grade et le score ``pylint`` sont satisfaisants, pusher le travail pour évaluation

    $ git pull
    $ git add .
    $ git commit -m "un message explicatif"
    $ git push

> [!CAUTION]
En cas de soumissions multiples, seule la première est prise en compte.
