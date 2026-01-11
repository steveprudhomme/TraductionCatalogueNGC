# Traducteur de Catalogue NGC (Python - v1.2.0)

Ce projet est un script utilitaire en Python conçu pour automatiser la traduction de catalogues astronomiques (format Excel) de l'anglais vers le français. Il est spécifiquement optimisé pour le catalogue NGC (New General Catalogue).

## 📋 Table des Matières

- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Personnalisation](#-personnalisation)

## ✨ Fonctionnalités

* **Support Excel complet** : Lit les fichiers `.xls` (anciens) et génère des fichiers `.xlsx` (modernes).
* **Traduction Intelligente** :
    * **Types d'objets** : Traduit "Globular Cluster" en "Amas globulaire", "Asterism", etc.
    * **Constellations** : Traduit les noms latins (ex: "Ursa Major") en français.
    * **En-têtes de colonnes** : Renomme les colonnes (ex: `ObjectNum` -> `N° Objet`, `RAHour` -> `AD Heure`).
    * **Infos détaillées** : Traduit le contenu des descriptions (ex: `Size:` -> `Taille :`).
* **Nettoyage de Données** :
    * Supprime les espaces invisibles qui bloquent la traduction.
    * Remplace les erreurs `nan` (Not a Number) par des cellules vides propres.

## 🛠 Prérequis

Avant de lancer le script, assurez-vous d'avoir installé Python 3.x sur votre machine.

### Installation des dépendances

Le script nécessite `pandas` et `numpy` pour le traitement, ainsi que `xlrd` et `openpyxl` pour la gestion Excel.

Ouvrez votre terminal et exécutez :

```bash
pip install pandas numpy openpyxl xlrd
```

## 🚀 Installation

1.  Créez un dossier pour votre projet.
2.  Placez le script `traducteur_ngc.py` dans ce dossier.
3.  Placez votre fichier Excel source dans ce même dossier.
    * *Nom par défaut attendu :* `NGCObjects.xls`

## ▶️ Utilisation

1.  Ouvrez un terminal dans le dossier du projet.
2.  Lancez le script :

```bash
python traducteur_ngc.py
```

3.  Une fois terminé, le message suivant s'affiche :
    > "Traduction terminée ! Fichier Excel généré : NGCObjects_FR.xlsx"

## ⚙️ Personnalisation

### Changer le fichier source
Ouvrez `traducteur_ngc.py` et modifiez la variable `input_file` :

```python
input_file = 'Mon_Catalogue.xls'
```

### Ajouter des traductions
Vous pouvez enrichir les dictionnaires `type_map` (objets), `const_map` (constellations) ou `column_map` (en-têtes) directement dans le script.