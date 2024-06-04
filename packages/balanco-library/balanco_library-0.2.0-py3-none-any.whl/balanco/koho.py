import requests

def fetch_data(id, token):
    response = requests.get(f"https://suite.koho-online.com/api/customers?company_id={id}&token={token}")
    response.raise_for_status()
