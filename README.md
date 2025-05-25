# Allergen Chip Challenge — TER Allergie (2024-2025)

## À propos du projet

Ce projet a été réalisé dans le cadre d’un TER (Travail d’Étude et de Recherche) en collaboration avec la Société Française d’Allergologie (SFA) et le Health Data Hub.  
L’objectif principal est de développer des modèles d’apprentissage automatique pour prédire la présence et la sévérité des allergies à partir de données complexes issues de puces allergéniques (ISAC_V1, ISAC_V2, ALEX).  
Les données utilisées comprennent plus de 4000 patients, avec des profils IgE détaillés et des informations cliniques.

##Objectifs

- Classer les patients en deux groupes : allergiques et non allergiques.
- Identifier le type d’allergie : respiratoire, alimentaire, venin, etc.
- Prédire la sévérité de l’allergie.
- Analyser l’importance des variables dans la classification.

## Méthodologie

- **Exploration et prétraitement des données** : analyse des cibles et des classes, équilibrage des données via SMOTE.
- **Modèles testés** :
  - Random Forest
  - XGBoost
  - Régression Logistique
  - SVM
- **Validation croisée** : K-Fold avec k=10.
- **Évaluation des performances** : F1-score (classe 1), précision, AUC-ROC, matrices de confusion.
- **Analyse des variables contributives** via les scores d’importance de XGBoost.

## Résultats

- **XGBoost** a démontré des performances supérieures sur l’ensemble des cibles, avec des AUC-ROC proches de l’optimum, un excellent F1-score sur la classe 1, et une stabilité remarquable sur les différents tests.
- Les résultats détaillés (F1-score, précision, AUC, matrices de confusion, importance des features) sont disponibles dans les notebooks et les fichiers CSV générés.


## À venir / Perspectives

- Ajout d’analyses explicatives avancées (SHAP, LIME) pour interpréter les prédictions.
- Intégration de données cliniques supplémentaires.
- Optimisation des hyperparamètres et exploration d’autres modèles (deep learning).

## Auteur

- **AL AYOUBI Ibrahim**  


