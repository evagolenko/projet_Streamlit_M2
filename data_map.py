import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# Charger le fichier CSV
df = pd.read_csv("fichier_coworking_nettoye.csv", encoding="utf-8").dropna(subset=["adresse"])

# Nettoyer les adresses
df["adresse"] = df["adresse"].astype(str).str.strip()

# Initialiser le géocodeur avec un user-agent
geolocator = Nominatim(user_agent="my_cowork_geocoder")

# Fonction pour obtenir les coordonnées
def get_coordinates(adresse, retries=3):
    try:
        location = geolocator.geocode(adresse)
        return (location.latitude, location.longitude) if location else (None, None)
    except GeocoderTimedOut:
        if retries > 0:
            time.sleep(1)
            return get_coordinates(adresse, retries - 1)
        return (None, None)

# Géocodage des adresses
df["latitude"], df["longitude"] = zip(*df["adresse"].map(get_coordinates))

# Sauvegarder le fichier
df.to_csv("fichier_map_global.csv", index=False, encoding="utf-8")

print("✅ Géocodage terminé")