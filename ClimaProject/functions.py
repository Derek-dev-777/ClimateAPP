import requests
import os
from dotenv import load_dotenv

# API openweather (usada para buscar as cordenadas das cidades que serão digitadas):
# https://openweathermap.org/city/3449324

# API ipInfo (usada para pegar as cordenadas atuais do usuario):
# https://ipinfo.io/


load_dotenv()

api_key = os.getenv("API_KEY")

# Função para pegar as cordenadas da cidade informada.
"""
Exemplo de como usar a função de buscar as cordenadas da localização digitada pelo usuario

lati,long = cords_by_name(apiKey="",city="Balneario Camboriu", country="BR")

print(lati,long)

"""
def cords_by_name(apiKey, city, country, country_code=None, limit=1):
    
    if country_code:
        location = f"{city},{country_code},{country}"
    else:
        location = f"{city},{country}"
    
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit={limit}&appid={apiKey}"

    cords_request = requests.get(url).json() 

    return cords_request[0]["lat"], cords_request[0]["lon"]

# Função para pegar as cordenadas do usuario ( baseadas no ip do mesmo )

"""
Exemplo de como usar a função de buscar as cordenadas atuais do usuario

user_lat, user_long = get_user_cords()
print(user_lat,user_long)

"""
def get_user_cords():

    url = "https://ipinfo.io/"

    ip_request = requests.get(url).json()

    user_cords = ip_request["loc"].split(",")

    user_lat = user_cords[0]
    user_long = user_cords[1]

    city = ip_request.get("city")
    region = ip_request.get("region")
    country = ip_request.get("country")

    return [user_lat,user_long,city,region,country]

# Função para buscar as informações do clima atual da cidade informada:
"""
Exemplo de como usar a função:

previsao_atual = get_climate_by_name(API,"São Paulo","BR")

print(previsao_atual)

"""

def get_climate_by_name(apiKey,city,country):
    
    cordenadas_dadas_user = cords_by_name(apiKey,city,country)
    previsao = previsao_tempo(cordenadas_dadas_user[0],cordenadas_dadas_user[1],api_key)

    return previsao

# Função para buscar as informações do tempo na cordenada desejada pelo usuario

def previsao_tempo(user_lat, user_long, api_key):

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={user_lat}&lon={user_long}&units=metric&appid={api_key}"

    requisicao = requests.get(url).json()

    return requisicao

# Função para pegar as previsão dos proximos 5 dias
"""


request = days_predict(apiKey="",city="Balneario Camboriu", country="BR")

print(lati,long)

"""
def days_predict(apikey, city, country):

    lat,lon = cords_by_name(apikey,city,country)

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&&appid={apikey}"

    requisicao = requests.get(url).json()

    return requisicao

