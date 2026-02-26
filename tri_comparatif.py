import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


###############################################################################
# FONCTIONS DE TRI
###############################################################################

def trouve_minimum(liste, compteurs):
    """Trouve l'indice du plus petit élément en comptant les opérations"""
    if len(liste) == 0:
        return None

    indice_min = 0
    compteurs['affectations'] += 1

    for i in range(1, len(liste)):
        compteurs['comparaisons'] += 1
        if liste[i] < liste[indice_min]:
            indice_min = i
            compteurs['affectations'] += 1

    return indice_min


def tri_naif(liste):
    """Tri naïf instrumenté"""
    compteurs = {
        'comparaisons': 0,
        'affectations': 2,
        'temps_execution': 0.0,
        'historique': []
    }

    resultat = []
    travail = liste.copy()
    start_time = time.time()

    compteurs['historique'].append(resultat.copy() + travail.copy())

    while len(travail) > 0:
        i_min = trouve_minimum(travail, compteurs)
        compteurs['affectations'] += 1

        resultat.append(travail[i_min])
        travail.pop(i_min)

        compteurs['historique'].append(resultat.copy() + travail.copy())

    compteurs['temps_execution'] = time.time() - start_time

    return {
        'resultat': resultat,
        'comparaisons': compteurs['comparaisons'],
        'affectations': compteurs['affectations'],
        'temps': compteurs['temps_execution'],
        'historique': compteurs['historique']
    }


def tri_selection(liste):
    """Tri par sélection instrumenté"""
    liste_tri = liste.copy()

    stats = {
        'comparaisons': 0,
        'affectations': 0,
        'temps': 0.0,
        'historique': [liste_tri.copy()]
    }

    debut = time.time()
    n = len(liste_tri)

    for i in range(n - 1):
        stats['affectations'] += 1
        i_min = i

        for j in range(i + 1, n):
            stats['comparaisons'] += 1
            if liste_tri[j] < liste_tri[i_min]:
                stats['affectations'] += 1
                i_min = j

        stats['comparaisons'] += 1
        if i_min != i:
            liste_tri[i], liste_tri[i_min] = liste_tri[i_min], liste_tri[i]
            stats['affectations'] += 2

        stats['historique'].append(liste_tri.copy())

    stats['temps'] = time.time() - debut

    return {
        'resultat': liste_tri,
        'comparaisons': stats['comparaisons'],
        'affectations': stats['affectations'],
        'temps': stats['temps'],
        'historique': stats['historique']
    }


def tri_insertion(liste):
    """Tri par insertion instrumenté"""
    liste_tri = liste.copy()

    stats = {
        'comparaisons': 0,
        'affectations': 0,
        'temps': 0,
        'historique': [liste_tri.copy()]
    }

    debut = time.time()

    for i in range(1, len(liste_tri)):
        element_a_inserer = liste_tri[i]
        stats['affectations'] += 1

        j = i - 1
        stats['affectations'] += 1

        while j >= 0 and liste_tri[j] > element_a_inserer:
            stats['comparaisons'] += 1
            liste_tri[j + 1] = liste_tri[j]
            stats['affectations'] += 1
            j -= 1
            stats['affectations'] += 1

        if j >= 0:
            stats['comparaisons'] += 1

        liste_tri[j + 1] = element_a_inserer
        stats['affectations'] += 1

        stats['historique'].append(liste_tri.copy())

    stats['temps'] = time.time() - debut

    return {
        'resultat': liste_tri,
        'comparaisons': stats['comparaisons'],
        'affectations': stats['affectations'],
        'temps': stats['temps'],
        'historique': stats['historique']
    }


###############################################################################
# AFFICHAGE DES RESULTATS
###############################################################################

def afficher_resultats(nom_tri, resultat):
    print(f"\n{nom_tri.upper()}")
    print("=" * 40)
    print(f"Résultat final : {resultat['resultat']}")
    print(f"Temps d'exécution : {resultat['temps']:.6f} secondes")
    print(f"Nombre de comparaisons : {resultat['comparaisons']}")
    print(f"Nombre d'affectations : {resultat['affectations']}")

    print("\nHistorique des étapes :")
    for i, etape in enumerate(resultat['historique']):
        print(f"Étape {i}: {etape}")


def comparer_tris(liste):
    tris = [
        ("Tri naïf", tri_naif),
        ("Tri par sélection", tri_selection),
        ("Tri par insertion", tri_insertion)
    ]

    for nom, fonction_tri in tris:
        resultat = fonction_tri(liste.copy())
        afficher_resultats(nom, resultat)


###############################################################################
# AFFICHAGE GRAPHIQUE ET ANIMATION
###############################################################################

def generer_animation(historique, titre, nom_fichier):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_title(titre)
    ax.set_xlabel('Position')
    ax.set_ylabel('Valeur')

    bars = ax.bar(range(len(historique[0])), historique[0])
    text_info = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    def animate(frame):
        for i, bar in enumerate(bars):
            bar.set_height(historique[frame][i])
        text_info.set_text(f'Étape {frame + 1}/{len(historique)}')
        return bars

    anim = FuncAnimation(fig, animate, frames=len(historique), interval=300)
    anim.save(nom_fichier, writer='pillow', fps=3)
    plt.close()


def comparer_tris3(tailles):
    temps_naif, temps_selection, temps_insertion = [], [], []

    for taille in tailles:
        liste = random.sample(range(1, 1001), taille)

        temps_naif.append(tri_naif(liste.copy())['temps'])
        temps_selection.append(tri_selection(liste.copy())['temps'])
        temps_insertion.append(tri_insertion(liste.copy())['temps'])

    plt.figure(figsize=(10, 6))
    plt.plot(tailles, temps_naif, label="Tri Naïf", marker='o')
    plt.plot(tailles, temps_selection, label="Tri Sélection", marker='s')
    plt.plot(tailles, temps_insertion, label="Tri Insertion", marker='^')
    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Comparaison des performances des algorithmes de tri")
    plt.legend()
    plt.grid(True)
    plt.savefig("comparaison_performances.png")
    plt.close()


###############################################################################
# PROGRAMME PRINCIPAL
###############################################################################

if __name__ == "__main__":

    # Question 1
    liste_test = [64, 34, 25, 12, 22, 11, 90]
    print("Liste originale :", liste_test)
    comparer_tris(liste_test)

    # Question 2
    tailles = [10, 50, 100]
    for taille in tailles:
        liste = random.sample(range(1000000), taille)
        comparer_tris(liste)

    # Question 3
    liste_anim = random.sample(range(1, 101), 10)
    generer_animation(tri_naif(liste_anim.copy())['historique'], "Tri Naïf", "tri_naif.gif")
    generer_animation(tri_selection(liste_anim.copy())['historique'], "Tri Sélection", "tri_selection.gif")
    generer_animation(tri_insertion(liste_anim.copy())['historique'], "Tri Insertion", "tri_insertion.gif")

    comparer_tris3([10, 50, 100, 200, 500])
    print("Toutes les animations et le graphique ont été générés.")
