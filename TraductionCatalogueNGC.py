import pandas as pd

# --- CONFIGURATION ---
input_file = 'NGCObjects.xls'
output_file = 'NGCObjects_FR.xlsx'
# ---------------------

# Dictionnaires (inchangés)
type_map = {
    'Open Cluster': 'Amas ouvert',
    'Globular Cluster': 'Amas globulaire',
    'Diffuse Nebula': 'Nébuleuse diffuse',
    'Planetary Nebula': 'Nébuleuse planétaire',
    'Supernova Remnant': 'Reste de supernova',
    'Spiral Galaxy': 'Galaxie spirale',
    'Elliptical Galaxy': 'Galaxie elliptique',
    'Lenticular Galaxy': 'Galaxie lenticulaire',
    'Lenticular (S0) Galaxy': 'Galaxie lenticulaire',
    'Irregular Galaxy': 'Galaxie irrégulière',
    'Double Star': 'Étoile double',
    'Star Cloud': 'Nuage stellaire',
    'Cluster associated with nebulosity': 'Amas avec nébulosité',
    'Emission Nebula': 'Nébuleuse en émission',
    'Reflection Nebula': 'Nébuleuse par réflexion',
    'Dark Nebula': 'Nébuleuse obscure'
}

const_map = {
    'Andromeda': 'Andromède', 'Antlia': 'Machine pneumatique', 'Apus': 'Oiseau de paradis',
    'Aquarius': 'Verseau', 'Aquila': 'Aigle', 'Ara': 'Autel', 'Aries': 'Bélier',
    'Auriga': 'Cocher', 'Bootes': 'Bouvier', 'Caelum': 'Burin', 'Camelopardalis': 'Girafe',
    'Cancer': 'Cancer', 'Canes Venatici': 'Chiens de chasse', 'Canis Major': 'Grand Chien',
    'Canis Minor': 'Petit Chien', 'Capricornus': 'Capricorne', 'Carina': 'Carène',
    'Cassiopeia': 'Cassiopée', 'Centaurus': 'Centaure', 'Cepheus': 'Céphée',
    'Cetus': 'Baleine', 'Chamaeleon': 'Caméléon', 'Circinus': 'Compas', 'Columba': 'Colombe',
    'Coma Berenices': 'Chevelure de Bérénice', 'Corona Australis': 'Couronne australe',
    'Corona Borealis': 'Couronne boréale', 'Corvus': 'Corbeau', 'Crater': 'Coupe',
    'Crux': 'Croix du Sud', 'Cygnus': 'Cygne', 'Delphinus': 'Dauphin', 'Dorado': 'Dorade',
    'Draco': 'Dragon', 'Equuleus': 'Petit Cheval', 'Eridanus': 'Éridan', 'Fornax': 'Fourneau',
    'Gemini': 'Gémeaux', 'Grus': 'Grue', 'Hercules': 'Hercule', 'Horologium': 'Horloge',
    'Hydra': 'Hydre', 'Hydrus': 'Hydre mâle', 'Indus': 'Indien', 'Lacerta': 'Lézard',
    'Leo': 'Lion', 'Leo Minor': 'Petit Lion', 'Lepus': 'Lièvre', 'Libra': 'Balance',
    'Lupus': 'Loup', 'Lynx': 'Lynx', 'Lyra': 'Lyre', 'Mensa': 'Table',
    'Microscopium': 'Microscope', 'Monoceros': 'Licorne', 'Musca': 'Mouche',
    'Norma': 'Règle', 'Octans': 'Octant', 'Ophiuchus': 'Serpentaire', 'Ophiucus': 'Serpentaire',
    'Orion': 'Orion', 'Pavo': 'Paon', 'Pegasus': 'Pégase', 'Perseus': 'Persée',
    'Phoenix': 'Phénix', 'Pictor': 'Peintre', 'Pisces': 'Poissons',
    'Piscis Austrinus': 'Poisson austral', 'Puppis': 'Poupe', 'Pyxis': 'Boussole',
    'Reticulum': 'Réticule', 'Sagitta': 'Flèche', 'Sagittarius': 'Sagittaire',
    'Scorpius': 'Scorpion', 'Sculptor': 'Sculpteur', 'Scutum': 'Écu de Sobieski',
    'Serpens': 'Serpent', 'Serpens Caput': 'Tête du Serpent', 'Serpens Cauda': 'Queue du Serpent',
    'Sextans': 'Sextant', 'Taurus': 'Taureau', 'Telescopium': 'Télescope',
    'Triangulum': 'Triangle', 'Triangulum Australe': 'Triangle austral',
    'Tucana': 'Toucan', 'Ursa Major': 'Grande Ourse', 'Ursa Minor': 'Petite Ourse',
    'Vela': 'Voiles', 'Virgo': 'Vierge', 'Volans': 'Poisson volant', 'Vulpecula': 'Petit Renard'
}

try:
    print(f"Lecture du fichier {input_file} en cours...")
    
    # CORRECTION : header=2 pour sauter les deux premières lignes (titre + vide)
    df = pd.read_excel(input_file, header=2)
    
    # DEBUG : Affiche les colonnes trouvées dans le log
    print(f"Colonnes détectées : {list(df.columns)}")

    # Traduction
    if 'Type' in df.columns:
        print("Traduction de la colonne 'Type'...")
        df['Type'] = df['Type'].map(type_map).fillna(df['Type'])
    else:
        print("ATTENTION : Colonne 'Type' non trouvée !")
    
    if 'Constellation' in df.columns:
        print("Traduction de la colonne 'Constellation'...")
        df['Constellation'] = df['Constellation'].map(const_map).fillna(df['Constellation'])
    else:
        print("ATTENTION : Colonne 'Constellation' non trouvée !")

    # Sauvegarde
    df.to_excel(output_file, index=False)
    print(f"Traduction terminée ! Fichier Excel généré : {output_file}")

except FileNotFoundError:
    print(f"Erreur : Le fichier '{input_file}' est introuvable.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")