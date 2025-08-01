import requests

BASE_URL = "http://localhost:8000"
AUTH_TOKEN = "your_jwt_token_here"  # Bisa hardcode dulu untuk testing

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

def get_agents():
    response = requests.get(f"{BASE_URL}/agent/all", headers=HEADERS)
    return response.json()["data"]

def register_agent(hostname: str, os: str):
    data = {
        "hostname": hostname,
        "os": os
    }
    response = requests.post(f"{BASE_URL}/agent/register", json=data, headers=HEADERS)
    return response.json()

def delete_agent(agent_id: str):
    response = requests.delete(f"{BASE_URL}/agent/{agent_id}", headers=HEADERS)
    return response.json()
