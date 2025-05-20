scrapping.py :contient le script de web scraping utilisé pour extraire les données brutes depuis le site source.

data_cleaning.py: sert à effectuer un premier nettoyage des données extraites : suppression des doublons, uniformisation des formats, filtrage des lignes inutiles, etc.

data_map.py: ajoute les coordonnées géographiques aux adresses grâce à une API de géocodage (comme Nominatim d’OpenStreetMap), pour obtenir la latitude et la longitude de chaque lieu.

data_cleaning_map.py: effectue un second nettoyage sur les données enrichies, corrige les erreurs éventuelles, ajuste les noms de colonnes, et prépare le fichier 
final à exploiter.

fichier_map_nettoye.csv : fichier CSV final, prêt à être utilisé dans l’application. Il contient les données propres et géolocalisées.

app.py: application Streamlit. Ce fichier permet de charger et d’afficher les données dans une interface web interactive, avec des éléments de visualisation.

Readme.txt: fichier de documentation du projet. Il explique les objectifs, les étapes de traitement des données, ainsi que la façon d’utiliser l’application.
