import pandas as pd
import numpy as np

# --- CONFIGURATION ---
input_file = 'NGCObjects.xls'
output_file = 'NGCObjects_FR.xlsx'
# ---------------------

# 1. Dictionnaire des Types
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
    'Dark Nebula': 'Nébuleuse obscure',
    'Star': 'Étoile',
    'Triple Star': 'Étoile triple',
    'Cluster Nebulosity': 'Nébulosité d\'amas',
    'Asterism': 'Astérisme',
    'Nebulosity in External Galaxy': 'Nébulosité dans une galaxie externe',
    'Galaxy': 'Galaxie',
    'Nebula': 'Nébuleuse'
}

# 2. Dictionnaire des Constellations (Abréviations UAI -> Français)
const_map = {
    'And': 'Andromède', 'Ant': 'Machine pneumatique', 'Aps': 'Oiseau de paradis',
    'Aqr': 'Verseau', 'Aql': 'Aigle', 'Ara': 'Autel', 'Ari': 'Bélier',
    'Aur': 'Cocher', 'Boo': 'Bouvier', 'Cae': 'Burin', 'Cam': 'Girafe',
    'Cnc': 'Cancer', 'CVn': 'Chiens de chasse', 'CMa': 'Grand Chien',
    'CMi': 'Petit Chien', 'Cap': 'Capricorne', 'Car': 'Carène',
    'Cas': 'Cassiopée', 'Cen': 'Centaure', 'Cep': 'Céphée', 'Cet': 'Baleine',
    'Cha': 'Caméléon', 'Cir': 'Compas', 'Col': 'Colombe',
    'Com': 'Chevelure de Bérénice', 'CrA': 'Couronne australe',
    'CrB': 'Couronne boréale', 'Crv': 'Corbeau', 'Crt': 'Coupe',
    'Cru': 'Croix du Sud', 'Cyg': 'Cygne', 'Del': 'Dauphin', 'Dor': 'Dorade',
    'Dra': 'Dragon', 'Equ': 'Petit Cheval', 'Eri': 'Éridan', 'For': 'Fourneau',
    'Gem': 'Gémeaux', 'Gru': 'Grue', 'Her': 'Hercule', 'Hor': 'Horloge',
    'Hya': 'Hydre', 'Hyi': 'Hydre mâle', 'Ind': 'Indien', 'Lac': 'Lézard',
    'Leo': 'Lion', 'LMi': 'Petit Lion', 'Lep': 'Lièvre', 'Lib': 'Balance',
    'Lup': 'Loup', 'Lyn': 'Lynx', 'Lyr': 'Lyre', 'Men': 'Table',
    'Mic': 'Microscope', 'Mon': 'Licorne', 'Mus': 'Mouche', 'Nor': 'Règle',
    'Oct': 'Octant', 'Oph': 'Serpentaire', 'Ori': 'Orion', 'Pav': 'Paon',
    'Peg': 'Pégase', 'Per': 'Persée', 'Phe': 'Phénix', 'Pic': 'Peintre',
    'Psc': 'Poissons', 'PsA': 'Poisson austral', 'Pup': 'Poupe', 'Pyx': 'Boussole',
    'Ret': 'Réticule', 'Sge': 'Flèche', 'Sgr': 'Sagittaire', 'Sco': 'Scorpion',
    'Scl': 'Sculpteur', 'Sct': 'Écu de Sobieski', 'Ser': 'Serpent',
    'Sex': 'Sextant', 'Tau': 'Taureau', 'Tel': 'Télescope', 'Tri': 'Triangle',
    'TrA': 'Triangle austral', 'Tuc': 'Toucan', 'UMa': 'Grande Ourse',
    'UMi': 'Petite Ourse', 'Vel': 'Voiles', 'Vir': 'Vierge',
    'Vol': 'Poisson volant', 'Vul': 'Petit Renard'
}

# 3. Dictionnaire des En-têtes
column_map = {
    'ObjectNum': 'N° Objet',
    'Name': 'Nom',
    'Type': 'Type',
    'Constellation': 'Constellation',
    'RAHour': 'AD Heure',
    'RAMinute': 'AD Minute',
    'DecSign': 'Déc Signe',
    'DecDeg': 'Déc Degré',
    'DecMinute': 'Déc Minute',
    'Magnitude': 'Magnitude',
    'Info': 'Infos',
    'Distance (ly)': 'Distance (al)'
}

def clean_info_text(text):
    """Traduit le contenu textuel de la colonne Info"""
    if not isinstance(text, str):
        return text
    replacements = {'Size:': 'Taille :', 'size:': 'Taille :', 'Sep:': 'Sép :', 'sep:': 'Sép :'}
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

try:
    print(f"Lecture du fichier {input_file} en cours...")
    df = pd.read_excel(input_file, header=2)
    
    # TRADUCTION DES TYPES
    if 'Type' in df.columns:
        df['Type'] = df['Type'].astype(str).str.strip().replace('nan', np.nan)
        df['Type'] = df['Type'].map(type_map).fillna(df['Type'])
    
    # TRADUCTION DES CONSTELLATIONS
    if 'Constellation' in df.columns:
        df['Constellation'] = df['Constellation'].astype(str).str.strip().replace('nan', np.nan)
        df['Constellation'] = df['Constellation'].map(const_map).fillna(df['Constellation'])

    # TRADUCTION INFO
    if 'Info' in df.columns:
        df['Info'] = df['Info'].apply(clean_info_text)

    # NETTOYAGE GLOBAL
    df = df.fillna("").replace("nan", "")

    # EN-TÊTES
    df.rename(columns=column_map, inplace=True)

    df.to_excel(output_file, index=False)
    print(f"Traduction terminée ! Fichier Excel généré : {output_file}")

except FileNotFoundError:
    print(f"Erreur : Le fichier '{input_file}' est introuvable.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")