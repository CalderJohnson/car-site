"""Get car data from auto.dev api"""
import requests
from website.keys import API_KEY

def getCarData(make, model, year_min):
    """Get car data from auto.dev api"""
    url = f"https://auto.dev/api/listings?api_key={API_KEY}==&make={make}&model={model}&year_min={year_min}"
    response = requests.get(url)
    return response.json()
