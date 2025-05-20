import pandas as pd
import re
import unicodedata

def nettoyage_csv(fichier):
    df = pd.read_csv(fichier).fillna("NULL").astype(str)  # Charger et convertir en chaîne de caractères

    # Nettoyage des textes
    def nettoyer_texte(texte):
        return re.sub(r'\s+', ' ', unicodedata.normalize('NFKD', texte).encode('ascii', 'ignore').decode('ascii').strip())  # Normaliser et retirer les espaces inutiles

    df = df.applymap(nettoyer_texte)  # Appliquer à toutes les cellules du dataframe

    # Nettoyage des numéros de téléphone
    def nettoyer_numeros_telephone(texte):
        match = re.search(r'\b(0[1-9](?:[ .-]?\d{2}){4}|0[1-9]\d{8})\b', texte.split(',')[0].strip())
        if match:
            return ' '.join(re.sub(r'\D', '', match.group(0))[i:i+2] for i in range(0, 10, 2))
        return "NULL"

    if "téléphone" in df.columns:
        df["téléphone"] = df["téléphone"].apply(nettoyer_numeros_telephone)
    else:
        print("Colonne 'téléphone' non trouvée.")

    df.to_csv("fichier_map_nettoye.csv", index=False)
    print("Fichier nettoyé et sauvegardé.")

# Utilisation
nettoyage_csv("fichier_map_global.csv")