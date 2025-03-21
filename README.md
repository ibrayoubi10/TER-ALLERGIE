# Analyse des Données sur les Allergies

## Description du Projet
Ce projet vise à analyser un jeu de données public sur les allergies. Dans un premier temps, nous avons effectué une analyse exploratoire des données afin de mieux comprendre leur structure et leurs caractéristiques principales. Par la suite, après avoir obtenu la version finale des données nettoyées et prétraitées, nous avons réalisé plusieurs analyses avancées de réduction de dimensionnalité pour mieux visualiser et interpréter les relations entre les variables.

## Analyses Réalisées
### 1. Analyse en Composantes Principales (ACP)
L'Analyse en Composantes Principales (ACP) est une technique statistique permettant de réduire la dimensionnalité des données tout en conservant le maximum de variance possible. Elle transforme les variables initiales en un ensemble de nouvelles variables non corrélées appelées composantes principales.

**Objectif :**
- Réduire le nombre de dimensions tout en conservant les informations essentielles.
- Visualiser les données dans un espace de plus faible dimension.

**Résultat :**
Les résultats obtenus ont été décevants, car les premières composantes principales ne capturaient pas suffisamment bien la structure sous-jacente des données pour permettre une interprétation claire.

### 2. Uniform Manifold Approximation and Projection (UMAP)
UMAP est une technique de réduction de dimensionnalité non linéaire qui cherche à préserver la structure locale et globale des données dans un espace de plus faible dimension. Cette méthode est souvent utilisée pour la visualisation de données complexes.

**Objectif :**
- Réduire la dimensionnalité en conservant la proximité locale des points de données.
- Identifier des groupes potentiels dans les données.

**Résultat :**
Les résultats obtenus avec UMAP n'ont pas permis de révéler de structures claires au sein du jeu de données, rendant difficile toute segmentation pertinente des données.

### 3. t-Distributed Stochastic Neighbor Embedding (t-SNE)
Le t-SNE est une autre méthode de réduction de dimensionnalité qui est particulièrement adaptée à la visualisation des données en 2D ou 3D. Elle fonctionne en préservant les relations de voisinage entre les points dans un espace de dimension réduite.

**Objectif :**
- Visualiser des structures sous-jacentes dans des données de grande dimension.
- Identifier des regroupements potentiels.

**Résultat :**
Malgré plusieurs ajustements des hyperparamètres, les résultats obtenus avec t-SNE n'ont pas été concluants. Les données ne montraient pas de séparation nette entre différentes classes ou groupes, ce qui a limité la pertinence de cette approche.

## Conclusion
Malgré l'utilisation de plusieurs techniques avancées de réduction de dimensionnalité, les résultats obtenus ont été décevants. Aucune des méthodes testées n'a permis de dégager des tendances claires ou des clusters significatifs au sein des données. Ces résultats suggèrent que d'autres approches, telles que des techniques de modélisation plus avancées ou l'incorporation de nouvelles variables, pourraient être nécessaires pour extraire des informations utiles de ces données.

## Auteurs
- Al Ayoubi Ibrahim 
- Sauma Christen


