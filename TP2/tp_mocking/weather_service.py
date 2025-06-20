import requests
import json
from datetime import datetime
# def get_temperature(city):
#  """Récupère la température d'une ville via une API"""
#  url = f"http://api.openweathermap.org/data/2.5/weather"
#  params = {
#  'q': city,
#  'appid': 'fake_api_key', # Clé bidon pour ce TP
#  'units': 'metric'
#  }

#  response = requests.get(url, params=params)

#  if response.status_code == 200:
#     data = response.json()
#     return data['main']['temp']
#  else:
#     return None

"""1. Que se passe-t-il si vous n'avez pas internet ?"""
"""--> Retourne une erreur car pas d'accès à l'API en raison du manque de connexion"""
"""Comment tester le cas où l'API retourne une erreur ?"""
"""Comment être sûr que votre fonction gère bien les différents cas ?"""
"""--> Utilisation de mocks"""

def get_temperature(city):
  """Récupère la température d'une ville via une API"""
  url = "http://api.openweathermap.org/data/2.5/weather" 
  params = {
    'q': city,
    'appid': 'fake_api_key',  # Clé bidon pour ce TP
    'units': 'metric'
  }

  try:
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['main']['temp']
    else:
        return None
  except requests.exceptions.RequestException:
    return None

def save_weather_report(city, filename="weather_log.json"):
    """Récupère la météo et la sauvegarde dans un fichier"""

    # 1. Récupérer la température
    temp = get_temperature(city)
    if temp is None:
        return False

    # 2. Créer le rapport
    report = {
        'city': city,
        'temperature': temp,
        'timestamp': datetime.now().isoformat()
    }

    # 3. Sauvegarder dans le fichier
    try:
    # Lire le fichier existant
        with open(filename, 'r') as f:
            reports = json.load(f)
    except FileNotFoundError:
        reports = []

    reports.append(report)

    with open(filename, 'w') as f:
        json.dump(reports, f)

    return True