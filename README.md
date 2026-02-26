# Comparaison et visualisation des algorithmes de tri en Python


Ce projet implémente et compare trois algorithmes classiques :

- Tri naïf - Tri par sélection  
- Tri par insertion  

Chaque algorithme mesure :

- le nombre de comparaisons  
- le nombre d’affectations  
- le temps d’exécution  
- l’historique des états intermédiaires  

Le programme inclut également :

- des tests sur différentes tailles de listes  
- une comparaison graphique des performances  
- des animations illustrant le déroulement des tris  

---

## Fichier principal


**tri_comparatif.py**


---

## Complexité des algorithmes


| Algorithme | Complexité moyenne | Complexité pire cas |
|-----------|-------------------|--------------------|
| Tri naïf | O(n²) | O(n²) |
| Tri sélection | O(n²) | O(n²) |
| Tri insertion | O(n²) | O(n²) |
| Tri insertion (meilleur cas) | O(n) | — |


## Tests réalisés

### Test simple

Une liste courte est utilisée pour observer étape par étape le déroulement des tris.

### Tests sur différentes tailles

Des listes de différentes tailles sont générées automatiquement afin d’évaluer l’impact de la taille des données sur les performances.

---

## Visualisations produites


Fichiers générés :

- tri_naif.gif  
- tri_selection.gif  
- tri_insertion.gif  


### Exécuter le programme


python tri_comparatif.py
```

## Auteur 

Yanis Khelif  (Lycée Notre Dame Providence- Enghien les bains)

