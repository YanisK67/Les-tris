import time
import random

def trouve_minimum(liste, compteurs):
    """Trouve l'indice du plus petit élément en comptant les opérations"""
    if len(liste) == 0:
        return None
    
    indice_min = 0
    compteurs['affectations'] += 1  # Affectation initiale
    
    for i in range(1, len(liste)):
        compteurs['comparaisons'] += 1  # Comptage comparaison
        if liste[i] < liste[indice_min]:
            indice_min = i
            compteurs['affectations'] += 1  # Affectation mise à jour
    
    return indice_min

def tri_naif(liste):
    """Tri par sélection avec instrumentation complète avec gestion de l'historique"""
    compteurs = {
        'comparaisons': 0,
        'affectations': 2,  # Initialisation resultat + travail
        'temps_execution': 0.0,
        'historique': []
    }
    
    resultat = []
    travail = liste.copy()
    start_time = time.time()
    
    # État initial avant toute modification
    compteurs['historique'].append(resultat.copy() + travail.copy())
    
    while len(travail) > 0:
        # Recherche du minimum avec comptage
        i_min = trouve_minimum(travail, compteurs)
        compteurs['affectations'] += 1  # Affectation i_min
        
        # Transfert élément minimum
        resultat.append(travail[i_min])
        travail.pop(i_min)
        
        # Sauvegarde état intermédiaire
        compteurs['historique'].append(resultat.copy() + travail.copy())
    
    compteurs['temps_execution'] = time.time() - start_time
    return {
        'resultat': resultat,
        'comparaisons': compteurs['comparaisons'],
        'affectations': compteurs['affectations'],
        'temps': compteurs['temps_execution'],
        'historique': compteurs['historique']
    }

###########################################################################################
def tri_selection(liste):
    """Tri par sélection instrumenté avec statistiques complètes pour la gestion de l'historique"""
    # Création d'une copie pour ne pas modifier l'original
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
        # Initialisation du minimum
        stats['affectations'] += 1
        i_min = i
        
        # Recherche du minimum
        for j in range(i + 1, n):
            stats['comparaisons'] += 1  # Comptage comparaison
            if liste_tri[j] < liste_tri[i_min]:
                stats['affectations'] += 1  # Nouveau minimum trouvé
                i_min = j
                
        # Vérification et échange
        stats['comparaisons'] += 1  # Comparaison finale
        if i_min != i:
            # Échange avec 3 affectations (tuple + déballage)
            liste_tri[i], liste_tri[i_min] = liste_tri[i_min], liste_tri[i]
            stats['affectations'] += 2  # 2 affectations pour l'échange
        
        # Sauvegarde de l'état intermédiaire
        stats['historique'].append(liste_tri.copy())
    
    stats['temps'] = time.time() - debut
    return {
        'resultat': liste_tri,
        'comparaisons': stats['comparaisons'],
        'affectations': stats['affectations'],
        'temps': stats['temps'],
        'historique': stats['historique']
    }

###########################################################################################

def tri_insertion(liste):
    """
    Trie une liste en utilisant l'algorithme du tri par insertion.
    Cette fonction retourne une nouvelle liste triée et des statistiques.
    
    Args:
        liste: La liste d'éléments à trier
    Returns:
        Un dictionnaire contenant le résultat et les statistiques
    """
    liste_tri = liste.copy()  # Copie pour ne pas modifier l'original
    stats = {
        'comparaisons': 0,
        'affectations': 0,
        'temps': 0,
        'historique': [liste_tri.copy()]
    }
    
    debut = time.time()
    
    for i in range(1, len(liste_tri)):
        element_a_inserer = liste_tri[i]
        stats['affectations'] += 1  # Affectation de element_a_inserer
        
        j = i - 1
        stats['affectations'] += 1  # Affectation de j
        
        while j >= 0 and liste_tri[j] > element_a_inserer:
            stats['comparaisons'] += 1  # Comparaison dans la condition du while
            liste_tri[j + 1] = liste_tri[j]
            stats['affectations'] += 1  # Décalage d'un élément
            j -= 1
            stats['affectations'] += 1  # Décrémentation de j
        
        if j >= 0:
            stats['comparaisons'] += 1  # Comparaison finale qui a fait sortir du while
        
        liste_tri[j + 1] = element_a_inserer
        stats['affectations'] += 1  # Insertion de l'élément
        
        stats['historique'].append(liste_tri.copy())
    
    stats['temps'] = time.time() - debut
    
    return {
        'resultat': liste_tri,
        'comparaisons': stats['comparaisons'],
        'affectations': stats['affectations'],
        'temps': stats['temps'],
        'historique': stats['historique']
    }
#####################################################################

def afficher_resultats(nom_tri, resultat):
    """
    Affiche les résultats d'un algorithme de tri J'ai utilisé un dictionnaire
    
    Args:
        nom_tri: Nom de l'algorithme de tri
        resultat: Dictionnaire contenant le résultat et les statistiques
    """
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
    """
    Compare les trois algorithmes de tri sur la même liste.
    
    Args:
        liste: La liste d'éléments à trier
    """
    tris = [
        ("Tri naïf", tri_naif),
        ("Tri par sélection", tri_selection),
        ("Tri par insertion", tri_insertion)
    ]

    for nom, fonction_tri in tris:
        resultat = fonction_tri(liste.copy())
        afficher_resultats(nom, resultat)
        print("\n")

###########################################################
###Question 1  Test simple pour comparer les tris
###########################################################
# Liste à trier test simple
liste_test = [64, 34, 25, 12, 22, 11, 90]

print("Liste originale :", liste_test)
print("*************Compare les trois algorithmes de tri sur la même liste**************\n")
comparer_tris(liste_test)

###########################################################
###Question 2  Test sur differentes listes et tailles
###########################################################
def afficher_resultats2(nom_tri, resultat):
    """
    Affiche les résultats d'un algorithme de tri.
    
    Args:
        nom_tri: Nom de l'algorithme de tri
        resultat: Dictionnaire contenant le résultat et les statistiques
    """
    print(f"\n{nom_tri.upper()}")
    print("=" * 40)
    #print(f"Résultat final : {resultat['resultat']}")
    print(f"Temps d'exécution : {resultat['temps']:.6f} secondes")
    print(f"Nombre de comparaisons : {resultat['comparaisons']}")
    print(f"Nombre d'affectations : {resultat['affectations']}")
    


def comparer_tris2(liste, taille):
    """
    Compare les trois algorithmes de tri sur la même liste.
    
    Args:
        liste: La liste d'éléments à trier
    """
    tris = [
        ("Tri naïf", tri_naif),
        ("Tri par sélection", tri_selection),
        ("Tri par insertion", tri_insertion)
    ]
    
    for nom, fonction_tri in tris:
        resultat = fonction_tri(liste.copy())
        afficher_resultats2(nom, resultat)


tailles = [10, 50, 100, 200, 500, 1000]
print("\n###################Comparaison des 3 tris sur des listes et des tailles differentes #################\n")
for taille in tailles:
    
    liste = random.sample(range(1000000), taille)
    print("\n*******************Tri sur liste aleatoire de taille : ", taille, "**************")
    comparer_tris2(liste, taille)
    print("\n*******************Tri sur liste triée par odre croissante de taille: ", taille,"**************")
    liste.sort()
    comparer_tris2(liste, taille)
    print("\n********************Tri sur liste inverse de taille: ", taille,"**************")
    liste.sort(reverse=True)
    comparer_tris2(liste, taille)


###################################################################################
###Question 3  appel sur differentes listes et tailles avec affichage graphique 
###################################################################################


#################################################
###Code affichage de l'animation et du plot
##################################################

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

def generer_animation(historique, titre, nom_fichier):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_title(titre, fontsize=14, pad=20)
    ax.set_xlabel('Position')
    ax.set_ylabel('Valeur')
    
    # Configuration initiale
    bars = ax.bar(range(len(historique[0])), historique[0], color='skyblue')
    text_info = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=10)
    text_stats = ax.text(0.02, 0.85, '', transform=ax.transAxes, fontsize=8, color='dimgrey')

    def truncate_array(arr, max_len=10):
        """Tronque l'affichage du tableau pour les grandes tailles"""
        if len(arr) <= max_len:
            return str(arr)
        half = max_len // 2
        return f"[{', '.join(map(str, arr[:half]))}, ... , {', '.join(map(str, arr[-half:]))}]"

    def animate(frame):
        # Mise à jour des barres
        for i, bar in enumerate(bars):
            bar.set_height(historique[frame][i])
            
        # Affichage tronqué du tableau
        truncated = truncate_array(historique[frame])
        text_stats.set_text(f'État: {truncated}')
        text_info.set_text(f'Étape {frame + 1}/{len(historique)}')
        
        return bars.patches + [text_info, text_stats]

    anim = FuncAnimation(fig, animate, frames=len(historique), interval=300, blit=True, repeat=False)
    anim.save(nom_fichier, writer='pillow', fps=3, dpi=100)
    plt.close()
    print(f"Animation sauvegardée : {nom_fichier}")

def comparer_tris3(tailles):
    temps_naif, temps_selection, temps_insertion = [], [], []

    for taille in tailles:
        liste = random.sample(range(1, 1001), taille)

        resultat = tri_naif(liste.copy())
        temps_naif.append(resultat['temps'])

        resultat = tri_selection(liste.copy())
        temps_selection.append(resultat['temps'])

        resultat = tri_insertion(liste.copy())
        temps_insertion.append(resultat['temps'])

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
    print("Graphique de comparaison sauvegardé : comparaison_performances.png")

# Générer les animations
liste_test = random.sample(range(1, 101), 10)
generer_animation(tri_naif(liste_test.copy())['historique'], "Tri Naïf", "tri_naif.gif")
generer_animation(tri_selection(liste_test.copy())['historique'], "Tri par Sélection", "tri_selection.gif")
generer_animation(tri_insertion(liste_test.copy())['historique'], "Tri par Insertion", "tri_insertion.gif")

# Comparer les performances le plot
tailles_test = [10, 50, 100, 200, 500, 1000]
comparer_tris3(tailles_test)

print("Toutes les animations et le graphique de comparaison ont été générés avec succès.")
