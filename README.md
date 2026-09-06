# Prototype de suivi QA pour projets IT

## Description du besoin

Dans un projet IT, les tickets sont dispersés entre plusieurs membres d'équipe, avec des statuts et des dates limites difficiles à suivre globalement, ce qui rend le pilotage du projet compliqué et chronophage.

Ce prototype vise à centraliser le suivi des tickets d'un projet : afficher des indicateurs clés, détecter automatiquement des situations à risque (retards, tickets bloqués, sans responsable, priorités critiques), et générer une courte synthèse de l'état du projet.

Pour ce premier mois, le périmètre est volontairement limité à un prototype simple et fonctionnel : pas de connexion réelle à Jira/GitHub, pas de système multi-agents, pas de RAG, pas de déploiement cloud. L'objectif est un socle clair et démontrable avant d'envisager des extensions.
Le prototype fonctionne à partir de données simulées (fichier CSV de démonstration), sans dépendance à des données réelles ou confidentielles.



## Fonctionnalités
- Chargement d'un fichier CSV de tickets
- Tableau de bord avec indicateurs clés (KPI)
- Filtres par statut, priorité, responsable
- Détection automatique de 4 types d'alertes (retard, bloqué, critique, sans responsable)
- Niveau de gravité pour les tickets en retard
- Synthèse automatique de l'état du projet

## Installation

```bash
pip install -r requirements.txt
```

## Lancement


```bash
python -m streamlit run app.py
```

L'application s'ouvre automatiquement dans le navigateur à l'adresse http://localhost:8501

## Structure du projet
- `tickets.py` : génère le jeu de données de démonstration
- `preparation_donnees.py` : nettoyage des données et calcul des règles d'alerte
- `app.py` : interface Streamlit (dashboard)
- `test_preparation.py` : tests unitaires des règles d'alerte
- `tickets_demo.csv` : jeu de données de démonstration generé avec 'tickets.py'

## Limites connues
- Léger déséquilibre dans la génération aléatoire des dates (proportion de tickets "en retard" plus élevée qu'attendu)
- Pas de connexion à de vraies données (Jira, GitHub) - données simulées uniquement
