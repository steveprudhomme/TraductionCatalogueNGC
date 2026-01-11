# Traducteur de Catalogue NGC (Python - Version Excel)

Ce projet est un script utilitaire en Python conçu pour automatiser la traduction de catalogues astronomiques (format Excel) de l'anglais vers le français. Il est spécifiquement optimisé pour le catalogue NGC (New General Catalogue), en traduisant les types d'objets (ex: "Globular Cluster") et les noms de constellations (ex: "Ursa Major").

## 📋 Table des Matières

- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Personnalisation](#-personnalisation)
- [Dépannage](#-dépannage)

## ✨ Fonctionnalités

* **Support Excel complet** : Lit les anciens fichiers `.xls` et génère des fichiers modernes `.xlsx`.
* **Mapping Intelligent** : Utilise des dictionnaires pour traduire précisément :
    * Les types d'objets (Galaxies, Nébuleuses, Amas).
    * Les 88 constellations officielles (du Latin vers le Français).
* **Gestion des erreurs** : Conserve les termes originaux si aucune traduction n'est trouvée.
* **Formatage propre** : Génère un fichier Excel prêt à l'emploi sans colonnes d'index inutiles.

## 🛠 Prérequis

Avant de lancer le script, assurez-vous d'avoir installé Python 3.x sur votre machine.

### Installation des dépendances

Le script nécessite `pandas` pour les données, ainsi que `xlrd` (pour lire les .xls) et `openpyxl` (pour écrire les .xlsx).

Ouvrez votre terminal (ou invite de commande) et exécutez :

```bash
pip install pandas openpyxl xlrd
```

*Note : Si vous utilisez Anaconda, la plupart de ces librairies sont déjà incluses, mais xlrd peut manquer.*

## 🚀 Installation

1.  Créez un dossier pour votre projet.
2.  Enregistrez le script Python principal dans un fichier nommé `traducteur_ngc.py`.
3.  Placez votre fichier Excel source dans ce même dossier.
    * *Nom par défaut attendu :* `NGCObjects.xls`

## ▶️ Utilisation

1.  Ouvrez un terminal dans le dossier du projet.
2.  Lancez le script avec la commande suivante :

```bash
python traducteur_ngc.py
```

3.  Une fois l'exécution terminée, un message de confirmation s'affichera :
    > "Traduction terminée ! Fichier Excel généré : NGCObjects_FR.xlsx"

4.  Ouvrez le nouveau fichier `.xlsx` avec Excel pour voir le résultat.

## ⚙️ Personnalisation

Vous pouvez modifier le script pour l'adapter à d'autres fichiers.

### Changer le fichier source
Ouvrez `traducteur_ngc.py` avec un éditeur de texte et modifiez la variable `input_file` au début du script :

```python
# Modifiez le nom ici si votre fichier s'appelle autrement
input_file = 'Mon_Catalogue.xls'
```

### Ajouter des termes au dictionnaire
Si vous rencontrez des termes non traduits, ajoutez-les dans la section `type_map` ou `const_map` du script :

```python
type_map = {
    'Terme Anglais': 'Terme Français',
    # ... autres termes existants
}
```

## ❓ Dépannage

**Erreur : `FileNotFoundError`**
* Le script ne trouve pas le fichier `.xls`. Vérifiez que le nom dans la variable `input_file` correspond exactement au fichier présent.

**Erreur : `ImportError: Missing optional dependency 'xlrd'`**
* Il manque le module de lecture des anciens fichiers Excel. Exécutez `pip install xlrd`.

**Erreur : `ImportError: Missing optional dependency 'openpyxl'`**
* Il manque le module d'écriture des nouveaux fichiers Excel. Exécutez `pip install openpyxl`.