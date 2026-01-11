# Procédure de Test

## Objectif
Vérifier que le script de traduction convertit correctement le catalogue NGC du format source Excel (.xls) vers le format cible traduit (.xlsx).

## Prérequis
* Python 3.x installé.
* Les bibliothèques requises installées (`pandas`, `xlrd`, `openpyxl`).
* Le fichier source `NGCObjects.xls` présent dans le répertoire.

## Scénario de Test Manuel

Pour valider le fonctionnement, suivez ces étapes :

1. **Préparation**
   Assurez-vous qu'aucun fichier `NGCObjects_FR.xlsx` n'existe déjà (le supprimer si nécessaire).

2. **Exécution avec Logs**
   Lancez la commande suivante pour exécuter le script et capturer la sortie :
   ```bash
   python -u TraductionCatalogueNGC.py | tee execution_log.txt
   ```

3. **Vérification de la Console**
   * **Attendu** : Le message "Traduction terminée ! Fichier Excel généré : NGCObjects_FR.xlsx" doit s'afficher.
   * **Attendu** : Aucune erreur Python (Traceback) ne doit apparaître.

4. **Vérification du Fichier de Sortie**
   Ouvrez le fichier généré `NGCObjects_FR.xlsx` avec Excel :
   * **Colonnes** : Vérifiez que les colonnes `Type` et `Constellation` contiennent des termes en français (ex: "Galaxie spirale", "Grande Ourse").
   * **Accents** : Vérifiez que les accents (é, è, ô) sont affichés correctement.
   * **Intégrité** : Vérifiez que le nombre de lignes correspond approximativement au fichier source.

## Gestion des fichiers de test
* Le fichier `execution_log.txt` ne doit **pas** être commité sur Git (ajouter au `.gitignore`).
* Le fichier généré `.xlsx` ne doit **pas** être commité sur Git.