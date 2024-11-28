#### Fonctions secondaires
"""
Ce programme travaille avec les suites de Syracuse (ou conjecture de Collatz). 
Il permet de :
- Générer une suite de Syracuse à partir d'un nombre donné.
- Afficher cette suite sous forme de graphique.
- Trouver plusieurs informations importantes sur cette suite, comme :
  Le nombre d'étapes pour atteindre 1 (temps de vol).
  Le nombre d'étapes avant de passer sous la valeur de départ (temps de vol en altitude).
  La plus grande valeur atteinte (altitude maximale).
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Affiche un graphique pour représenter la suite de Syracuse.

    Arguments :
        lsyr (list) : La liste des nombres qui forment la suite de Syracuse.

    Retourne :
        None : Cette fonction n'a pas de valeur de retour, mais elle affiche un graphique.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({
            'layout': { 
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}}
        }
    })
    x = list(range(len(lsyr)))  # Utilisation directe de range()
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()


def syracuse_l(n):
    """
    Calcule la suite de Syracuse à partir d'un nombre donné.

    Arguments :
        n (int) : Le nombre de départ pour calculer la suite de Syracuse.

    Retourne :
        list : La suite de Syracuse sous forme de liste, jusqu'à ce qu'elle atteigne 1.
    """
    l = [n]  # Initialisation directe de la liste avec l'élément initial
    while n != 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1  # Ternaire pour simplifier
        l.append(n)
    return l


def temps_de_vol(l):
    """
    Calcule le temps de vol d'une suite de Syracuse.

    Le temps de vol est le nombre d'étapes nécessaires pour atteindre la valeur 1.

    Arguments :
        l (list) : La suite de Syracuse.

    Retourne :
        int : Le temps de vol (nombre d'étapes pour atteindre 1).
    """
    return next((i for i, elt in enumerate(l) if elt == 1), None)  # Simplification avec next()


def temps_de_vol_en_altitude(l):
    """
    Calcule le temps de vol en altitude d'une suite de Syracuse.

    Le temps de vol en altitude est le nombre d'étapes pendant lesquelles 
    la suite reste au-dessus de la valeur de départ.

    Arguments :
        l (list) : La suite de Syracuse.

    Retourne :
        int : Le temps de vol en altitude (nombre d'étapes avant de passer sous la valeur initiale).
    """
    n = l[0]
    return next((i - 1 for i, elt in enumerate(l) if elt < n), None)  # Simplification avec next()


def altitude_maximale(l):
    """
    Trouve l'altitude maximale atteinte dans une suite de Syracuse.

    Arguments :
        l (list) : La suite de Syracuse.

    Retourne :
        int : La valeur la plus grande atteinte dans la suite.
    """
    return max(l)  # Utilisation de la fonction max() pour simplifier


#### Fonction principale ####

def main():
    """
    Fonction principale qui exécute toutes les étapes du programme.

    Étapes réalisées :
        1. Génère la suite de Syracuse pour le nombre 15.
        2. Affiche la suite sous forme de liste.
        3. Affiche un graphique représentant la suite.
        4. Affiche :
            - Le temps de vol.
            - Le temps de vol en altitude.
            - L'altitude maximale.

    Arguments :
        Aucun.

    Retourne :
        None : Les résultats sont affichés dans la console et sous forme de graphique.
    """
    lsyr = syracuse_l(15)
    print(lsyr)
    syr_plot(lsyr)
    print("Temps de vol :", temps_de_vol(lsyr))
    print("Temps de vol en altitude :", temps_de_vol_en_altitude(lsyr))
    print("Altitude maximale :", altitude_maximale(lsyr))


# Point d'entrée du programme
if __name__ == "__main__":
    main()
