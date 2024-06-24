# config.py
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://v3.football.api-sports.io/'
