# TP Python — Comparaison des algorithmes de tri

Projet réalisé par **Yanis KHELIF**.

Ce projet implémente et compare trois algorithmes classiques de tri :
- **Tri naïf** (tri par sélection avec tableau auxiliaire)
- **Tri par sélection**
- **Tri par insertion**

Chaque algorithme est **instrumenté** afin de mesurer :
- le nombre de **comparaisons**
- le nombre d’**affectations**
- le **temps d’exécution**
- l’**historique des états intermédiaires**

Le projet inclut également :
- des tests sur différentes tailles et configurations de listes
- une **visualisation graphique** des performances
- des **animations** illustrant le déroulement des tris

---

## 📁 Fichier du projet

- `tri_VF.py`  
  Script Python unique contenant :
  - l’implémentation des trois algorithmes de tri
  - l’instrumentation complète (statistiques + historique)
  - des tests comparatifs
  - la génération de graphiques et d’animations

---

## 🎯 Objectifs pédagogiques

- Comprendre le fonctionnement des principaux algorithmes de tri
- Comparer leur efficacité selon :
  - la taille de la liste
  - l’ordre initial des données (aléatoire, trié, inversé)
- Mettre en évidence les notions de :
  - complexité algorithmique
  - coût en opérations (comparaisons / affectations)
- Visualiser pas à pas l’exécution des algorithmes

---

## 🧠 Algorithmes implémentés

### 🔹 Tri naïf
- Recherche répétée du minimum
- Utilisation d’un tableau auxiliaire
- Complexité : **O(n²)**
- Historique détaillé à chaque extraction du minimum

### 🔹 Tri par sélection
- Recherche du minimum dans la partie non triée
- Échange avec l’élément courant
- Complexité : **O(n²)**
- Moins d’affectations que le tri naïf

### 🔹 Tri par insertion
- Insertion progressive des éléments dans une partie déjà triée
- Complexité :
  - **O(n²)** dans le pire cas
  - **O(n)** dans le meilleur cas (liste déjà triée)

---

## 📊 Statistiques collectées

Pour chaque tri :
- Temps d’exécution (en secondes)
- Nombre de comparaisons
- Nombre d’affectations
- Historique des états intermédiaires de la liste

Les résultats sont stockés dans un **dictionnaire** Python.

---

## 🧪 Tests réalisés

### ✔️ Test simple
- Liste courte pour observer étape par étape le déroulement des tris

### ✔️ Tests sur différentes tailles
- Tailles testées :
