import streamlit as st
import folium
from streamlit_folium import folium_static#f2b0a5
import pandas as pd
import matplotlib
import re




@st.cache_data
def load_data():
    data = pd.read_csv('fichier_map_nettoye.csv')
    return data

data = load_data()

# --- BARRE DE RECHERCHE ---
st.subheader("🔎 Recherche")
search_query = st.text_input("Rechercher par nom ou adresse :", "")

# Appliquer le filtre si une recherche est faite
if search_query:
    search_query_lower = search_query.lower()
    data = data[
        data["nom"].str.lower().str.contains(search_query_lower) |
        data["adresse"].str.lower().str.contains(search_query_lower)
    ]
    st.success(f"{len(data)} résultats trouvés pour : '{search_query}'")


# Affichage de la carte avec Folium
st.title("Carte des espaces de coworking en Île-de-France")

# Centre de la carte (centre de Paris par défaut)
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Ajout des marqueurs pour chaque coworking
for _, row in data.dropna(subset=["latitude", "longitude"]).iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"<b>{row['nom']}</b><br>{row['adresse']}",
        tooltip=row["nom"]
    ).add_to(m)

folium_static(m)