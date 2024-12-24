import requests
from typing import List

BASE_URL = "https://api.geckoterminal.com/api/v2"
API_KEY = "your_api_key_here"

MARKET_PRICE_ENDPOINT = "/simple/networks/solana/token_price/"

# Define headers for authentication
HEADERS = {
    "Content-Type": "application/json",
    # "Authorization": f"Bearer {API_KEY}"
}

def fetch_data(address: List[str], params=None):
   
    address = ",".join([x for x in address]) 
    print(address)
    url = f"{BASE_URL}{MARKET_PRICE_ENDPOINT}{address}" 
    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        prices = data.get("data", []).get("attributes", []).get("token_prices", {})
        return prices


    except requests.exceptions.RequestException as e:
        print(f"Error fetching prices: {e}")
        return None

        
        

if __name__ == "__main__":
    address: List[str] = ["5odbSFH3kKHFNcy6Kai7ykm7Da9B55Kk9wgy4Fh8GSfh","HgBRWfYxEfvPhtqkaeymCQtHCrKE46qQ43pKe8HCpump"]
    data = fetch_data(address=address)
    
    if data:
        print("Prices:", data)
    else:
        print("Failed to fetch prices.")
