# Journal des modifications (Changelog)

Tous les changements notables de ce projet seront documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère à [Semantic Versioning](https://semver.org/lang/fr/).

## [1.1.1] - 2026-01-11

### Divers (Maintenance)
- Mise à jour du fichier `.gitignore` pour exclure les logs d'exécution (`*.txt`) et les fichiers Excel générés afin de garder le dépôt propre.
- Amélioration de la documentation de test (`TESTING.md`) avec une procédure plus détaillée et sécurisée.

## [1.1.0] - 2026-01-11

### Ajouté
- Support de la lecture des fichiers Excel anciens (`.xls`) via la bibliothèque `xlrd`.
- Support de l'écriture des fichiers Excel modernes (`.xlsx`) via la bibliothèque `openpyxl`.
- Ajout des nouvelles dépendances (`openpyxl`, `xlrd`) dans la documentation.

### Modifié
- Le script traite désormais nativement les fichiers Excel au lieu des fichiers CSV pour une meilleure gestion du formatage.
- Le fichier de sortie est généré sans colonne d'index inutile.
- Mise à jour du `README.md` pour refléter le changement de format de fichier (CSV -> XLS/XLSX).

## [1.0.0] - 2026-01-11

### Ajouté
- Version initiale du projet.
- Script Python `traducteur_ngc.py` fonctionnel.
- Support de la lecture et écriture au format CSV.
- Dictionnaires de traduction complets pour :
    - Les types d'objets astronomiques (ex: Galaxy -> Galaxie).
    - Les 88 constellations officielles (Latin -> Français).
- Documentation complète (`README.md`) incluant les procédures d'installation.