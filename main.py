# main.py
import requests
from config import API_KEY, BASE_URL

headers = {
    'x-apisports-key': API_KEY
}

def get_leagues():
    url = f"{BASE_URL}/leagues"
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    leagues = get_leagues()
    print(leagues)

