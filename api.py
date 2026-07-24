import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FOOTBALL_API_KEY")
BASE_URL = "https://api.football-data.org/v4"

headers = {"X-Auth-Token": API_KEY}

def get_standings():
    response = requests.get(f"{BASE_URL}/competitions/PL/standings", headers=headers)
    response.raise_for_status()
    return response.json()

def get_scorers():
    response = requests.get(f"{BASE_URL}/competitions/PL/scorers", headers=headers)
    response.raise_for_status()
    return response.json()

def get_matches():
    response = requests.get(f"{BASE_URL}/competitions/PL/matches", headers=headers)
    response.raise_for_status()
    return response.json()



if __name__ == "__main__":
    result = get_standings()
    print(result["standings"][0]["table"][0])

    scorers_result = get_scorers()
    print(scorers_result["scorers"])

    matches_result = get_matches()
    #print (matches_result["matches"][0])

    scorers_result = get_scorers()
    for entry in scorers_result["scorers"]:
        print(entry["type"])

    print(matches_result["resultSet"])
    print(len(matches_result["matches"]))

    


    
    
