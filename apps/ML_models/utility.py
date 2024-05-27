import requests
from django.conf import settings


def get_firebase_data():
    url = f"{settings.FIREBASE_DATABASE_URL}/{settings.FIREBASE_PATH_TO_DATA}.json?auth={settings.FIREBASE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
