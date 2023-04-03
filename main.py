import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from flask import Flask, jsonify,  request

app = Flask(__name__)

OMDB_KEY = 'b1f02201'
API_KEY ='TO-BE-DEFINED'


# Définir les identifiants de l'API Google Sheets
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDS = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)
CLIENT = gspread.authorize(CREDS)

# Ouvrir la feuille de calcul
SPREADSHEET_ID = 'votre_id_de_feuille_de_calcul'
SHEET_NAME = 'votre_nom_de_feuille_de_calcul'
sheet = CLIENT.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

@app.route('/films')
def get_films():
    # Effectuer la requête à l'API OMDB pour récupérer les données des films Fast & Furious
    response = requests.get('http://www.omdbapi.com/', params={'s': 'Fast & Furious', 'apikey': OMDB_KEY})
    data = response.json()
    # Extraire les informations des films (image, titre, année, réalisateur)
    films = []
    for movie in data['Search']:
        film = {'image': movie['Poster'], 'titre': movie['Title'], 'annee': movie['Year']}
        films.append(film)
    # Renvoyer la liste des films au format JSON
    return jsonify(films)

# Endpoint pour stocker les films "Pirates des Caraïbes"
@app.route('/stock-film', methods=['POST'])
def stock_film():
    # Vérifier si la demande contient une clé d'API valide
    if request.headers.get('x-api-key') != API_KEY:
        return jsonify({'message': 'Clé API invalide'}), 401
    # Récupérer les données des films Pirates des Caraïbes depuis l'API OMDB
    response = requests.get('http://www.omdbapi.com/', params={'s': 'Pirates of the Caribbean', 'apikey': OMDB_KEY})
    data = response.json()
    # Stocker les données dans le Google Spreadsheet
    for movie in data['Search']:
        # Vérifier si le film a été produit avant 2015
        annee = int(movie['Year'])
        avant_2015 = True if annee < 2015 else False
        # Vérifier si Paul Walker est un des acteurs du film
        acteurs = movie['Actors'].split(', ')
        paul_walker = True if 'Paul Walker' in acteurs else False
        # Récupérer les acteurs en commun avec les films Star Wars
        response = requests.get('http://www.omdbapi.com/', params={'s': 'Star Wars', 'apikey': 'votre_api_key'})
        data = response.json()
        star_wars_actors = set()
        for movie in data['Search']:
            response = requests.get('http://www.omdbapi.com/', params={'t': movie['Title'], 'apikey': 'votre_api_key'})
            data = response.json()
            actors = data['Actors'].split(', ')
            star_wars_actors.update(set(actors))

        communs = list(set(acteurs).intersection(star_wars_actors))
        # Ajouter les données au Google Spreadsheet
        row = [movie['Title'], movie['Year'], movie['Director'], avant_2015, paul_walker, json.dumps(communs)]
        sheet.append_row(row)
    # Retourner une réponse de succès
    return jsonify({'message': 'Les films ont été stockés avec succès'})


if __name__ == '__main__':
    app.run(debug=True)


