import requests

URL = "https://api.freecurrencyapi.com/v1/latest?apikey="
API_KEY = "fca_live_AIroZcDjFASDdkKLdZ4rjkDBFwPOzJjLI2sAzTSe"

def get_currencies():
    response = requests.get(URL + API_KEY)
    return response.json()
