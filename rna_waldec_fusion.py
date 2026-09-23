# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 22:41:26 2026

@author: Zhang
"""

"""
Objectif : Fusionner en un seul fichier csv tous les csv téléchargés du jeu de données RNA 
"""
# Importation de la bibliothèque pandas pour la manipulation de données (DataFrame)
import pandas as pd

# Importation du module glob pour récupérer des fichiers à partir de motifs (wildcards)
import glob

# Définition du chemin du dossier contenant les fichiers CSV
# Le "r" indique une chaîne brute (raw string) pour éviter les problèmes avec les \ de Windows
chemin = r"C:/Users/Zhang/OneDrive/Bureau/Memoire_SDHC/Base_de_donnees/data_associations/rna_waldec_20250901"

# Récupération de tous les fichiers CSV dont le nom commence par "rna_waldec_20250901"
# Le * permet de capturer tous les fichiers correspondants au motif
fichiers = glob.glob(f"{chemin}/rna_waldec_20250901*.csv")

# Affichage du nombre de fichiers trouvés dans le dossier
print(f"{len(fichiers)} fichiers trouvés")

# Lecture de tous les fichiers CSV et fusion dans un seul DataFrame
# - pd.read_csv lit chaque fichier CSV
# - sep=";" précise que le séparateur est le point-virgule
# - low_memory=False évite les warnings liés aux types de colonnes
# - pd.concat fusionne tous les DataFrames en un seul
# - ignore_index=True recrée un index continu
df = pd.concat(
    (pd.read_csv(f, sep=";", low_memory=False) for f in fichiers),
    ignore_index=True
)

# Export du DataFrame final fusionné dans un nouveau fichier CSV
# index=False évite d'ajouter une colonne d’index inutile
df.to_csv(f"{chemin}/waldec_complet.csv", index=False)

# Message de confirmation indiquant que la fusion est terminée
print("Fusion terminée")



