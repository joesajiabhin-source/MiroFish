import os
import requests
import json
from dotenv import load_dotenv

# Load env from root
load_dotenv(r"c:\Users\abhin\OneDrive\Desktop\BTech S2\HTML\MiroFish-main\.env")

api_key = os.getenv("LLM_FALLBACK_API_KEY")
if not api_key:
    print("No fallback API key found")
    exit()

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
response = requests.get(url)

if response.status_code == 200:
    models = response.json()
    for model in models.get('models', []):
        print(f"{model['name']} - {model.get('displayName', 'No display name')}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
