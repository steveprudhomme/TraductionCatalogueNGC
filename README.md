# Traducteur de Catalogue NGC (Python)

Ce projet est un script utilitaire en Python conçu pour automatiser la traduction de catalogues astronomiques (format CSV) de l'anglais vers le français. Il est spécifiquement optimisé pour le catalogue NGC (New General Catalogue), en traduisant les types d'objets (ex: "Globular Cluster") et les noms de constellations (ex: "Ursa Major").

## 📋 Table des Matières
- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Personnalisation](#-personnalisation)
- [Dépannage](#-dépannage)

## ✨ Fonctionnalités

* **Lecture de fichiers CSV** : Importe les données brutes depuis un fichier CSV standard.
* **Mapping Intelligent** : Utilise des dictionnaires pour traduire précisément :
    * Les types d'objets (Galaxies, Nébuleuses, Amas).
    * Les 88 constellations officielles (du Latin vers le Français).
* **Gestion des erreurs** : Conserve les termes originaux si aucune traduction n'est trouvée, évitant la perte de données.
* **Export UTF-8** : Génère un fichier propre (`_FR.csv`) compatible avec Excel (encodage `utf-8-sig` pour gérer les accents).

## 🛠 Prérequis

Avant de lancer le script, assurez-vous d'avoir installé les éléments suivants sur votre machine :

1.  **Python 3.x** : [Télécharger Python](https://www.python.org/downloads/)
2.  **Bibliothèque Pandas** : Nécessaire pour la manipulation des données.

### Installation des dépendances

Ouvrez votre terminal (ou invite de commande) et exécutez :

```bash
pip install pandas
```

*Note : Si vous utilisez une distribution comme Anaconda, pandas est déjà installé.*

## 🚀 Installation

1.  Créez un dossier pour votre projet (ex: `Projet_Astronomie`).
2.  Enregistrez le script Python dans un fichier nommé `traducteur_ngc.py`.
3.  Placez votre fichier source (le catalogue à traduire) dans ce même dossier.
    * *Nom par défaut attendu :* `NGCObjects.xls - Sheet1.csv`

## ▶️ Utilisation

1.  Ouvrez un terminal dans le dossier du projet.
2.  Lancez le script avec la commande suivante :

```bash
python traducteur_ngc.py
```

3.  Une fois l'exécution terminée, un message de confirmation s'affichera :
    > "Traduction terminée ! Fichier sauvegardé sous : NGCObjects_FR.csv"

4.  Ouvrez le nouveau fichier `NGCObjects_FR.csv` avec Excel ou un éditeur de texte pour voir le résultat.

## ⚙️ Personnalisation

Vous pouvez modifier le script pour l'adapter à d'autres fichiers ou ajouter des traductions.

### Changer le fichier source
Ouvrez `traducteur_ngc.py` avec un éditeur de texte (Notepad, VS Code) et modifiez la variable `input_file` au début du script :

```python
# Modifiez le nom ici si votre fichier s'appelle autrement
input_file = 'Mon_Fichier_Source.csv'
```

### Ajouter des termes au dictionnaire
Si vous rencontrez des termes non traduits dans le fichier de sortie, ajoutez-les simplement dans la section `type_map` ou `const_map` du script :

```python
type_map = {
    'Terme Anglais': 'Terme Français',
    # ... autres termes existants
}
```

## ❓ Dépannage

**Erreur : `FileNotFoundError`**
* Le script ne trouve pas le fichier CSV. Vérifiez que le nom dans la variable `input_file` correspond *exactement* au nom de votre fichier (attention à l'extension `.csv`).

**Erreur : `ModuleNotFoundError: No module named 'pandas'`**
* La bibliothèque pandas n'est pas installée. Relancez `pip install pandas`.

**Les accents s'affichent mal dans Excel**
* Le script utilise l'encodage `utf-8-sig` spécifiquement pour corriger cela. Assurez-vous d'ouvrir le fichier généré par le script, et non une sauvegarde intermédiaire.
